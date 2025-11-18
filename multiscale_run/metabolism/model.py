# ruff: noqa: F841
import numpy as np
from constants import ETC, GeneralParameters
from indexes import MIdx

midx = MIdx()


def _notBigg_J_KH_n(u_h_m_n, u_h_i_n, u_k_m_n):
    return ETC.x_KH * (ETC.K_i * (1e-3 * u_h_m_n) - (1e-6 * u_k_m_n * u_h_i_n))


def _notBigg_J_K_n(u_k_m_n, u_notBigg_MitoMembrPotent_m_n):
    return (
        ETC.x_K
        * u_notBigg_MitoMembrPotent_m_n
        * (
            ETC.K_i * np.exp(ETC.etcF * u_notBigg_MitoMembrPotent_m_n / ETC.etcRT)
            - (1e-3 * u_k_m_n)
        )
        / (np.exp(ETC.etcF * u_notBigg_MitoMembrPotent_m_n / ETC.etcRT) - 1)
    )


def _notBigg_J_MgATPx_n(u_notBigg_ATP_mx_m_n, u_mg2_m_n, ATP_fx_n):
    return ETC.x_MgA * (ATP_fx_n * (1e-3 * u_mg2_m_n) - ETC.K_DT * (1e-3 * u_notBigg_ATP_mx_m_n))


def _notBigg_J_MgADPx_n(u_mg2_m_n, u_notBigg_ADP_mx_m_n, ADP_fx_n):
    return ETC.x_MgA * (ADP_fx_n * (1e-3 * u_mg2_m_n) - ETC.K_DD * (1e-3 * u_notBigg_ADP_mx_m_n))


def compute_du(u, p, t):
    # unpack
    u_h_m_n = u[midx.h_m_n]
    u_k_m_n = u[midx.k_m_n]
    u_mg2_m_n = u[midx.mg2_m_n]
    u_atp_m_n = u[midx.atp_m_n]
    u_adp_m_n = u[midx.adp_m_n]
    u_notBigg_ATP_mx_m_n = u[midx.notBigg_ATP_mx_m_n]
    u_notBigg_ADP_mx_m_n = u[midx.notBigg_ADP_mx_m_n]

    u_notBigg_MitoMembrPotent_m_n = u[midx.notBigg_MitoMembrPotent_m_n]
    u_h_i_n = u[midx.h_i_n]

    # convenience values
    ATPmito_nM = 1e-3 * u[midx.atp_m_n]
    ATP_mx_nM = 1e-3 * u[midx.notBigg_ATP_mx_m_n]
    ATP_fx_n = ATPmito_nM - ATP_mx_nM
    ADPmito_nM = 1e-3 * u[midx.adp_m_n]
    ADP_mx_nM = 1e-3 * u[midx.notBigg_ADP_mx_m_n]
    ADP_fx_n = ADPmito_nM - ADP_mx_nM

    # build du
    du = np.zeros_like(u)

    # du[midx.h_m_n] = 0 # already at 0
    du[midx.k_m_n] = (
        0.5
        * GeneralParameters.T2Jcorrection
        * (
            1000
            * (
                _notBigg_J_KH_n(u_h_m_n, u_h_i_n, u_k_m_n)
                + _notBigg_J_K_n(u_k_m_n, u_notBigg_MitoMembrPotent_m_n)
            )
            / ETC.W_x
        )
    )
    du[midx.mg2_m_n] = (
        0.5
        * GeneralParameters.T2Jcorrection
        * (
            1000
            * (
                -_notBigg_J_MgATPx_n(u_notBigg_ATP_mx_m_n, u_mg2_m_n, ATP_fx_n)
                - _notBigg_J_MgADPx_n(u_mg2_m_n, u_notBigg_ADP_mx_m_n, ADP_fx_n)
            )
            / ETC.W_x
        )
    )
    return du


if __name__ == "__main__":
    # Instantiate indexes
    midx = MIdx()

    # Print indexes and comments
    print("Indexes and comments:")
    print(midx)
    print(f"Total vars: {midx.size}\n")

    # Create a dummy u array
    u = np.ones(midx.size) * 1.0  # all ones
    p = []  # dummy, unused in this simple test
    t = 0.0  # dummy time

    # Call compute_du
    du = compute_du(u, p, t)

    # Print a few du values to check
    print("du:", du)
