# ruff: noqa: F841

import numpy as np

from multiscale_run.metabolism.constants import (
    ATDMP,
    ETC,
    MAS,
    TCA,
    BfInput,
    Creatine,
    Ephys,
    GeneralConstants,
    Generalizations,
    GLCtransport,
    Gltgln,
    Glycogen,
    Glycolysis,
    Gshgssg,
    Ketones,
    Lactate,
    PPP_a,
    PPP_n,
    PyrCarb,
    PyrTrCytoMito,
)
from multiscale_run.metabolism.indexes import PIdx, UIdx


def compute_du(u, p, t):
    # unpack p
    p_ina_density = p[PIdx.ina_density]
    p_ik_density = p[PIdx.ik_density]
    p_mito_scale = p[PIdx.mito_scale]
    p_notBigg_FinDyn_W2017 = p[PIdx.notBigg_FinDyn_W2017]
    p_notBigg_Fout_W2017 = p[PIdx.notBigg_Fout_W2017]
    p_notBigg_vV_b_b = p[PIdx.notBigg_vV_b_b]

    # unpack u
    u_h_m_n = u[UIdx.h_m_n]
    u_k_m_n = u[UIdx.k_m_n]
    u_mg2_m_n = u[UIdx.mg2_m_n]
    u_nadh_m_n = u[UIdx.nadh_m_n]
    u_q10h2_m_n = u[UIdx.q10h2_m_n]
    u_focytC_m_n = u[UIdx.focytC_m_n]
    u_o2_c_n = u[UIdx.o2_c_n]
    u_atp_m_n = u[UIdx.atp_m_n]
    u_adp_m_n = u[UIdx.adp_m_n]
    u_notBigg_ATP_mx_m_n = u[UIdx.notBigg_ATP_mx_m_n]
    u_notBigg_ADP_mx_m_n = u[UIdx.notBigg_ADP_mx_m_n]
    u_pi_m_n = u[UIdx.pi_m_n]
    u_atp_i_n = u[UIdx.atp_i_n]
    u_adp_i_n = u[UIdx.adp_i_n]
    u_amp_i_n = u[UIdx.amp_i_n]
    u_notBigg_ATP_mi_i_n = u[UIdx.notBigg_ATP_mi_i_n]
    u_notBigg_ADP_mi_i_n = u[UIdx.notBigg_ADP_mi_i_n]
    u_pi_i_n = u[UIdx.pi_i_n]
    u_notBigg_MitoMembrPotent_m_n = u[UIdx.notBigg_MitoMembrPotent_m_n]
    u_notBigg_Ctot_m_n = u[UIdx.notBigg_Ctot_m_n]
    u_notBigg_Qtot_m_n = u[UIdx.notBigg_Qtot_m_n]
    u_h_i_n = u[UIdx.h_i_n]
    u_atp_c_n = u[UIdx.atp_c_n]
    u_fum_m_n = u[UIdx.fum_m_n]
    u_mal_L_m_n = u[UIdx.mal_L_m_n]
    u_oaa_m_n = u[UIdx.oaa_m_n]
    u_succ_m_n = u[UIdx.succ_m_n]
    u_succoa_m_n = u[UIdx.succoa_m_n]
    u_coa_m_n = u[UIdx.coa_m_n]
    u_akg_m_n = u[UIdx.akg_m_n]
    u_ca2_m_n = u[UIdx.ca2_m_n]
    u_icit_m_n = u[UIdx.icit_m_n]
    u_cit_m_n = u[UIdx.cit_m_n]
    u_accoa_m_n = u[UIdx.accoa_m_n]
    u_acac_c_n = u[UIdx.acac_c_n]
    u_aacoa_m_n = u[UIdx.aacoa_m_n]
    u_pyr_m_n = u[UIdx.pyr_m_n]
    u_bhb_c_n = u[UIdx.bhb_c_n]
    u_bhb_e_e = u[UIdx.bhb_e_e]
    u_bhb_c_a = u[UIdx.bhb_c_a]
    u_bhb_b_b = u[UIdx.bhb_b_b]
    u_asp_L_m_n = u[UIdx.asp_L_m_n]
    u_asp_L_c_n = u[UIdx.asp_L_c_n]
    u_glu_L_m_n = u[UIdx.glu_L_m_n]
    u_mal_L_c_n = u[UIdx.mal_L_c_n]
    u_oaa_c_n = u[UIdx.oaa_c_n]
    u_akg_c_n = u[UIdx.akg_c_n]
    u_glu_L_c_n = u[UIdx.glu_L_c_n]
    u_nadh_c_n = u[UIdx.nadh_c_n]
    u_h_m_a = u[UIdx.h_m_a]
    u_k_m_a = u[UIdx.k_m_a]
    u_mg2_m_a = u[UIdx.mg2_m_a]
    u_nadh_m_a = u[UIdx.nadh_m_a]
    u_q10h2_m_a = u[UIdx.q10h2_m_a]
    u_focytC_m_a = u[UIdx.focytC_m_a]
    u_o2_c_a = u[UIdx.o2_c_a]
    u_atp_m_a = u[UIdx.atp_m_a]
    u_adp_m_a = u[UIdx.adp_m_a]
    u_notBigg_ATP_mx_m_a = u[UIdx.notBigg_ATP_mx_m_a]
    u_notBigg_ADP_mx_m_a = u[UIdx.notBigg_ADP_mx_m_a]
    u_pi_m_a = u[UIdx.pi_m_a]
    u_atp_i_a = u[UIdx.atp_i_a]
    u_adp_i_a = u[UIdx.adp_i_a]
    u_amp_i_a = u[UIdx.amp_i_a]
    u_notBigg_ATP_mi_i_a = u[UIdx.notBigg_ATP_mi_i_a]
    u_notBigg_ADP_mi_i_a = u[UIdx.notBigg_ADP_mi_i_a]
    u_pi_i_a = u[UIdx.pi_i_a]
    u_notBigg_MitoMembrPotent_m_a = u[UIdx.notBigg_MitoMembrPotent_m_a]
    u_notBigg_Ctot_m_a = u[UIdx.notBigg_Ctot_m_a]
    u_notBigg_Qtot_m_a = u[UIdx.notBigg_Qtot_m_a]
    u_h_i_a = u[UIdx.h_i_a]
    u_atp_c_a = u[UIdx.atp_c_a]
    u_fum_m_a = u[UIdx.fum_m_a]
    u_mal_L_m_a = u[UIdx.mal_L_m_a]
    u_oaa_m_a = u[UIdx.oaa_m_a]
    u_succ_m_a = u[UIdx.succ_m_a]
    u_succoa_m_a = u[UIdx.succoa_m_a]
    u_coa_m_a = u[UIdx.coa_m_a]
    u_akg_m_a = u[UIdx.akg_m_a]
    u_ca2_m_a = u[UIdx.ca2_m_a]
    u_icit_m_a = u[UIdx.icit_m_a]
    u_cit_m_a = u[UIdx.cit_m_a]
    u_accoa_m_a = u[UIdx.accoa_m_a]
    u_acac_c_a = u[UIdx.acac_c_a]
    u_aacoa_m_a = u[UIdx.aacoa_m_a]
    u_pyr_m_a = u[UIdx.pyr_m_a]
    u_gln_L_c_n = u[UIdx.gln_L_c_n]
    u_gln_L_e_e = u[UIdx.gln_L_e_e]
    u_gln_L_c_a = u[UIdx.gln_L_c_a]
    u_glu_L_c_a = u[UIdx.glu_L_c_a]
    u_notBigg_Va_c_a = u[UIdx.notBigg_Va_c_a]
    u_na1_c_a = u[UIdx.na1_c_a]
    u_k_c_a = u[UIdx.k_c_a]
    u_k_e_e = u[UIdx.k_e_e]
    u_glu_L_syn_syn = u[UIdx.glu_L_syn_syn]
    u_notBigg_VNeu_c_n = u[UIdx.notBigg_VNeu_c_n]
    u_na1_c_n = u[UIdx.na1_c_n]
    u_notBigg_hgate_c_n = u[UIdx.notBigg_hgate_c_n]
    u_notBigg_ngate_c_n = u[UIdx.notBigg_ngate_c_n]
    u_ca2_c_n = u[UIdx.ca2_c_n]
    u_notBigg_pgate_c_n = u[UIdx.notBigg_pgate_c_n]
    u_notBigg_nBK_c_a = u[UIdx.notBigg_nBK_c_a]
    u_notBigg_mGluRboundRatio_c_a = u[UIdx.notBigg_mGluRboundRatio_c_a]
    u_notBigg_IP3_c_a = u[UIdx.notBigg_IP3_c_a]
    u_notBigg_hIP3Ca_c_a = u[UIdx.notBigg_hIP3Ca_c_a]
    u_ca2_c_a = u[UIdx.ca2_c_a]
    u_ca2_r_a = u[UIdx.ca2_r_a]
    u_notBigg_sTRP_c_a = u[UIdx.notBigg_sTRP_c_a]
    u_notBigg_EET_c_a = u[UIdx.notBigg_EET_c_a]
    u_notBigg_ddHb_b_b = u[UIdx.notBigg_ddHb_b_b]
    u_o2_b_b = u[UIdx.o2_b_b]
    u_glc_D_b_b = u[UIdx.glc_D_b_b]
    u_glc_D_ecsEndothelium_ecsEndothelium = u[UIdx.glc_D_ecsEndothelium_ecsEndothelium]
    u_glc_D_ecsBA_ecsBA = u[UIdx.glc_D_ecsBA_ecsBA]
    u_glc_D_c_a = u[UIdx.glc_D_c_a]
    u_glc_D_ecsAN_ecsAN = u[UIdx.glc_D_ecsAN_ecsAN]
    u_glc_D_c_n = u[UIdx.glc_D_c_n]
    u_g6p_c_n = u[UIdx.g6p_c_n]
    u_g6p_c_a = u[UIdx.g6p_c_a]
    u_f6p_c_n = u[UIdx.f6p_c_n]
    u_f6p_c_a = u[UIdx.f6p_c_a]
    u_fdp_c_n = u[UIdx.fdp_c_n]
    u_fdp_c_a = u[UIdx.fdp_c_a]
    u_f26bp_c_a = u[UIdx.f26bp_c_a]
    u_glycogen_c_a = u[UIdx.glycogen_c_a]
    u_amp_c_n = u[UIdx.amp_c_n]
    u_amp_c_a = u[UIdx.amp_c_a]
    u_g1p_c_a = u[UIdx.g1p_c_a]
    u_g3p_c_n = u[UIdx.g3p_c_n]
    u_g3p_c_a = u[UIdx.g3p_c_a]
    u_dhap_c_n = u[UIdx.dhap_c_n]
    u_dhap_c_a = u[UIdx.dhap_c_a]
    u_n13dpg_c_n = u[UIdx.n13dpg_c_n]
    u_n13dpg_c_a = u[UIdx.n13dpg_c_a]
    u_nadh_c_a = u[UIdx.nadh_c_a]
    u_pi_c_n = u[UIdx.pi_c_n]
    u_pi_c_a = u[UIdx.pi_c_a]
    u_n3pg_c_n = u[UIdx.n3pg_c_n]
    u_n3pg_c_a = u[UIdx.n3pg_c_a]
    u_n2pg_c_n = u[UIdx.n2pg_c_n]
    u_n2pg_c_a = u[UIdx.n2pg_c_a]
    u_pep_c_n = u[UIdx.pep_c_n]
    u_pep_c_a = u[UIdx.pep_c_a]
    u_pyr_c_n = u[UIdx.pyr_c_n]
    u_pyr_c_a = u[UIdx.pyr_c_a]
    u_lac_L_b_b = u[UIdx.lac_L_b_b]
    u_lac_L_e_e = u[UIdx.lac_L_e_e]
    u_lac_L_c_a = u[UIdx.lac_L_c_a]
    u_lac_L_c_n = u[UIdx.lac_L_c_n]
    u_nadph_c_n = u[UIdx.nadph_c_n]
    u_nadph_c_a = u[UIdx.nadph_c_a]
    u_n6pgl_c_n = u[UIdx.n6pgl_c_n]
    u_n6pgl_c_a = u[UIdx.n6pgl_c_a]
    u_n6pgc_c_n = u[UIdx.n6pgc_c_n]
    u_n6pgc_c_a = u[UIdx.n6pgc_c_a]
    u_ru5p_D_c_n = u[UIdx.ru5p_D_c_n]
    u_ru5p_D_c_a = u[UIdx.ru5p_D_c_a]
    u_r5p_c_n = u[UIdx.r5p_c_n]
    u_r5p_c_a = u[UIdx.r5p_c_a]
    u_xu5p_D_c_n = u[UIdx.xu5p_D_c_n]
    u_xu5p_D_c_a = u[UIdx.xu5p_D_c_a]
    u_s7p_c_n = u[UIdx.s7p_c_n]
    u_s7p_c_a = u[UIdx.s7p_c_a]
    u_e4p_c_n = u[UIdx.e4p_c_n]
    u_e4p_c_a = u[UIdx.e4p_c_a]
    u_gthrd_c_n = u[UIdx.gthrd_c_n]
    u_gthrd_c_a = u[UIdx.gthrd_c_a]
    u_gthox_c_n = u[UIdx.gthox_c_n]
    u_gthox_c_a = u[UIdx.gthox_c_a]
    u_creat_c_n = u[UIdx.creat_c_n]
    u_pcreat_c_n = u[UIdx.pcreat_c_n]
    u_creat_c_a = u[UIdx.creat_c_a]
    u_pcreat_c_a = u[UIdx.pcreat_c_a]
    u_camp_c_a = u[UIdx.camp_c_a]
    u_nrpphr_e_e = u[UIdx.nrpphr_e_e]
    u_udpg_c_a = u[UIdx.udpg_c_a]
    u_utp_c_a = u[UIdx.utp_c_a]
    u_notBigg_GS_c_a = u[UIdx.notBigg_GS_c_a]
    u_notBigg_GPa_c_a = u[UIdx.notBigg_GPa_c_a]
    u_notBigg_GPb_c_a = u[UIdx.notBigg_GPb_c_a]

    # convenience values

    ## initial simplifications
    p_notBigg_Fout_W2017 = p_notBigg_FinDyn_W2017
    NADtot_n = ETC.NADtot
    NADtot_a = ETC.NADtot
    NAD_aging_coeff_n = 1.0
    NAD_aging_coeff_a = 1.0
    NAD_aging_coeff_mn = 1.0
    NAD_aging_coeff_ma = 1.0
    NADHshuttle_aging_n = 1.0
    NADHshuttle_aging_a = 1.0
    syn_aging_coeff = 1.0

    ## replacements in unpacking
    j_un = ATDMP.qAK * (ATDMP.qAK + 4 * (ATDMP.ATDPtot_n / u_atp_c_n - 1))
    j_ug = ATDMP.qAK * (ATDMP.qAK + 4 * (ATDMP.ATDPtot_a / u_atp_c_a - 1))
    u_adp_c_n = u_atp_c_n / 2 * (-ATDMP.qAK + np.sqrt(j_un))
    u_adp_c_a = u_atp_c_a / 2 * (-ATDMP.qAK + np.sqrt(j_ug))

    ## aliases
    u_h_c_n = GeneralConstants.C_H_cyt_n
    u_h_c_a = GeneralConstants.C_H_cyt_a
    u_co2_m_n = GeneralConstants.CO2_mito_n
    u_co2_m_a = GeneralConstants.CO2_mito_a
    u_ppi_c_a = GeneralConstants.PPi_a0
    u_notBigg_PHKa_c_a = GeneralConstants.PHKa_a0
    u_notBigg_PP1_c_a_initialValue = GeneralConstants.PP1_a0
    H2PIi_n = (1e-3 * u_pi_i_n) * (1e-3 * u_h_i_n) / ((1e-3 * u_h_i_n) + ETC.k_dHPi)
    H2PIx_n = (1e-3 * u_pi_m_n) * (1e-3 * u_h_m_n) / ((1e-3 * u_h_m_n) + ETC.k_dHPi)
    H2PIi_a = (1e-3 * u_pi_i_a) * (1e-3 * u_h_i_a) / ((1e-3 * u_h_i_a) + ETC.k_dHPi)
    H2PIx_a = (1e-3 * u_pi_m_a) * (1e-3 * u_h_m_a) / ((1e-3 * u_h_m_a) + ETC.k_dHPi)

    Pi_n = u_pi_c_n
    Pi_a = u_pi_c_a
    C_H_mitomatr_nM = 1e-3 * u_h_m_n
    K_x_nM = 1e-3 * u_k_m_n
    Mg_x_nM = 1e-3 * u_mg2_m_n
    NADHmito_nM = 1e-3 * u_nadh_m_n
    QH2mito_nM = 1e-3 * u_q10h2_m_n
    CytCredmito_nM = 1e-3 * u_focytC_m_n
    O2_nM = 1e-3 * u_o2_c_n
    ATPmito_nM = 1e-3 * u_atp_m_n
    ADPmito_nM = 1e-3 * u_adp_m_n
    Cr_n = Creatine.Crtot - u_pcreat_c_n
    Cr_a = Creatine.Crtot - u_pcreat_c_a
    ADP_n = u_atp_c_n / 2 * (-ATDMP.qAK + np.sqrt(j_un))
    ADP_a = u_atp_c_a / 2 * (-ATDMP.qAK + np.sqrt(j_ug))
    dAMPdATPn = (
        -1
        + ATDMP.qAK / 2
        - 0.5 * np.sqrt(j_un)
        + ATDMP.qAK * ATDMP.ATDPtot_n / (u_atp_c_n * np.sqrt(j_un))
    )
    dAMPdATPg = (
        -1
        + ATDMP.qAK / 2
        - 0.5 * np.sqrt(j_ug)
        + ATDMP.qAK * ATDMP.ATDPtot_a / (u_atp_c_a * np.sqrt(j_ug))
    )
    ATP_nM = 1e-3 * u_atp_c_n
    ADP_nM = 1e-3 * ADP_n
    ATP_aM = 1e-3 * u_atp_c_a
    ADP_aM = 1e-3 * ADP_a
    ATP_mx_nM = 1e-3 * u_notBigg_ATP_mx_m_n
    ADP_mx_nM = 1e-3 * u_notBigg_ADP_mx_m_n
    Pimito_nM = 1e-3 * u_pi_m_n
    ATP_i_nM = 1e-3 * u_atp_i_n
    ADP_i_nM = 1e-3 * u_adp_i_n
    AMP_i_nM = 1e-3 * u_amp_i_n
    ATP_mi_nM = 1e-3 * u_notBigg_ATP_mi_i_n
    ADP_mi_nM = 1e-3 * u_notBigg_ADP_mi_i_n
    Pi_i_nM = 1e-3 * u_pi_i_n
    Ctot_nM = 1e-3 * u_notBigg_Ctot_m_n
    Qtot_nM = 1e-3 * u_notBigg_Qtot_m_n
    C_H_ims_nM = 1e-3 * u_h_i_n
    AMP_nM = 0
    NAD_x_n = NADtot_n - NADHmito_nM
    u_nad_m_n = 1000 * NAD_x_n
    Q_n = Qtot_nM - QH2mito_nM
    Qmito_n = 1000 * Q_n
    Cox_n = Ctot_nM - CytCredmito_nM
    ATP_fx_n = ATPmito_nM - ATP_mx_nM
    ADP_fx_n = ADPmito_nM - ADP_mx_nM
    ATP_fi_n = ATP_i_nM - ATP_mi_nM
    ADP_fi_n = ADP_i_nM - ADP_mi_nM
    ADP_me_n = (
        (ETC.K_DD + ADP_nM + ETC.Mg_tot)
        - np.sqrt((ETC.K_DD + ADP_nM + ETC.Mg_tot) ** 2 - 4 * (ETC.Mg_tot * ADP_nM))
    ) / 2
    Mg_i_n = ETC.Mg_tot - ADP_me_n
    dG_H_n = ETC.etcF * u_notBigg_MitoMembrPotent_m_n + 1 * ETC.etcRT * np.log(C_H_ims_nM / C_H_mitomatr_nM)
    dG_C1op_n = ETC.dG_C1o - 1 * ETC.etcRT * np.log(C_H_mitomatr_nM / 1e-7)
    dG_C3op_n = ETC.dG_C3o + 2 * ETC.etcRT * np.log(C_H_mitomatr_nM / 1e-7)
    dG_C4op_n = ETC.dG_C4o - 2 * ETC.etcRT * np.log(C_H_mitomatr_nM / 1e-7)
    dG_F1op_n = ETC.dG_F1o - 1 * ETC.etcRT * np.log(C_H_mitomatr_nM / 1e-7)
    C_H_mitomatr_a = u_h_m_a
    C_H_mitomatr_aM = 1e-3 * u_h_m_a
    K_x_aM = 1e-3 * u_k_m_a
    Mg_x_aM = 1e-3 * u_mg2_m_a
    NADHmito_aM = 1e-3 * u_nadh_m_a
    QH2mito_aM = 1e-3 * u_q10h2_m_a
    CytCredmito_aM = 1e-3 * u_focytC_m_a
    O2_aM = 1e-3 * u_o2_c_a
    ATPmito_aM = 1e-3 * u_atp_m_a
    ADPmito_aM = 1e-3 * u_adp_m_a
    ATP_mx_aM = 1e-3 * u_notBigg_ATP_mx_m_a
    ADP_mx_aM = 1e-3 * u_notBigg_ADP_mx_m_a
    Pimito_aM = 1e-3 * u_pi_m_a
    ATP_i_aM = 1e-3 * u_atp_i_a
    ADP_i_aM = 1e-3 * u_adp_i_a
    AMP_i_aM = 1e-3 * u_amp_i_a
    ATP_mi_aM = 1e-3 * u_notBigg_ATP_mi_i_a
    ADP_mi_aM = 1e-3 * u_notBigg_ADP_mi_i_a
    Pi_i_aM = 1e-3 * u_pi_i_a
    Ctot_aM = 1e-3 * u_notBigg_Ctot_m_a
    Qtot_aM = 1e-3 * u_notBigg_Qtot_m_a
    C_H_ims_aM = 1e-3 * u_h_i_a
    AMP_aM = 0
    NAD_x_a = NADtot_a - NADHmito_aM
    u_nad_m_a = 1000 * NAD_x_a
    Q_a = Qtot_aM - QH2mito_aM
    Qmito_a = 1000 * Q_a
    Cox_a = Ctot_aM - CytCredmito_aM
    ATP_fx_a = ATPmito_aM - ATP_mx_aM
    ADP_fx_a = ADPmito_aM - ADP_mx_aM
    ATP_fi_a = ATP_i_aM - ATP_mi_aM
    ADP_fi_a = ADP_i_aM - ADP_mi_aM
    ADP_me_a = (
        (ETC.K_DD_a + ADP_aM + ETC.Mg_tot)
        - np.sqrt((ETC.K_DD_a + ADP_aM + ETC.Mg_tot) ** 2 - 4 * (ETC.Mg_tot * ADP_aM))
    ) / 2
    Mg_i_a = ETC.Mg_tot - ADP_me_a
    dG_H_a = ETC.etcF * u_notBigg_MitoMembrPotent_m_a + 1 * ETC.etcRT * np.log(
        C_H_ims_aM / C_H_mitomatr_aM
    )
    dG_C1op_a = ETC.dG_C1o - 1 * ETC.etcRT * np.log(C_H_mitomatr_aM / 1e-7)
    dG_C3op_a = ETC.dG_C3o + 2 * ETC.etcRT * np.log(C_H_mitomatr_aM / 1e-7)
    dG_C4op_a = ETC.dG_C4o - 2 * ETC.etcRT * np.log(C_H_mitomatr_aM / 1e-7)
    dG_F1op_a = ETC.dG_F1o - 1 * ETC.etcRT * np.log(C_H_mitomatr_aM / 1e-7)
    u_nadp_c_n = 0.0303 - u_nadph_c_n
    u_nadp_c_a = 0.0303 - u_nadph_c_a
    u_nad_c_n = 0.212 - u_nadh_c_n
    u_nad_c_a = 0.212 - u_nadh_c_a

    # V=u[98]
    # rTRPVsinf=u[111]

    Glutamate_syn = u_glu_L_syn_syn

    # alpham=-0.1*(V+33)/(np.exp(-0.1*(V+33))-1)
    # betam=4*np.exp(-(V+58)/12)
    # alphah=0.07*np.exp(-(V+50)/10)
    # betah=1/(np.exp(-0.1*(V+20))+1)
    # alphan=-0.01*(V+34)/(np.exp(-0.1*(V+34))-1)
    # betan=0.125*np.exp(-(V+44)/25)
    # minf=alpham/(alpham+betam)
    # ninf=alphan/(alphan+betan)
    # hinf=alphah/(alphah+betah)
    # taun=1/(alphan+betan)*1e-03
    # tauh=1/(alphah+betah)*1e-03
    # p_inf=1.0/(1.0+np.exp(-(V+35.0)/10.0))
    # tau_p=tau_max/(3.3*np.exp((V+35.0)/20.0)+np.exp(-(V+35.0)/20.0))
    # K_n=K_n_Rest+(Na_n_Rest-u[99])
    # EK=RTF*log(u[96]/K_n)
    # EL=gKpas*EK/(gKpas+gNan)+gNan/(gKpas+gNan)*RTF*log(Na_out/u[99])
    # IL=gL*(V-EL)
    # INa=ina_density #gNa*minf**3*u[100]*(V-RTF*log(Na_out/u[99]))
    # IK=ik_density #gK*u[101]**4*(V-EK)
    # mCa=1/(1+np.exp(-(V+20)/9))
    # ICa=gCa*mCa**2*(V-ECa)
    # ImAHP=gmAHP*u[102]/(u[102]+KD)*(V-EK)
    # IM=g_M*u[103]*(V-EK)

    # dIPump=F*kPumpn*u_atp_c_n*(u[99]-u0_ss[99])/(1+u_atp_c_n/KmPump)
    # dIPump_a=F*kPumpg*u_atp_c_a*(u[94]-u0_ss[94])/(1+u_atp_c_a/KmPump)
    # Isyne=-synInput*(V-Ee)
    # Isyni=0

    # vnstim=SmVn/F*ina_density #SmVn/F*(2/3*Isyne-INa)
    # vgstim=SmVg/F*glia*ina_density #SmVg/F*2/3*glia*synInput
    # vLeakNan=SmVn*gNan/F*(RTF*log(Na_out/u[99])-V)
    # vLeakNag=SmVg*gNag/F*(RTF*log(Na_out/u[94])-V)
    # vPumpn=SmVn*kPumpn*u_atp_c_n*u[99]/(1+u_atp_c_n/KmPump)
    vPumpg = Ephys.SmVg * Ephys.kPumpg * u_atp_c_a * u_na1_c_a / (1 + u_atp_c_a / Ephys.KmPump)

    # functions (here turned into values for speed). Names are prepended with f_
    f_r0509_n = ETC.x_DH*(ETC.r_DH*NAD_x_n-(1e-3*u_nadh_m_n))*((1+(1e-3*u_pi_m_n)/ETC.k_Pi1)/(1+(1e-3*u_pi_m_n)/ETC.k_Pi2))
    f_NADH2_u10mi_n = ETC.x_C1*(np.exp(-(dG_C1op_n+4*dG_H_n)/ETC.etcRT)*(1e-3*u_nadh_m_n)*Q_n-NAD_x_n*(1e-3*u_q10h2_m_n))
    f_CYOR_u10mi_n = ETC.x_C3*((1+(1e-3*u_pi_m_n)/ETC.k_Pi3)/(1+(1e-3*u_pi_m_n)/ETC.k_Pi4))*(np.exp(-(dG_C3op_n+4*dG_H_n-2*ETC.etcF*u_notBigg_MitoMembrPotent_m_n)/(2*ETC.etcRT))*Cox_n*(1e-3*u_q10h2_m_n)**0.5-(1e-3*u_focytC_m_n)*Q_n**0.5)
    f_CYOOm2i_n = 1*(ETC.x_C4*((1e-3*u_o2_c_n)/((1e-3*u_o2_c_n)+ETC.k_O2))*((1e-3*u_focytC_m_n)/(1e-3*u_notBigg_Ctot_m_n))*(np.exp(-(dG_C4op_n+2*dG_H_n)/(2*ETC.etcRT))*(1e-3*u_focytC_m_n)*((1e-3*u_o2_c_n)**0.25)-Cox_n*np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_n/ETC.etcRT)))
    f_ATPS4mi_n = ETC.x_F1*(np.exp(-(dG_F1op_n-ETC.n_A*dG_H_n)/ETC.etcRT)*(ETC.K_DD/ETC.K_DT)*(1e-3*u_notBigg_ADP_mx_m_n)*(1e-3*u_pi_m_n)-(1e-3*u_notBigg_ATP_mx_m_n))

    f_ATPtm_n = ETC.x_ANT*(ADP_fi_n/(ADP_fi_n+ATP_fi_n*np.exp(-ETC.etcF*(0.35*u_notBigg_MitoMembrPotent_m_n)/ETC.etcRT))-ADP_fx_n/(ADP_fx_n+ATP_fx_n*np.exp(-ETC.etcF*(-0.65*u_notBigg_MitoMembrPotent_m_n)/ETC.etcRT)))*(ADP_fi_n/(ADP_fi_n+ETC.k_mADP))
    f_notBigg_J_Pi1_n = ETC.x_Pi1*((1e-3*u_h_m_n)*H2PIi_n-(1e-3*u_h_i_n)*H2PIx_n)/(H2PIi_n+ETC.k_PiH)
    f_notBigg_J_Hle_n = ETC.x_Hle*u_notBigg_MitoMembrPotent_m_n*((1e-3*u_h_i_n)*np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_n/ETC.etcRT)-(1e-3*u_h_m_n))/(np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_n/ETC.etcRT)-1)
    f_notBigg_J_KH_n = ETC.x_KH*(ETC.K_i*(1e-3*u_h_m_n)-(1e-3*u_k_m_n)*(1e-3*u_h_i_n))
    f_notBigg_J_K_n = ETC.x_K*u_notBigg_MitoMembrPotent_m_n*(ETC.K_i*np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_n/ETC.etcRT)-(1e-3*u_k_m_n))/(np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_n/ETC.etcRT)-1)
    f_ADK1m_n = ETC.x_AK*(ETC.K_AK*(1e-3*u_adp_i_n)*(1e-3*u_adp_i_n)-(1e-3*u_amp_i_n)*(1e-3*u_atp_i_n))
    f_notBigg_J_AMP_n = ETC.gamma*ETC.x_A*((1e-3*u_amp_c_n)-(1e-3*u_amp_i_n))
    f_notBigg_J_ADP_n = ETC.gamma*ETC.x_A*((1e-3*u_adp_c_n)-(1e-3*u_adp_i_n))
    f_notBigg_J_ATP_n = ETC.gamma*ETC.x_A*((1e-3*u_atp_c_n)-(1e-3*u_atp_i_n))
    f_notBigg_J_Pi2_n = ETC.gamma*ETC.x_Pi2*(1e-3*u_pi_c_n-(1e-3*u_pi_i_n))
    f_notBigg_J_Ht_n = ETC.gamma*ETC.x_Ht*(1e-3*u_h_c_n-(1e-3*u_h_i_n))
    f_notBigg_J_MgATPx_n = ETC.x_MgA*(ATP_fx_n*(1e-3*u_mg2_m_n)-ETC.K_DT*(1e-3*u_notBigg_ATP_mx_m_n))
    f_notBigg_J_MgADPx_n = ETC.x_MgA*(ADP_fx_n*(1e-3*u_mg2_m_n)-ETC.K_DD*(1e-3*u_notBigg_ADP_mx_m_n))
    f_notBigg_J_MgATPi_n = ETC.x_MgA*(ATP_fi_n*Mg_i_n-ETC.K_DT*(1e-3*u_notBigg_ATP_mi_i_n))
    f_notBigg_J_MgADPi_n = ETC.x_MgA*(ADP_fi_n*Mg_i_n-ETC.K_DD*(1e-3*u_notBigg_ADP_mi_i_n))
    f_PDHm_n = TCA.VmaxPDHCmito_n*(u_pyr_m_n/(u_pyr_m_n+TCA.KmPyrMitoPDH_n))*(u_nad_m_n/(u_nad_m_n+TCA.KmNADmitoPDH_na))*(u_coa_m_n/(u_coa_m_n+TCA.KmCoAmitoPDH_n))
    f_CSm_n = 1*(TCA.VmaxCSmito_n*(u_oaa_m_n/(u_oaa_m_n+TCA.KmOxaMito_n*(1.0+u_cit_m_n/TCA.KiCitMito_n)))*(u_accoa_m_n/(u_accoa_m_n+TCA.KmAcCoAmito_n*(1.0+u_coa_m_n/TCA.KiCoA_n))))
    f_ACONTm_n = 1*(TCA.VmaxAco_n*(u_cit_m_n-u_icit_m_n/TCA.KeqAco_na)/(1.0+u_cit_m_n/TCA.KmCitAco_n+u_icit_m_n/TCA.KmIsoCitAco_n))
    f_ICDHxm_n = 1*(TCA.VmaxIDH_n*(u_nad_m_n/TCA.KiNADmito_na)*((u_icit_m_n/TCA.KmIsoCitIDHm_n)**TCA.nIDH)/(1.0+u_nad_m_n/TCA.KiNADmito_na+(TCA.KmNADmito_na/TCA.KiNADmito_na)*((u_icit_m_n/TCA.KmIsoCitIDHm_n)**TCA.nIDH)+u_nadh_m_n/TCA.KiNADHmito_na+(u_nad_m_n/TCA.KiNADmito_na)*((u_icit_m_n/TCA.KmIsoCitIDHm_n)**TCA.nIDH)+((TCA.KmNADmito_na*u_nadh_m_n)/(TCA.KiNADmito_na*TCA.KiNADHmito_na))*((u_icit_m_n/TCA.KmIsoCitIDHm_n)**TCA.nIDH)))
    f_AKGDm_n = 1*((TCA.VmaxKGDH_n*(1+u_adp_m_n/TCA.KiADPmito_KGDH_n)*(u_akg_m_n/TCA.Km1KGDHKGDH_n)*(u_coa_m_n/TCA.Km_CoA_kgdhKGDH_n)*(u_nad_m_n/TCA.KmNADkgdhKGDH_na))/(((u_coa_m_n/TCA.Km_CoA_kgdhKGDH_n)*(u_nad_m_n/TCA.KmNADkgdhKGDH_na)*(u_akg_m_n/TCA.Km1KGDHKGDH_n+(1+u_atp_m_n/TCA.KiATPmito_KGDH_n)/(1+u_ca2_m_n/TCA.KiCa2KGDH_n)))+((u_akg_m_n/TCA.Km1KGDHKGDH_n)*(u_coa_m_n/TCA.Km_CoA_kgdhKGDH_n+u_nad_m_n/TCA.KmNADkgdhKGDH_na)*(1+u_nadh_m_n/TCA.KiNADHKGDHKGDH_na+u_succoa_m_n/TCA.Ki_SucCoA_kgdhKGDH_n))))
    f_SUCOASm_n = 1*(TCA.VmaxSuccoaATPscs_n*(1+TCA.AmaxPscs_n*((u_pi_m_n**TCA.npscs_n)/((u_pi_m_n**TCA.npscs_n)+(TCA.Km_pi_scs_na**TCA.npscs_n))))*(u_succoa_m_n*u_adp_m_n*u_pi_m_n-u_succ_m_n*u_coa_m_n*u_atp_m_n/TCA.Keqsuccoascs_na)/((1+u_succoa_m_n/TCA.Km_succoa_scs_n)*(1+u_adp_m_n/TCA.Km_ADPmito_scs_n)*(1+u_pi_m_n/TCA.Km_pi_scs_na)+(1+u_succ_m_n/TCA.Km_succ_scs_n)*(1+u_coa_m_n/TCA.Km_coa_scs_n)*(1+u_atp_m_n/TCA.Km_atpmito_scs_n)))
    f_FUMm_n = 1*(TCA.Vmaxfum_n*(u_fum_m_n-u_mal_L_m_n/TCA.Keqfummito_na)/(1.0+u_fum_m_n/TCA.Km_fummito_n+u_mal_L_m_n/TCA.Km_malmito_n))
    f_MDHm_n = 1*(TCA.VmaxMDHmito_n*(u_mal_L_m_n*u_nad_m_n-u_oaa_m_n*u_nadh_m_n/TCA.Keqmdhmito_na)/((1.0+u_mal_L_m_n/TCA.Km_mal_mdh_n)*(1.0+u_nad_m_n/TCA.Km_nad_mdh_na)+(1.0+u_oaa_m_n/TCA.Km_oxa_mdh_n)*(1.0+u_nadh_m_n/TCA.Km_nadh_mdh_na)))
    f_OCOAT1m_n = (Ketones.VmaxfSCOT_n*u_succoa_m_n*u_acac_c_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n*(u_succoa_m_n/Ketones.Ki_SucCoA_SCOT_n+Ketones.Km_SucCoA_SCOT_n*u_acac_c_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n)+u_aacoa_m_n/Ketones.Ki_AcAcCoA_SCOT_n+Ketones.Km_AcAcCoA_SCOT_n*u_succ_m_n/(Ketones.Ki_AcAcCoA_SCOT_n*Ketones.Km_SUC_SCOT_n)+u_succoa_m_n*u_acac_c_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n)+u_succoa_m_n*u_aacoa_m_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Ki_AcAcCoA_SCOT_n)+Ketones.Km_SucCoA_SCOT_n*u_acac_c_n*u_succ_m_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n*Ketones.Ki_SUC_SCOT_n)+u_aacoa_m_n*u_succ_m_n/(Ketones.Ki_AcAcCoA_SCOT_n*Ketones.Km_SUC_SCOT_n))))-(Ketones.VmaxrSCOT_n*u_aacoa_m_n*u_succ_m_n/(Ketones.Ki_AcAcCoA_SCOT_n*Ketones.Km_SUC_SCOT_n*(u_succoa_m_n/Ketones.Ki_SucCoA_SCOT_n+Ketones.Km_SucCoA_SCOT_n*u_acac_c_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n)+u_aacoa_m_n/Ketones.Ki_AcAcCoA_SCOT_n+Ketones.Km_AcAcCoA_SCOT_n*u_succ_m_n/(Ketones.Ki_AcAcCoA_SCOT_n*Ketones.Km_SUC_SCOT_n)+u_succoa_m_n*u_acac_c_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n)+u_succoa_m_n*u_aacoa_m_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Ki_AcAcCoA_SCOT_n)+Ketones.Km_SucCoA_SCOT_n*u_acac_c_n*u_succ_m_n/(Ketones.Ki_SucCoA_SCOT_n*Ketones.Km_AcAc_SCOT_n*Ketones.Ki_SUC_SCOT_n)+u_aacoa_m_n*u_succ_m_n/(Ketones.Ki_AcAcCoA_SCOT_n*Ketones.Km_SUC_SCOT_n))))
    f_ACACT1rm_n = Ketones.Vmax_thiolase_f_n*u_coa_m_n*u_aacoa_m_n/(Ketones.Ki_CoA_thiolase_f_n*Ketones.Km_AcAcCoA_thiolase_f_n+Ketones.Km_AcAcCoA_thiolase_f_n*u_coa_m_n+Ketones.Km_CoA_thiolase_f_n*u_aacoa_m_n+u_coa_m_n*u_aacoa_m_n)
    f_notBigg_JbHBTrArtCap = (2*(Ketones.C_bHB_a-u_bhb_b_b)/GeneralConstants.eto_b)*p_notBigg_FinDyn_W2017
    f_notBigg_MCT1_bHB_b = Ketones.VmaxMCTbhb_b*(u_bhb_b_b/(u_bhb_b_b+Ketones.KmMCT1_bHB_b)-u_bhb_e_e/(u_bhb_e_e+Ketones.KmMCT1_bHB_b))
    f_BHBt_n = Ketones.VmaxMCTbhb_n*(u_bhb_e_e/(u_bhb_e_e+Ketones.KmMCT2_bHB_n)-u_bhb_c_n/(u_bhb_c_n+Ketones.KmMCT2_bHB_n))
    f_BHBt_a = Ketones.VmaxMCTbhb_a*(u_bhb_e_e/(u_bhb_e_e+Ketones.KmMCT1_bHB_a)-u_bhb_c_a/(u_bhb_c_a+Ketones.KmMCT1_bHB_a))
    f_BDHm_n = Ketones.Vmax_bHBDH_f_n*u_nad_m_n*u_bhb_c_n/(Ketones.Ki_NAD_B_HBD_f_n*Ketones.Km_betaHB_BHBD_n+Ketones.Km_betaHB_BHBD_n*u_nad_m_n+Ketones.Km_NAD_B_HBD_n*u_bhb_c_n+u_nad_m_n*u_bhb_c_n)-(Ketones.Vmax_bHBDH_r_n*u_nadh_m_n*u_acac_c_n/(Ketones.Ki_NADH_BHBD_r_n*Ketones.Km_AcAc_BHBD_n+Ketones.Km_AcAc_BHBD_n*u_nadh_m_n+Ketones.Km_NADH_BHBD_n*u_acac_c_n+u_nadh_m_n*u_acac_c_n))
        
    # BDHm_a(u_bhb_c_a,u_acac_c_a,u_nad_m_a,u_nadh_m_a) = 1*(Ketones.Vmax_bHBDH_f_n*u_nad_m_a*u_bhb_c_a/(Ketones.Ki_NAD_B_HBD_f_n*Ketones.Km_betaHB_BHBD_n+Ketones.Km_betaHB_BHBD_n*u_nad_m_a+Ketones.Km_NAD_B_HBD_n*u_bhb_c_a+u_nad_m_a*u_bhb_c_a)-(Ketones.Vmax_bHBDH_r_n*u_nadh_m_a*u_acac_c_a/(Ketones.Ki_NADH_BHBD_r_n*Ketones.Km_AcAc_BHBD_n+Ketones.Km_AcAc_BHBD_n*u_nadh_m_a+Ketones.Km_NADH_BHBD_n*u_acac_c_a+u_nadh_m_a*u_acac_c_a)))

    f_ASPTAm_n = MAS.VfAAT_n*(u_asp_L_m_n*u_akg_m_n-u_oaa_m_n*u_glu_L_m_n/MAS.KeqAAT_n)/(MAS.KmAKG_AAT_n*u_asp_L_m_n+MAS.KmASP_AAT_n*(1.0+u_akg_m_n/MAS.KiAKG_AAT_n)*u_akg_m_n+u_asp_L_m_n*u_akg_m_n+MAS.KmASP_AAT_n*u_akg_m_n*u_glu_L_m_n/MAS.KiGLU_AAT_n+(MAS.KiASP_AAT_n*MAS.KmAKG_AAT_n/(MAS.KmOXA_AAT_n*MAS.KiGLU_AAT_n))*(MAS.KmGLU_AAT_n*u_asp_L_m_n*u_oaa_m_n/MAS.KiASP_AAT_n+u_oaa_m_n*u_glu_L_m_n+MAS.KmGLU_AAT_n*(1.0+u_akg_m_n/MAS.KiAKG_AAT_n)*u_oaa_m_n+MAS.KmOXA_AAT_n*u_glu_L_m_n))
    f_MDH_n = MAS.VmaxcMDH_n*(u_mal_L_c_n*u_nad_c_n-u_oaa_c_n*u_nadh_c_n/MAS.Keqcmdh_n)/((1+u_mal_L_c_n/MAS.Kmmalcmdh_n)*(1+u_nad_c_n/MAS.Kmnadcmdh_n)+(1+u_oaa_c_n/MAS.Kmoxacmdh_n)*(1+u_nadh_c_n/MAS.Kmnadhcmdh_n)-1)
    f_ASPTA_n = MAS.VfCAAT_n*(u_asp_L_c_n*u_akg_c_n-u_oaa_c_n*u_glu_L_c_n/MAS.KeqCAAT_n)/(MAS.KmAKG_CAAT_n*u_asp_L_c_n+MAS.KmASP_CAAT_n*(1.0+u_akg_c_n/MAS.KiAKG_CAAT_n)*u_akg_c_n+u_asp_L_c_n*u_akg_c_n+MAS.KmASP_CAAT_n*u_akg_c_n*u_glu_L_c_n/MAS.KiGLU_CAAT_n+(MAS.KiASP_CAAT_n*MAS.KmAKG_CAAT_n/(MAS.KmOXA_CAAT_n*MAS.KiGLU_CAAT_n))*(MAS.KmGLU_CAAT_n*u_asp_L_c_n*u_oaa_c_n/MAS.KiASP_CAAT_n+u_oaa_c_n*u_glu_L_c_n+MAS.KmGLU_CAAT_n*(1.0+u_akg_c_n/MAS.KiAKG_CAAT_n)*u_oaa_c_n+MAS.KmOXA_CAAT_n*u_glu_L_c_n))
    f_ASPGLUm_n = MAS.Vmaxagc_n*(u_asp_L_m_n*u_glu_L_c_n-u_asp_L_c_n*u_glu_L_m_n/((np.exp(u_notBigg_MitoMembrPotent_m_n*GeneralConstants.F/(GeneralConstants.R*GeneralConstants.T)))*(u_h_c_n/u_h_m_n)))/((u_asp_L_m_n+MAS.Km_aspmito_agc_n)*(u_glu_L_c_n+MAS.Km_glu_agc_n)+(u_asp_L_c_n+MAS.Km_asp_agc_n)*(u_glu_L_m_n+MAS.Km_glumito_agc_n))
    f_AKGMALtm_n = MAS.Vmaxmakgc_n*(u_mal_L_c_n*u_akg_m_n-u_mal_L_m_n*u_akg_c_n)/((u_mal_L_c_n+MAS.Km_mal_mkgc_n)*(u_akg_m_n+MAS.Km_akgmito_mkgc_n)+(u_mal_L_m_n+MAS.Km_malmito_mkgc_n)*(u_akg_c_n+MAS.Km_akg_mkgc_n))
    f_r0509_a = ETC.x_DH_a*(ETC.r_DH_a*NAD_x_a-(1e-3*u_nadh_m_a))*((1+(1e-3*u_pi_m_a)/ETC.k_Pi1)/(1+(1e-3*u_pi_m_a)/ETC.k_Pi2))
    f_NADH2_u10mi_a = ETC.x_C1*(np.exp(-(dG_C1op_a+4*dG_H_a)/ETC.etcRT)*(1e-3*u_nadh_m_a)*Q_a-NAD_x_a*(1e-3*u_q10h2_m_a))
    f_CYOR_u10mi_a = ETC.x_C3*((1+(1e-3*u_pi_m_a)/ETC.k_Pi3)/(1+(1e-3*u_pi_m_a)/ETC.k_Pi4))*(np.exp(-(dG_C3op_a+4*dG_H_a-2*ETC.etcF*u_notBigg_MitoMembrPotent_m_a)/(2*ETC.etcRT))*Cox_a*(1e-3*u_q10h2_m_a)**0.5-(1e-3*u_focytC_m_a)*Q_a**0.5)
    f_CYOOm2i_a = ETC.x_C4*((1e-3*u_o2_c_a)/((1e-3*u_o2_c_a)+ETC.k_O2))*((1e-3*u_focytC_m_a)/(1e-3*u_notBigg_Ctot_m_a))*(np.exp(-(dG_C4op_a+2*dG_H_a)/(2*ETC.etcRT))*(1e-3*u_focytC_m_a)*((1e-3*u_o2_c_a)**0.25)-Cox_a*np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_a/ETC.etcRT))
    f_ATPS4mi_a = ETC.x_F1_a*(np.exp(-(dG_F1op_a-ETC.n_A*dG_H_a)/ETC.etcRT)*(ETC.K_DD_a/ETC.K_DT_a)*(1e-3*u_notBigg_ADP_mx_m_a)*(1e-3*u_pi_m_a)-(1e-3*u_notBigg_ATP_mx_m_a))
    f_ATPtm_a = ETC.x_ANT_a*(ADP_fi_a/(ADP_fi_a+ATP_fi_a*np.exp(-ETC.etcF*(0.35*u_notBigg_MitoMembrPotent_m_a)/ETC.etcRT))-ADP_fx_a/(ADP_fx_a+ATP_fx_a*np.exp(-ETC.etcF*(-0.65*u_notBigg_MitoMembrPotent_m_a)/ETC.etcRT)))*(ADP_fi_a/(ADP_fi_a+ETC.k_mADP_a))
    f_notBigg_J_Pi1_a = ETC.x_Pi1*((1e-3*u_h_m_a)*H2PIi_a-(1e-3*u_h_i_a)*H2PIx_a)/(H2PIi_a+ETC.k_PiH)
    f_notBigg_J_Hle_a = ETC.x_Hle*u_notBigg_MitoMembrPotent_m_a*((1e-3*u_h_i_a)*np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_a/ETC.etcRT)-(1e-3*u_h_m_a))/(np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_a/ETC.etcRT)-1)
    f_notBigg_J_KH_a = ETC.x_KH*(ETC.K_i*(1e-3*u_h_m_a)-(1e-3*u_k_m_a)*(1e-3*u_h_i_a))
    f_notBigg_J_K_a = ETC.x_K*u_notBigg_MitoMembrPotent_m_a*(ETC.K_i*np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_a/ETC.etcRT)-(1e-3*u_k_m_a))/(np.exp(ETC.etcF*u_notBigg_MitoMembrPotent_m_a/ETC.etcRT)-1)
    f_ADK1m_a = ETC.x_AK*(ETC.K_AK*(1e-3*u_adp_i_a)*(1e-3*u_adp_i_a)-(1e-3*u_amp_i_a)*(1e-3*u_atp_i_a))
    f_notBigg_J_AMP_a = ETC.gamma*ETC.x_A*((1e-3*u_amp_c_a)-(1e-3*u_amp_i_a))
    f_notBigg_J_ADP_a = ETC.gamma*ETC.x_A*((1e-3*u_adp_c_a)-(1e-3*u_adp_i_a))
    f_notBigg_J_ATP_a = ETC.gamma*ETC.x_A*((1e-3*u_atp_c_a)-(1e-3*u_atp_i_a))
    f_notBigg_J_Pi2_a = ETC.gamma*ETC.x_Pi2*(1e-3*u_pi_c_a-(1e-3*u_pi_i_a))
    f_notBigg_J_Ht_a = ETC.gamma*ETC.x_Ht*(1e-3*u_h_c_a-(1e-3*u_h_i_a))
    f_notBigg_J_MgATPx_a = ETC.x_MgA*(ATP_fx_a*(1e-3*u_mg2_m_a)-ETC.K_DT_a*(1e-3*u_notBigg_ATP_mx_m_a))
    f_notBigg_J_MgADPx_a = ETC.x_MgA*(ADP_fx_a*(1e-3*u_mg2_m_a)-ETC.K_DD_a*(1e-3*u_notBigg_ADP_mx_m_a))
    f_notBigg_J_MgATPi_a = ETC.x_MgA*(ATP_fi_a*Mg_i_a-ETC.K_DT_a*(1e-3*u_notBigg_ATP_mi_i_a))
    f_notBigg_J_MgADPi_a = ETC.x_MgA*(ADP_fi_a*Mg_i_a-ETC.K_DD_a*(1e-3*u_notBigg_ADP_mi_i_a))

    f_PDHm_a = TCA.VmaxPDHCmito_a*(u_pyr_m_a/(u_pyr_m_a+TCA.KmPyrMitoPDH_a))*(u_nad_m_a/(u_nad_m_a+TCA.KmNADmitoPDH_na))*(u_coa_m_a/(u_coa_m_a+TCA.KmCoAmitoPDH_a))
    f_CSm_a = TCA.VmaxCSmito_a*(u_oaa_m_a/(u_oaa_m_a+TCA.KmOxaMito_a*(1.0+u_cit_m_a/
    TCA.KiCitMito_a)))*(u_accoa_m_a/(u_accoa_m_a+TCA.KmAcCoAmito_a*(1.0+u_coa_m_a/TCA.KiCoA_a)))
    f_ACONTm_a = TCA.VmaxAco_a*(u_cit_m_a-u_icit_m_a/TCA.KeqAco_na)/(1.0+u_cit_m_a/TCA.KmCitAco_a+u_icit_m_a/TCA.KmIsoCitAco_a)
    f_ICDHxm_a = TCA.VmaxIDH_a*(u_nad_m_a/TCA.KiNADmito_na)*((u_icit_m_a/TCA.KmIsoCitIDHm_a)**TCA.nIDH)/(1.0+u_nad_m_a/TCA.KiNADmito_na+(TCA.KmNADmito_na/TCA.KiNADmito_na)*((u_icit_m_a/TCA.KmIsoCitIDHm_a)**TCA.nIDH)+u_nadh_m_a/TCA.KiNADHmito_na+(u_nad_m_a/TCA.KiNADmito_na)*((u_icit_m_a/TCA.KmIsoCitIDHm_a)**TCA.nIDH)+((TCA.KmNADmito_na*u_nadh_m_a)/(TCA.KiNADmito_na*TCA.KiNADHmito_na))*((u_icit_m_a/TCA.KmIsoCitIDHm_a)**TCA.nIDH))
    f_AKGDm_a = (TCA.VmaxKGDH_a*(1+u_adp_m_a/TCA.KiADPmito_KGDH_a)*(u_akg_m_a/TCA.Km1KGDHKGDH_a)*(u_coa_m_a/TCA.Km_CoA_kgdhKGDH_a)*(u_nad_m_a/TCA.KmNADkgdhKGDH_na))/(((u_coa_m_a/TCA.Km_CoA_kgdhKGDH_a)*(u_nad_m_a/TCA.KmNADkgdhKGDH_na)*(u_akg_m_a/TCA.Km1KGDHKGDH_a+(1+u_atp_m_a/TCA.KiATPmito_KGDH_a)/(1+u_ca2_m_a/TCA.KiCa2KGDH_a)))+((u_akg_m_a/TCA.Km1KGDHKGDH_a)*(u_coa_m_a/TCA.Km_CoA_kgdhKGDH_a+u_nad_m_a/TCA.KmNADkgdhKGDH_na)*(1+u_nadh_m_a/TCA.KiNADHKGDHKGDH_na+u_succoa_m_a/TCA.Ki_SucCoA_kgdhKGDH_a)))
    f_SUCOASm_a = TCA.VmaxSuccoaATPscs_a*(1+TCA.AmaxPscs_a*((u_pi_m_a**TCA.npscs_a)/((u_pi_m_a**TCA.npscs_a)+(TCA.Km_pi_scs_na**TCA.npscs_a))))*(u_succoa_m_a*u_adp_m_a*u_pi_m_a-u_succ_m_a*u_coa_m_a*u_atp_m_a/TCA.Keqsuccoascs_na)/((1+u_succoa_m_a/TCA.Km_succoa_scs_a)*(1+u_adp_m_a/TCA.Km_ADPmito_scs_a)*(1+u_pi_m_a/TCA.Km_pi_scs_na)+(1+u_succ_m_a/TCA.Km_succ_scs_a)*(1+u_coa_m_a/TCA.Km_coa_scs_a)*(1+u_atp_m_a/TCA.Km_atpmito_scs_a))
    f_FUMm_a = TCA.Vmaxfum_a*(u_fum_m_a-u_mal_L_m_a/TCA.Keqfummito_na)/(1.0+u_fum_m_a/TCA.Km_fummito_a+u_mal_L_m_a/TCA.Km_malmito_a)
    f_MDHm_a = TCA.VmaxMDHmito_a*(u_mal_L_m_a*u_nad_m_a-u_oaa_m_a*u_nadh_m_a/TCA.Keqmdhmito_na)/((1.0+u_mal_L_m_a/TCA.Km_mal_mdh_a)*(1.0+u_nad_m_a/TCA.Km_nad_mdh_na)+(1.0+u_oaa_m_a/TCA.Km_oxa_mdh_a)*(1.0+u_nadh_m_a/TCA.Km_nadh_mdh_na))
    
    f_PCm_a = ((u_atp_m_a/u_adp_m_a)/(PyrCarb.muPYRCARB_a+(u_atp_m_a/u_adp_m_a)))*PyrCarb.VmPYRCARB_a*(u_pyr_m_a*u_co2_m_a-u_oaa_m_a/PyrCarb.KeqPYRCARB_a)/(PyrCarb.KmPYR_PYRCARB_a*PyrCarb.KmCO2_PYRCARB_a+PyrCarb.KmPYR_PYRCARB_a*u_co2_m_a+PyrCarb.KmCO2_PYRCARB_a*u_pyr_m_a+u_co2_m_a*u_pyr_m_a)

    f_GLNt4_n = Gltgln.TmaxSNAT_GLN_n*(u_gln_L_e_e-u_gln_L_c_n/Gltgln.coeff_gln_ratio_n_ecs)/(Gltgln.KmSNAT_GLN_n+u_gln_L_c_n)
    f_GLUNm_n = Gltgln.VmGLS_n*(u_gln_L_c_n-u_glu_L_m_n/Gltgln.KeqGLS_n)/(Gltgln.KmGLNGLS_n*(1.0+u_glu_L_m_n/Gltgln.KiGLUGLS_n)+u_gln_L_c_n)


    GLUt6_a_multi = Gltgln.alpha_EAAT/(2*GeneralConstants.F*1e-3)
    GLUt6_a_log_arg = ((Gltgln.Na_syn_EAAT/u_na1_c_a)**3)*(Gltgln.H_syn_EAAT/Gltgln.H_ast_EAAT)*(u_glu_L_syn_syn/u_glu_L_c_a)*(u_k_c_a/u_k_e_e)
    GLUt6_a_log_multi = (GeneralConstants.R*GeneralConstants.T/(2*GeneralConstants.F*1e-3))
    f_GLUt6_a = GLUt6_a_multi*np.exp(-Gltgln.beta_EAAT*(u_notBigg_Va_c_a-GLUt6_a_log_multi*np.log(GLUt6_a_log_arg)))



    f_GLUDxm_a = Gltgln.VmGDH_a*(u_nad_m_a*u_glu_L_c_a-u_nadh_m_a*u_akg_m_a/Gltgln.KeqGDH_a)/(Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a+Gltgln.KmGLU_GDH_a*u_nad_m_a+Gltgln.KiNAD_GDH_a*u_glu_L_c_a+u_glu_L_c_a*u_nad_m_a+u_glu_L_c_a*u_nad_m_a/Gltgln.KiAKG_GDH_a+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*u_nadh_m_a/Gltgln.KiNADH_GDH_a+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*Gltgln.KmNADH_GDH_a*u_akg_m_a/(Gltgln.KiAKG_GDH_a*Gltgln.KiNADH_GDH_a)+Gltgln.KmNADH_GDH_a*u_glu_L_c_a*u_nadh_m_a/Gltgln.KiNADH_GDH_a+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*Gltgln.KmAKG_GDH_a*u_nadh_m_a/(Gltgln.KiAKG_GDH_a*Gltgln.KiNADH_GDH_a)+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*Gltgln.KmAKG_GDH_a*u_akg_m_a*u_nadh_m_a/(Gltgln.KiAKG_GDH_a*Gltgln.KiNADH_GDH_a)+u_glu_L_c_a*u_nad_m_a*u_akg_m_a/Gltgln.KiAKG_GDH_a+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*Gltgln.KmAKG_GDH_a/Gltgln.KiAKG_GDH_a+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*u_glu_L_c_a*u_nadh_m_a*u_akg_m_a/(Gltgln.KiGLU_GDH_a*Gltgln.KiAKG_GDH_a*Gltgln.KiNADH_GDH_a)+Gltgln.KiNAD_GDH_a*Gltgln.KmGLU_GDH_a*u_akg_m_a*u_nadh_m_a/(Gltgln.KiAKG_GDH_a*Gltgln.KiNADH_GDH_a)+Gltgln.KmNADH_GDH_a*Gltgln.KmGLU_GDH_a*u_akg_m_a*u_nad_m_a/(Gltgln.KiAKG_GDH_a*Gltgln.KiNADH_GDH_a))
    f_GLNS_a = Gltgln.VmaxGLNsynth_a*(u_glu_L_c_a/(Gltgln.KmGLNsynth_a+u_glu_L_c_a))*((1/(u_atp_c_a/u_adp_c_a))/(Gltgln.muGLNsynth_a+(1/(u_atp_c_a/u_adp_c_a))))
    f_GLNt4_a = Gltgln.TmaxSNAT_GLN_a*(u_gln_L_c_a-u_gln_L_e_e)/(Gltgln.KmSNAT_GLN_a+u_gln_L_c_a)
        
    f_notBigg_JdHbin = 2*(BfInput.C_O_a-u_o2_b_b)*p_notBigg_FinDyn_W2017

    # notBigg_JdHbout(t,u_notBigg_ddHb_b_b,u_notBigg_vV_b_b) = (u_notBigg_ddHb_b_b/u_notBigg_vV_b_b)*(global_par_F_0*((u_notBigg_vV_b_b/u0_ss[111])**2+(u_notBigg_vV_b_b/u0_ss[111])**(-0.5)*global_par_tau_v/u0_ss[111]*notBigg_FinDyn_W2017)/(1+global_par_F_0*(u_notBigg_vV_b_b/u0_ss[111])**(-0.5)*global_par_tau_v/u0_ss[111]))

    f_notBigg_JdHbout = (u_notBigg_ddHb_b_b/p_notBigg_vV_b_b)*p_notBigg_Fout_W2017  
    f_notBigg_JO2art2cap = (1/GeneralConstants.eto_b)*2*(BfInput.C_O_a-u_o2_b_b)*p_notBigg_FinDyn_W2017
        
    f_notBigg_JO2fromCap2a = BfInput.PScapA*(BfInput.KO2b*(BfInput.HbOP/u_o2_b_b-1.)**(-1/BfInput.param_degree_nh)-u_o2_c_a)
    f_notBigg_JO2fromCap2n = BfInput.PScapNAratio*BfInput.PScapA*(BfInput.KO2b*(BfInput.HbOP/u_o2_b_b-1.)**(-1/BfInput.param_degree_nh)-u_o2_c_n)
        
    f_notBigg_trGLC_art_cap = (1/GeneralConstants.eto_b)*(2*(GLCtransport.C_Glc_a-u_glc_D_b_b))*p_notBigg_FinDyn_W2017

    f_notBigg_JGlc_be = GLCtransport.TmaxGLCce*(u_glc_D_b_b*(GLCtransport.KeG+u_glc_D_ecsEndothelium_ecsEndothelium)-u_glc_D_ecsEndothelium_ecsEndothelium*(GLCtransport.KeG+u_glc_D_b_b))/(GLCtransport.KeG**2+GLCtransport.KeG*GLCtransport.ReGoi*u_glc_D_b_b+GLCtransport.KeG*GLCtransport.ReGio*u_glc_D_ecsEndothelium_ecsEndothelium+GLCtransport.ReGee*u_glc_D_b_b*u_glc_D_ecsEndothelium_ecsEndothelium)

    f_notBigg_JGlc_e2ecsBA = GLCtransport.TmaxGLCeb*(u_glc_D_ecsEndothelium_ecsEndothelium*(GLCtransport.KeG2+u_glc_D_ecsBA_ecsBA)-u_glc_D_ecsBA_ecsBA*(GLCtransport.KeG2+u_glc_D_ecsEndothelium_ecsEndothelium))/(GLCtransport.KeG2**2+GLCtransport.KeG2*GLCtransport.ReGoi2*u_glc_D_ecsEndothelium_ecsEndothelium+GLCtransport.KeG2*GLCtransport.ReGio2*u_glc_D_ecsBA_ecsBA+GLCtransport.ReGee2*u_glc_D_ecsEndothelium_ecsEndothelium*u_glc_D_ecsBA_ecsBA)

    f_notBigg_JGlc_ecsBA2a = GLCtransport.TmaxGLCba*(u_glc_D_ecsBA_ecsBA*(GLCtransport.KeG3+u_glc_D_c_a)-u_glc_D_c_a*(GLCtransport.KeG3+u_glc_D_ecsBA_ecsBA))/(GLCtransport.KeG3**2+GLCtransport.KeG3*GLCtransport.ReGoi3*u_glc_D_ecsBA_ecsBA+GLCtransport.KeG3*GLCtransport.ReGio3*u_glc_D_c_a+GLCtransport.ReGee3*u_glc_D_ecsBA_ecsBA*u_glc_D_c_a)

    f_notBigg_JGlc_a2ecsAN = GLCtransport.TmaxGLCai*(u_glc_D_c_a*(GLCtransport.KeG4+u_glc_D_ecsAN_ecsAN)-u_glc_D_ecsAN_ecsAN*(GLCtransport.KeG4+u_glc_D_c_a))/(GLCtransport.KeG4**2+GLCtransport.KeG4*GLCtransport.ReGoi4*u_glc_D_c_a+GLCtransport.KeG4*GLCtransport.ReGio4*u_glc_D_ecsAN_ecsAN+GLCtransport.ReGee4*u_glc_D_c_a*u_glc_D_ecsAN_ecsAN)

    f_notBigg_JGlc_ecsAN2n = GLCtransport.TmaxGLCin*(u_glc_D_ecsAN_ecsAN*(GLCtransport.KeG5+u_glc_D_c_n)-u_glc_D_c_n*(GLCtransport.KeG5+u_glc_D_ecsAN_ecsAN))/(GLCtransport.KeG5**2+GLCtransport.KeG5*GLCtransport.ReGoi5*u_glc_D_ecsAN_ecsAN+GLCtransport.KeG5*GLCtransport.ReGio5*u_glc_D_c_n+GLCtransport.ReGee5*u_glc_D_ecsAN_ecsAN*u_glc_D_c_n)

    f_notBigg_JGlc_diffEcs = GLCtransport.kGLCdiff*(u_glc_D_ecsBA_ecsBA-u_glc_D_ecsAN_ecsAN)

    f_GLCS2_a = Glycogen.kL2_GS_a*u_notBigg_GS_c_a*u_udpg_c_a/(Glycogen.kmL2_GS_a+u_udpg_c_a)

    f_GLCP_a = (u_notBigg_GPa_c_a/(u_notBigg_GPa_c_a+u_notBigg_GPb_c_a))*Glycogen.VmaxGP_a*u_glycogen_c_a*(1/(1+(Glycogen.KmGP_AMP_a**Glycogen.hGPa)/(u_camp_c_a**Glycogen.hGPa)))

    f_PGMT_a = (Glycogen.Vmaxfpglm_a*u_g1p_c_a/Glycogen.KmG1PPGLM_a-((Glycogen.Vmaxfpglm_a*Glycogen.KmG6PPGLM_a)/(Glycogen.KmG1PPGLM_a*Glycogen.KeqPGLM_a))*u_g6p_c_a/Glycogen.KmG6PPGLM_a)/(1.0+u_g1p_c_a/Glycogen.KmG1PPGLM_a+u_g6p_c_a/Glycogen.KmG6PPGLM_a)

    f_PDE1_a = Glycogen.VmaxPDE_a*u_camp_c_a/(Glycogen.Kmcamppde_a+u_camp_c_a)

    f_GALUi_a = (Glycogen.VmaxfUDPGP*u_utp_c_a*u_g1p_c_a/(Glycogen.KutpUDPGP*Glycogen.Kg1pUDPGP)-Glycogen.VmaxrUDPGP*u_ppi_c_a*u_udpg_c_a/(Glycogen.KpiUDPGP*Glycogen.KUDPglucoUDPGP_a))/(1.0+u_g1p_c_a/Glycogen.Kg1pUDPGP+u_utp_c_a/Glycogen.KutpUDPGP+(u_g1p_c_a*u_utp_c_a)/(Glycogen.Kg1pUDPGP*Glycogen.KutpUDPGP)+u_udpg_c_a/Glycogen.KUDPglucoUDPGP_a+u_ppi_c_a/Glycogen.KpiUDPGP+(u_ppi_c_a*u_udpg_c_a)/(Glycogen.KpiUDPGP*Glycogen.KUDPglucoUDPGP_a))

    # f_notBigg_psiGSAJay_a = ((Glycogen.kg8_GSAJay*GeneralConstants.PP1_a0*(Glycogen.st_GSAJay-u_notBigg_GS_c_a))/((Glycogen.kmg8_GSAJay/(1.0+Glycogen.s1_GSAJay*u_udpg_c_a/Glycogen.kg2_GSAJay))+(Glycogen.st_GSAJay-u_notBigg_GS_c_a)))-((Glycogen.kg7_GSAJay*(u_notBigg_PHKa_c_a+u_notBigg_PKAa_c_a)*u_notBigg_GS_c_a)/(Glycogen.kmg7_GSAJay*(1+Glycogen.s1_GSAJay*u_udpg_c_a/Glycogen.kg2_GSAJay)+u_notBigg_GS_c_a))

    f_notBigg_psiPHK_a = (u_ca2_c_a/Glycogen.cai0_ca_ion)*(((Glycogen.kg5_PHK*u_notBigg_PHKa_c_a*(Glycogen.pt_PHK-u_notBigg_GPa_c_a))/(Glycogen.kmg5_PHK*(1.0+Glycogen.s1_PHK*u_g1p_c_a/Glycogen.kg2_PHK)+(Glycogen.pt_PHK-u_notBigg_GPa_c_a)))-((Glycogen.kg6_PHK*GeneralConstants.PP1_a0*u_notBigg_GPa_c_a)/(Glycogen.kmg6_PHK/(1+Glycogen.s2_PHK*u_udpg_c_a/Glycogen.kgi_PHK)+u_notBigg_GPa_c_a))-((0.003198/(1+u_glycogen_c_a)+Glycogen.kmind_PHK)*GeneralConstants.PP1_a0*u_notBigg_GPa_c_a))
    
    f_HEX1_n = (Glycolysis.VmaxHK_n*u_glc_D_c_n/(u_glc_D_c_n+Glycolysis.KmHK_n))*(u_atp_c_n/(1+(u_atp_c_n/Glycolysis.KIATPhex_n)**Glycolysis.nHhexn))*(1/(1+u_g6p_c_n/Glycolysis.KiHKG6P_n))
    f_HEX1_a = (Glycolysis.VmaxHK_a*u_glc_D_c_a/(u_glc_D_c_a+Glycolysis.KmHK_a))*(u_atp_c_a/(1+(u_atp_c_a/Glycolysis.KIATPhex_a)**Glycolysis.nHhexa))*(1/(1+u_g6p_c_a/Glycolysis.KiHKG6P_a))
    f_PGI_n = (Glycolysis.Vmax_fPGI_n*(u_g6p_c_n/Glycolysis.Km_G6P_fPGI_n-0.9*u_f6p_c_n/Glycolysis.Km_F6P_rPGI_n))/(1.0+u_g6p_c_n/Glycolysis.Km_G6P_fPGI_n+u_f6p_c_n/Glycolysis.Km_F6P_rPGI_n)
    f_PGI_a = (Glycolysis.Vmax_fPGI_a*(u_g6p_c_a/Glycolysis.Km_G6P_fPGI_a-0.9*u_f6p_c_a/Glycolysis.Km_F6P_rPGI_a))/(1.0+u_g6p_c_a/Glycolysis.Km_G6P_fPGI_a+u_f6p_c_a/Glycolysis.Km_F6P_rPGI_a)
    f_PFK_n = Glycolysis.VmaxPFK_n*(u_atp_c_n/(1+(u_atp_c_n/Glycolysis.KiPFK_ATP_na)**Glycolysis.nPFKn))*(u_f6p_c_n/(u_f6p_c_n+Glycolysis.KmPFKF6P_n))
    f_PFK_a = Glycolysis.VmaxPFK_a*(u_atp_c_a/(1+(u_atp_c_a/Glycolysis.KiPFK_ATP_a)**Glycolysis.nPFKa))*(u_f6p_c_a/(u_f6p_c_a+Glycolysis.KmPFKF6P_a*(1-Glycolysis.KoPFK_f26bp_a*((u_f26bp_c_a**Glycolysis.nPFKf26bp_a)/(Glycolysis.KmF26BP_PFK_a**Glycolysis.nPFKf26bp_a+u_f26bp_c_a**Glycolysis.nPFKf26bp_a)))))*(u_f26bp_c_a/(Glycolysis.KmF26BP_PFK_a+u_f26bp_c_a))
    f_PFK26_a = Glycolysis.Vmax_PFKII_g*u_f6p_c_a*u_atp_c_a*u_adp_c_a/((u_f6p_c_a+Glycolysis.Kmf6pPFKII_g)*(u_atp_c_a+Glycolysis.KmatpPFKII_g)*(u_adp_c_a+Glycolysis.Km_act_adpPFKII_g))-(Glycolysis.Vmax_PFKII_g*u_f26bp_c_a/(u_f26bp_c_a+Glycolysis.Km_f26bp_f_26pase_g*(1+u_f6p_c_a/Glycolysis.Ki_f6p_f_26_pase_g)))
    f_FBA_n = Glycolysis.Vmaxald_n*(u_fdp_c_n-u_g3p_c_n*u_dhap_c_n/Glycolysis.Keqald_n)/((1+u_fdp_c_n/Glycolysis.KmfbpAld_n)+(1+u_g3p_c_n/Glycolysis.KmgapAld_n)*(1+u_dhap_c_n/Glycolysis.KmdhapAld_n)-1)
    f_FBA_a = Glycolysis.Vmaxald_a*(u_fdp_c_a-u_g3p_c_a*u_dhap_c_a/Glycolysis.Keqald_a)/((1+u_fdp_c_a/Glycolysis.KmfbpAld_a)+(1+u_g3p_c_a/Glycolysis.KmgapAld_a)*(1+u_dhap_c_a/Glycolysis.KmdhapAld_a)-1)
    f_TPI_n = Glycolysis.Vmaxtpi_n*(u_dhap_c_n-u_g3p_c_n/Glycolysis.Keqtpi_n)/(1+u_dhap_c_n/Glycolysis.KmdhapTPI_n+u_g3p_c_n/Glycolysis.KmgapTPI_n)
    f_TPI_a = Glycolysis.Vmaxtpi_a*(u_dhap_c_a-u_g3p_c_a/Glycolysis.Keqtpi_a)/(1+u_dhap_c_a/Glycolysis.KmdhapTPI_a+u_g3p_c_a/Glycolysis.KmgapTPI_a)
    f_GAPD_n = Glycolysis.Vmaxgapdh_n*(u_nad_c_n*u_g3p_c_n*u_pi_c_n-u_n13dpg_c_n*u_nadh_c_n/Glycolysis.Keqgapdh_na)/((1+u_nad_c_n/Glycolysis.KmnadGpdh_n)*(1+u_g3p_c_n/Glycolysis.KmGapGapdh_n)*(1+u_pi_c_n/Glycolysis.KmpiGpdh_n)+(1+u_nadh_c_n/Glycolysis.KmnadhGapdh_n)*(1+u_n13dpg_c_n/Glycolysis.KmBPG13Gapdh_n)-1)

    f_GAPD_a = Glycolysis.Vmaxgapdh_a*(u_nad_c_a*u_g3p_c_a*u_pi_c_a-u_n13dpg_c_a*u_nadh_c_a/Glycolysis.Keqgapdh_na)/((1+u_nad_c_a/Glycolysis.KmnadGpdh_a)*(1+u_g3p_c_a/Glycolysis.KmGapGapdh_a)*(1+u_pi_c_a/Glycolysis.KmpiGpdh_a)+(1+u_nadh_c_a/Glycolysis.KmnadhGapdh_a)*(1+u_n13dpg_c_a/Glycolysis.KmBPG13Gapdh_a)-1)
    f_PGK_n = Glycolysis.Vmaxpgk_n*(u_n13dpg_c_n*u_adp_c_n-u_n3pg_c_n*u_atp_c_n/Glycolysis.Keqpgk_na)/((1+u_n13dpg_c_n/Glycolysis.Kmbpg13pgk_n)*(1+u_adp_c_n/Glycolysis.Kmadppgk_n)+(1+u_n3pg_c_n/Glycolysis.Kmpg3pgk_n)*(1+u_atp_c_n/Glycolysis.Kmatppgk_n)-1)
    f_PGK_a = Glycolysis.Vmaxpgk_a*(u_n13dpg_c_a*u_adp_c_a-u_n3pg_c_a*u_atp_c_a/Glycolysis.Keqpgk_na)/((1+u_n13dpg_c_a/Glycolysis.Kmbpg13pgk_a)*(1+u_adp_c_a/Glycolysis.Kmadppgk_a)+(1+u_n3pg_c_a/Glycolysis.Kmpg3pgk_a)*(1+u_atp_c_a/Glycolysis.Kmatppgk_a)-1)
    f_PGM_n = Glycolysis.Vmaxpgm_n*(u_n3pg_c_n-u_n2pg_c_n/Glycolysis.Keqpgm_n)/((1+u_n3pg_c_n/Glycolysis.Kmpg3pgm_n)+(1+u_n2pg_c_n/Glycolysis.Kmpg2pgm_n)-1)
    f_PGM_a = Glycolysis.Vmaxpgm_a*(u_n3pg_c_a-u_n2pg_c_a/Glycolysis.Keqpgm_a)/((1+u_n3pg_c_a/Glycolysis.Kmpg3pgm_a)+(1+u_n2pg_c_a/Glycolysis.Kmpg2pgm_a)-1)
    f_ENO_n = Glycolysis.Vmaxenol_n*(u_n2pg_c_n-u_pep_c_n/Glycolysis.Keqenol_n)/((1+u_n2pg_c_n/Glycolysis.Kmpg2enol_n)+(1+u_pep_c_n/Glycolysis.Km_pep_enol_n)-1)
    f_ENO_a = Glycolysis.Vmaxenol_a*(u_n2pg_c_a-u_pep_c_a/Glycolysis.Keqenol_a)/((1+u_n2pg_c_a/Glycolysis.Kmpg2enol_a)+(1+u_pep_c_a/Glycolysis.Km_pep_enol_a)-1)
    f_PYK_n = Glycolysis.Vmaxpk_n*u_pep_c_n*u_adp_c_n/((u_pep_c_n+Glycolysis.Km_pep_pk_n)*(u_adp_c_n+Glycolysis.Km_adp_pk_n*(1+u_atp_c_n/Glycolysis.Ki_ATP_pk_n)))
    f_PYK_a = Glycolysis.Vmaxpk_a*u_pep_c_a*u_adp_c_a/((u_pep_c_a+Glycolysis.Km_pep_pk_a)*(u_adp_c_a+Glycolysis.Km_adp_pk_a*(1+u_atp_c_a/Glycolysis.Ki_ATP_pk_a)))

    f_notBigg_JLacTr_b = (2*(Lactate.C_Lac_a-u_lac_L_b_b)/GeneralConstants.eto_b)*p_notBigg_FinDyn_W2017

    f_notBigg_MCT1_LAC_b = Lactate.TbLac*(u_lac_L_b_b/(u_lac_L_b_b+Lactate.KbLac)-u_lac_L_e_e/(u_lac_L_e_e+Lactate.KbLac))
    f_L_LACt2r_a = Lactate.TaLac*(u_lac_L_e_e/(u_lac_L_e_e+Lactate.Km_Lac_a)-u_lac_L_c_a/(u_lac_L_c_a+Lactate.Km_Lac_a))
    f_L_LACt2r_n = Lactate.TnLac*(u_lac_L_e_e/(u_lac_L_e_e+Lactate.Km_LacTr_n)-u_lac_L_c_n/(u_lac_L_c_n+Lactate.Km_LacTr_n))
    f_notBigg_jLacDiff_e = 0 # betaLacDiff*(u0_ss[150]-u_lac_L_e_e))
        
    f_notBigg_vLACgc = Lactate.TMaxLACgc*(u_lac_L_b_b/(u_lac_L_b_b+Lactate.KtLACgc)-u_lac_L_c_a/(u_lac_L_c_a+Lactate.KtLACgc))
    f_LDH_L_a = Lactate.VmfLDH_a*u_pyr_c_a*u_nadh_c_a-Lactate.KeLDH_a*Lactate.VmfLDH_a*u_lac_L_c_a*u_nad_c_a
    f_LDH_L_n = Lactate.VmfLDH_n*u_pyr_c_n*u_nadh_c_n-Lactate.KeLDH_n*Lactate.VmfLDH_n*u_lac_L_c_n*u_nad_c_n

    f_G6PDH2r_n = PPP_n.VmaxG6PDH_n*(1/(PPP_n.K_G6P_G6PDH_n*PPP_n.K_NADP_G6PDH_n))*((u_g6p_c_n*u_nadp_c_n-u_n6pgl_c_n*u_nadph_c_n/PPP_n.KeqG6PDH_n)/((1+u_g6p_c_n/PPP_n.K_G6P_G6PDH_n)*(1+u_nadp_c_n/PPP_n.K_NADP_G6PDH_n)+(1+u_n6pgl_c_n/PPP_n.K_GL6P_G6PDH_n)*(1+u_nadph_c_n/PPP_n.K_NADPH_G6PDH_n)-1))
    f_G6PDH2r_a = PPP_a.VmaxG6PDH_a*(1/(PPP_a.K_G6P_G6PDH_a*PPP_a.K_NADP_G6PDH_a))*((u_g6p_c_a*u_nadp_c_a-u_n6pgl_c_a*u_nadph_c_a/PPP_a.KeqG6PDH_a)/((1+u_g6p_c_a/PPP_a.K_G6P_G6PDH_a)*(1+u_nadp_c_a/PPP_a.K_NADP_G6PDH_a)+(1+u_n6pgl_c_a/PPP_a.K_GL6P_G6PDH_a)*(1+u_nadph_c_a/PPP_a.K_NADPH_G6PDH_a)-1))
    f_PGL_n = PPP_n.Vmax6PGL_n*(1/PPP_n.K_GL6P_6PGL_n)*((u_n6pgl_c_n-u_n6pgc_c_n/PPP_n.Keq6PGL_n)/((1+u_n6pgl_c_n/PPP_n.K_GL6P_6PGL_n)+(1+u_n6pgc_c_n/PPP_n.K_GO6P_6PGL_n)-1))
    f_PGL_a = PPP_a.Vmax6PGL_a*(1/PPP_a.K_GL6P_6PGL_a)*((u_n6pgl_c_a-u_n6pgc_c_a/PPP_a.Keq6PGL_a)/((1+u_n6pgl_c_a/PPP_a.K_GL6P_6PGL_a)+(1+u_n6pgc_c_a/PPP_a.K_GO6P_6PGL_a)-1))
    f_GND_n = PPP_n.Vmax6PGDH_n*(1/(PPP_n.K_GO6P_6PGDH_n*PPP_n.K_NADP_6PGDH_n))*(u_n6pgc_c_n*u_nadp_c_n-u_ru5p_D_c_n*u_nadph_c_n/PPP_n.Keq6PGDH_n)/((1+u_n6pgc_c_n/PPP_n.K_GO6P_6PGDH_n)*(1+u_nadp_c_n/PPP_n.K_NADP_6PGDH_n)+(1+u_ru5p_D_c_n/PPP_n.K_RU5P_6PGDH_n)*(1+u_nadph_c_n/PPP_n.K_NADPH_6PGDH_n)-1)
    f_GND_a = PPP_a.Vmax6PGDH_a*(1/(PPP_a.K_GO6P_6PGDH_a*PPP_a.K_NADP_6PGDH_a))*(u_n6pgc_c_a*u_nadp_c_a-u_ru5p_D_c_a*u_nadph_c_a/PPP_a.Keq6PGDH_a)/((1+u_n6pgc_c_a/PPP_a.K_GO6P_6PGDH_a)*(1+u_nadp_c_a/PPP_a.K_NADP_6PGDH_a)+(1+u_ru5p_D_c_a/PPP_a.K_RU5P_6PGDH_a)*(1+u_nadph_c_a/PPP_a.K_NADPH_6PGDH_a)-1)
    f_RPI_n = PPP_n.VmaxRPI_n*(1/PPP_n.K_RU5P_RPI_n)*(u_ru5p_D_c_n-u_r5p_c_n/PPP_n.KeqRPI_n)/((1+u_ru5p_D_c_n/PPP_n.K_RU5P_RPI_n)+(1+u_r5p_c_n/PPP_n.K_R5P_RPI_n)-1)
    f_RPI_a = PPP_a.VmaxRPI_a*(1/PPP_a.K_RU5P_RPI_a)*(u_ru5p_D_c_a-u_r5p_c_a/PPP_a.KeqRPI_a)/((1+u_ru5p_D_c_a/PPP_a.K_RU5P_RPI_a)+(1+u_r5p_c_a/PPP_a.K_R5P_RPI_a)-1)
    f_RPE_n = PPP_n.VmaxRPE_n*(1/PPP_n.K_RU5P_RPE_n)*(u_ru5p_D_c_n-u_xu5p_D_c_n/PPP_n.KeqRPE_n)/((1+u_ru5p_D_c_n/PPP_n.K_RU5P_RPE_n)+(1+u_xu5p_D_c_n/PPP_n.K_X5P_RPE_n)-1)
    f_RPE_a = PPP_a.VmaxRPE_a*(1/PPP_a.K_RU5P_RPE_a)*(u_ru5p_D_c_a-u_xu5p_D_c_a/PPP_a.KeqRPE_a)/((1+u_ru5p_D_c_a/PPP_a.K_RU5P_RPE_a)+(1+u_xu5p_D_c_a/PPP_a.K_X5P_RPE_a)-1)
    f_TKT1_n = PPP_n.VmaxTKL1_n*(1/(PPP_n.K_X5P_TKL1_n*PPP_n.K_R5P_TKL1_n))*(u_xu5p_D_c_n*u_r5p_c_n-u_g3p_c_n*u_s7p_c_n/PPP_n.KeqTKL1_n)/((1+u_xu5p_D_c_n/PPP_n.K_X5P_TKL1_n)*(1+u_r5p_c_n/PPP_n.K_R5P_TKL1_n)+(1+u_g3p_c_n/PPP_n.K_GAP_TKL1_n)*(1+u_s7p_c_n/PPP_n.K_S7P_TKL1_n)-1)
    f_TKT1_a = PPP_a.VmaxTKL1_a*(1/(PPP_a.K_X5P_TKL1_a*PPP_a.K_R5P_TKL1_a))*(u_xu5p_D_c_a*u_r5p_c_a-u_g3p_c_a*u_s7p_c_a/PPP_a.KeqTKL1_a)/((1+u_xu5p_D_c_a/PPP_a.K_X5P_TKL1_a)*(1+u_r5p_c_a/PPP_a.K_R5P_TKL1_a)+(1+u_g3p_c_a/PPP_a.K_GAP_TKL1_a)*(1+u_s7p_c_a/PPP_a.K_S7P_TKL1_a)-1)
    f_TKT2_n = PPP_n.VmaxTKL2_n*(1/(PPP_n.K_F6P_TKL2_n*PPP_n.K_GAP_TKL2_n))*(u_f6p_c_n*u_g3p_c_n-u_xu5p_D_c_n*u_e4p_c_n/PPP_n.KeqTKL2_n)/((1+u_f6p_c_n/PPP_n.K_F6P_TKL2_n)*(1+u_g3p_c_n/PPP_n.K_GAP_TKL2_n)+(1+u_xu5p_D_c_n/PPP_n.K_X5P_TKL2_n)*(1+u_e4p_c_n/PPP_n.K_E4P_TKL2_n)-1)
    f_TKT2_a = PPP_a.VmaxTKL2_a*(1/(PPP_a.K_F6P_TKL2_a*PPP_a.K_GAP_TKL2_a))*(u_f6p_c_a*u_g3p_c_a-u_xu5p_D_c_a*u_e4p_c_a/PPP_a.KeqTKL2_a)/((1+u_f6p_c_a/PPP_a.K_F6P_TKL2_a)*(1+u_g3p_c_a/PPP_a.K_GAP_TKL2_a)+(1+u_xu5p_D_c_a/PPP_a.K_X5P_TKL2_a)*(1+u_e4p_c_a/PPP_a.K_E4P_TKL2_a)-1)
    f_TALA_n = PPP_n.VmaxTAL_n*(1/(PPP_n.K_GAP_TAL_n*PPP_n.K_S7P_TAL_n))*(u_g3p_c_n*u_s7p_c_n-u_f6p_c_n*u_e4p_c_n/PPP_n.KeqTAL_n)/((1+u_g3p_c_n/PPP_n.K_GAP_TAL_n)*(1+u_s7p_c_n/PPP_n.K_S7P_TAL_n)+(1+u_f6p_c_n/PPP_n.K_F6P_TAL_n)*(1+u_e4p_c_n/PPP_n.K_E4P_TAL_n)-1)
    f_TALA_a = PPP_a.VmaxTAL_a*(1/(PPP_a.K_GAP_TAL_a*PPP_a.K_S7P_TAL_a))*(u_g3p_c_a*u_s7p_c_a-u_f6p_c_a*u_e4p_c_a/PPP_a.KeqTAL_a)/((1+u_g3p_c_a/PPP_a.K_GAP_TAL_a)*(1+u_s7p_c_a/PPP_a.K_S7P_TAL_a)+(1+u_f6p_c_a/PPP_a.K_F6P_TAL_a)*(1+u_e4p_c_a/PPP_a.K_E4P_TAL_a)-1)
    f_notBigg_psiNADPHox_n = PPP_n.k1NADPHox_n*u_nadph_c_n
    f_notBigg_psiNADPHox_a = PPP_a.k1NADPHox_a*u_nadph_c_a

    f_GTHO_n = (Gshgssg.Vmf_GSSGR_n*u_gthox_c_n*u_nadph_c_n)/((Gshgssg.KmGSSGRGSSG_n+u_gthox_c_n)*(Gshgssg.KmGSSGRNADPH_n+u_nadph_c_n))
    f_GTHO_a = (Gshgssg.Vmf_GSSGR_a*u_gthox_c_a*u_nadph_c_a)/((Gshgssg.KmGSSGRGSSG_a+u_gthox_c_a)*(Gshgssg.KmGSSGRNADPH_a+u_nadph_c_a))
    f_GTHP_n = Gshgssg.V_GPX_n*u_gthrd_c_n/(u_gthrd_c_n+Gshgssg.KmGPXGSH_n)
    f_GTHP_a = Gshgssg.V_GPX_a*u_gthrd_c_a/(u_gthrd_c_a+Gshgssg.KmGPXGSH_a)
    f_GTHS_n = Gshgssg.VmaxGSHsyn_n*(Gshgssg.glycine_n*Gshgssg.glutamylCys_n-u_gthrd_c_n/Gshgssg.KeGSHSyn_n)/(Gshgssg.Km_glutamylCys_GSHsyn_n*Gshgssg.Km_glycine_GSHsyn_n+Gshgssg.glutamylCys_n*Gshgssg.Km_glutamylCys_GSHsyn_n+Gshgssg.glycine_n*Gshgssg.Km_glycine_GSHsyn_n*(1+Gshgssg.glutamylCys_n/Gshgssg.Km_glutamylCys_GSHsyn_n)+u_gthrd_c_n/Gshgssg.KmGSHsyn_n)
    f_GTHS_a = Gshgssg.VmaxGSHsyn_a*(Gshgssg.glycine_a*Gshgssg.glutamylCys_a-u_gthrd_c_a/Gshgssg.KeGSHSyn_a)/(Gshgssg.Km_glutamylCys_GSHsyn_a*Gshgssg.Km_glycine_GSHsyn_a+Gshgssg.glutamylCys_a*Gshgssg.Km_glutamylCys_GSHsyn_a+Gshgssg.glycine_a*Gshgssg.Km_glycine_GSHsyn_a*(1+Gshgssg.glutamylCys_a/Gshgssg.Km_glutamylCys_GSHsyn_a)+u_gthrd_c_a/Gshgssg.KmGSHsyn_a)
    f_ADNCYC_a = ((ATDMP.VmaxfAC_a*u_atp_c_a/(ATDMP.KmACATP_a*(1+u_camp_c_a/ATDMP.KicAMPAC_a))-ATDMP.VmaxrAC_a*u_camp_c_a/(ATDMP.KmpiAC_a*ATDMP.KmcAMPAC_a))/(1+u_atp_c_a/(ATDMP.KmACATP_a*(1+u_camp_c_a/ATDMP.KicAMPAC_a))+u_camp_c_a/ATDMP.KmcAMPAC_a))
    
    f_CKc_n = Creatine.kCKnps*u_pcreat_c_n*u_adp_c_n-Creatine.KeqCKnpms*Creatine.kCKnps*(Creatine.Crtot-u_pcreat_c_n)*u_atp_c_n
    f_CKc_a = Creatine.kCKgps*u_pcreat_c_a*u_adp_c_a-Creatine.KeqCKgpms*Creatine.kCKgps*(Creatine.Crtot-u_pcreat_c_a)*u_atp_c_a
    f_PYRt2m_n = PyrTrCytoMito.Vmax_PYRtrcyt2mito_nH*(u_pyr_c_n*u_h_c_n-u_pyr_m_n*u_h_m_n)/((1.0+u_pyr_c_n/PyrTrCytoMito.KmPyrCytTr_n)*(1.0+u_pyr_m_n/PyrTrCytoMito.KmPyrMitoTr_n))
    f_PYRt2m_a = PyrTrCytoMito.Vmax_PYRtrcyt2mito_aH*(u_pyr_c_a*u_h_c_a-u_pyr_m_a*u_h_m_a)/((1.0+u_pyr_c_a/PyrTrCytoMito.KmPyrCytTr_a)*(1.0+u_pyr_m_a/PyrTrCytoMito.KmPyrMitoTr_a))

    f_notBigg_vShuttlen = Generalizations.TnNADH_jlv*(u_nadh_c_n/(0.212-u_nadh_c_n))/(Generalizations.MnCyto_jlv+(u_nadh_c_n/(0.212-u_nadh_c_n)))*((1000*ETC.NADtot-u_nadh_m_n)/u_nadh_m_n)/(Generalizations.MnMito_jlv+((1000*ETC.NADtot-u_nadh_m_n)/u_nadh_m_n))
    f_notBigg_vShuttleg = Generalizations.TgNADH_jlv*(u_nadh_c_a/(0.212-u_nadh_c_a))/(Generalizations.MgCyto_jlv+(u_nadh_c_a/(0.212-u_nadh_c_a)))*((1000*ETC.NADtot-u_nadh_m_a)/u_nadh_m_a)/(Generalizations.MgMito_jlv+((1000*ETC.NADtot-u_nadh_m_a)/u_nadh_m_a))
    f_notBigg_vMitooutn_n = Generalizations.V_oxphos_n*((1/(u_atp_i_n/u_adp_i_n))/(Generalizations.mu_oxphos_n+(1/(u_atp_i_n/u_adp_i_n))))*((u_nadh_m_n/u_nad_m_n)/(Generalizations.nu_oxphos_n+(u_nadh_m_n/u_nad_m_n)))*(u_o2_c_n/(u_o2_c_n+Generalizations.K_oxphos_n))
    f_notBigg_vMitooutg_a = Generalizations.V_oxphos_a*((1/(u_atp_i_a/u_adp_i_a))/(Generalizations.mu_oxphos_a+(1/(u_atp_i_a/u_adp_i_a))))*((u_nadh_m_a/u_nad_m_a)/(Generalizations.nu_oxphos_a+(u_nadh_m_a/u_nad_m_a)))*(u_o2_c_a/(u_o2_c_a+Generalizations.K_oxphos_a))
    f_notBigg_vMitoinn = Generalizations.VMaxMitoinn*u_pyr_m_n/(u_pyr_m_n+Generalizations.KmMito)*(1000*ETC.NADtot-u_nadh_m_n)/(1000*ETC.NADtot-u_nadh_m_n+Generalizations.KmNADn_jlv)
    f_notBigg_vMitoing = Generalizations.VMaxMitoing*u_pyr_m_a/(u_pyr_m_a+Generalizations.KmMito_a)*(1000*ETC.NADtot-u_nadh_m_a)/(1000*ETC.NADtot-u_nadh_m_a+Generalizations.KmNADg_jlv)


    # build du
    du = np.zeros_like(u)
    # the 0 values are omitted for speed but reported as a comment to underline that we want them as 0

    # du[UIdx.h_m_n] = 0
    du[UIdx.k_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_KH_n+f_notBigg_J_K_n)/ETC.W_x)
    du[UIdx.mg2_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_notBigg_J_MgATPx_n-f_notBigg_J_MgADPx_n)/ETC.W_x)
    du[UIdx.nadh_m_n] = 6.96*(f_notBigg_vMitoinn+f_notBigg_vShuttlen-f_notBigg_vMitooutn_n)
    du[UIdx.q10h2_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_NADH2_u10mi_n-f_CYOR_u10mi_n)/ETC.W_x)

    # print(u_nadh_m_n)
    # print(u_q10h2_m_n)
    # print(f_CYOR_u10mi_n)
    # print(u_focytC_m_n)
    # print(u_q10h2_m_n,u_pi_m_n)
    # print(u_notBigg_MitoMembrPotent_m_n)
# debug
# u_nadh_m_n = 0.3146584474671007
# u_q10h2_m_n = 0.0155067120830932
# NADH2_u10mi_n(u_nadh_m_n, u_q10h2_m_n) = 0.00019979828104945647
# u_focytC_m_n = 0.1318502545732708
# u_notBigg_MitoMembrPotent_m_n = 152.33918637408712
# (u_q10h2_m_n, u_pi_m_n) = (0.0155067120830932, 17.22873019667985)
# CYOR_u10mi_n(u_focytC_m_n, u_notBigg_MitoMembrPotent_m_n, u_q10h2_m_n, u_pi_m_n) = 0.00019979930000609114
# /debug


    du[UIdx.focytC_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+2*f_CYOR_u10mi_n-2*f_CYOOm2i_n)/ETC.W_i)
    du[UIdx.o2_c_n] = f_notBigg_JO2fromCap2n-0.6*f_notBigg_vMitooutn_n
    du[UIdx.atp_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_ATPS4mi_n-f_ATPtm_n)/ETC.W_x)
    du[UIdx.adp_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_ATPS4mi_n+f_ATPtm_n)/ETC.W_x)
    du[UIdx.notBigg_ATP_mx_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgATPx_n)/ETC.W_x)
    du[UIdx.notBigg_ADP_mx_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgADPx_n)/ETC.W_x)
    du[UIdx.pi_m_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_ATPS4mi_n+f_notBigg_J_Pi1_n)/ETC.W_x)
    du[UIdx.atp_i_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_notBigg_J_ATP_n+f_ATPtm_n+f_ADK1m_n)/ETC.W_i)
    du[UIdx.adp_i_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_notBigg_J_ADP_n-f_ATPtm_n-2*f_ADK1m_n)/ETC.W_i)
    du[UIdx.amp_i_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_notBigg_J_AMP_n+f_ADK1m_n)/ETC.W_i)
    du[UIdx.notBigg_ATP_mi_i_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgATPi_n)/ETC.W_i)
    du[UIdx.notBigg_ADP_mi_i_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgADPi_n)/ETC.W_i)
    du[UIdx.pi_i_n] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_notBigg_J_Pi1_n+f_notBigg_J_Pi2_n)/ETC.W_i)
    du[UIdx.notBigg_MitoMembrPotent_m_n] = 0.5*GeneralConstants.T2Jcorrection*(4*f_NADH2_u10mi_n+2*f_CYOR_u10mi_n+4*f_CYOOm2i_n-ETC.n_A*f_ATPS4mi_n-f_ATPtm_n-f_notBigg_J_Hle_n-f_notBigg_J_K_n)/ETC.CIM
    # du[UIdx.notBigg_Ctot_m_n] = 0
    # du[UIdx.notBigg_Qtot_m_n] = 0
    # du[UIdx.h_i_n] = 0
    du[UIdx.atp_c_n] = (f_CKc_n+0.5*(1/6.96)*1000*(-f_notBigg_J_ATP_n)-f_HEX1_n-f_PFK_n+f_PGK_n+f_PYK_n )/(1-dAMPdATPn) #(f_CKc_n+0.5*(1/6.96)*1000*(-f_notBigg_J_ATP_n)-f_HEX1_n-f_PFK_n+f_PGK_n+f_PYK_n-0.15*vPumpn-vATPasesn)/(1-dAMPdATPn)
    # du[UIdx.24] = 0
    du[UIdx.fum_m_n] = GeneralConstants.T2Jcorrection*(0.5*1000*f_r0509_n/ETC.W_x-f_FUMm_n)
    du[UIdx.mal_L_m_n] = GeneralConstants.T2Jcorrection*(f_FUMm_n-f_MDHm_n)+6.96*f_AKGMALtm_n
    du[UIdx.oaa_m_n] = GeneralConstants.T2Jcorrection*(f_MDHm_n-f_CSm_n)+f_ASPTAm_n
    du[UIdx.succ_m_n] = GeneralConstants.T2Jcorrection*(0.5*f_SUCOASm_n-0.5*1000*f_r0509_n/ETC.W_x)+0.5*GeneralConstants.T2Jcorrection*f_OCOAT1m_n
    du[UIdx.succoa_m_n] = 0.5*GeneralConstants.T2Jcorrection*(f_AKGDm_n-f_SUCOASm_n)-0.5*GeneralConstants.T2Jcorrection*f_OCOAT1m_n
    du[UIdx.coa_m_n] = GeneralConstants.T2Jcorrection*(f_CSm_n-f_PDHm_n-0.5*f_AKGDm_n+0.5*f_SUCOASm_n-0.5*f_ACACT1rm_n)
    du[UIdx.akg_m_n] = 0.5*GeneralConstants.T2Jcorrection*(f_ICDHxm_n-f_AKGDm_n)-f_ASPTAm_n-f_AKGMALtm_n
    # du[UIdx.ca2_m_n] = 0
    du[UIdx.icit_m_n] = 0.5*GeneralConstants.T2Jcorrection*(f_ACONTm_n-f_ICDHxm_n)
    du[UIdx.cit_m_n] = GeneralConstants.T2Jcorrection*(f_CSm_n-0.5*f_ACONTm_n)
    du[UIdx.accoa_m_n] = GeneralConstants.T2Jcorrection*(f_PDHm_n-f_CSm_n)+GeneralConstants.T2Jcorrection*f_ACACT1rm_n
    du[UIdx.acac_c_n] = 0.5*GeneralConstants.T2Jcorrection*(f_BDHm_n-f_OCOAT1m_n)
    du[UIdx.aacoa_m_n] = 0.5*GeneralConstants.T2Jcorrection*(f_OCOAT1m_n-f_ACACT1rm_n)
    du[UIdx.pyr_m_n] = 6.96*f_PYRt2m_n-GeneralConstants.T2Jcorrection*f_PDHm_n
    du[UIdx.bhb_c_n] = 0.44*f_BHBt_n-f_BDHm_n
    du[UIdx.bhb_e_e] = 0.0275*f_notBigg_MCT1_bHB_b-f_BHBt_n-f_BHBt_a
    du[UIdx.bhb_c_a] = 0 #0.8*BHBt_a(u_bhb_e_e,u_bhb_c_a) - BDHm_a(u_bhb_c_a,u_acac_c_a,u_nad_m_a,u_nadh_m_a) # 0
    du[UIdx.bhb_b_b] = f_notBigg_JbHBTrArtCap-f_notBigg_MCT1_bHB_b
    # du[UIdx.asp_L_m_n] = 0
    # du[UIdx.asp_L_c_n] = 0
    du[UIdx.glu_L_m_n] = 0.5*GeneralConstants.T2Jcorrection*(f_ASPTAm_n+6.96*f_ASPGLUm_n+f_GLUNm_n)
    # du[UIdx.mal_L_c_n] = 0
    # du[UIdx.oaa_c_n] = 0
    # du[UIdx.akg_c_n] = 0
    du[UIdx.glu_L_c_n] = f_ASPTA_n-f_ASPGLUm_n
    du[UIdx.nadh_c_n] = f_GAPD_n-f_LDH_L_n-f_notBigg_vShuttlen
    # du[UIdx.h_m_a] = 0
    du[UIdx.k_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_KH_a+f_notBigg_J_K_a)/ETC.W_x)
    du[UIdx.mg2_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_notBigg_J_MgATPx_a-f_notBigg_J_MgADPx_a)/ETC.W_x)
    du[UIdx.nadh_m_a] = 6.96*(f_notBigg_vMitoing+f_notBigg_vShuttleg-f_notBigg_vMitooutg_a)
    du[UIdx.q10h2_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_NADH2_u10mi_a-f_CYOR_u10mi_a)/ETC.W_x)
    du[UIdx.focytC_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+2*f_CYOR_u10mi_a-2*f_CYOOm2i_a)/ETC.W_i)
    du[UIdx.o2_c_a] = f_notBigg_JO2fromCap2a-0.6*f_notBigg_vMitooutg_a
    du[UIdx.atp_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_ATPS4mi_a-f_ATPtm_a)/ETC.W_x)
    du[UIdx.adp_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_ATPS4mi_a+f_ATPtm_a)/ETC.W_x)
    du[UIdx.notBigg_ATP_mx_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgATPx_a)/ETC.W_x)
    du[UIdx.notBigg_ADP_mx_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgADPx_a)/ETC.W_x)
    du[UIdx.pi_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_ATPS4mi_a+f_notBigg_J_Pi1_a)/ETC.W_x)
    du[UIdx.atp_i_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_notBigg_J_ATP_a+f_ATPtm_a+f_ADK1m_a)/ETC.W_i)
    du[UIdx.adp_i_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_notBigg_J_ADP_a-f_ATPtm_a-2*f_ADK1m_a)/ETC.W_i)
    du[UIdx.amp_i_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(+f_notBigg_J_AMP_a+f_ADK1m_a)/ETC.W_i)
    du[UIdx.notBigg_ATP_mi_i_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgATPi_a)/ETC.W_i)
    du[UIdx.notBigg_ADP_mi_i_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(f_notBigg_J_MgADPi_a)/ETC.W_i)
    du[UIdx.pi_i_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*(-f_notBigg_J_Pi1_a+f_notBigg_J_Pi2_a)/ETC.W_i)
    du[UIdx.notBigg_MitoMembrPotent_m_a] = 0.5*GeneralConstants.T2Jcorrection*((4*f_NADH2_u10mi_a+2*f_CYOR_u10mi_a+4*f_CYOOm2i_a-ETC.n_A*f_ATPS4mi_a-f_ATPtm_a-f_notBigg_J_Hle_a-f_notBigg_J_K_a)/ETC.CIM)
    # du[UIdx.notBigg_Ctot_m_a] = 0
    # du[UIdx.notBigg_Qtot_m_a] = 0
    # du[UIdx.h_i_a] = 0
    du[UIdx.atp_c_a] = (-(u_ca2_c_a/Glycogen.cai0_ca_ion)*(1+GeneralConstants.xNEmod*(u_nrpphr_e_e/(GeneralConstants.KdNEmod+u_nrpphr_e_e)))*f_ADNCYC_a+f_CKc_a+0.5*(1/6.96)*1000*(-f_notBigg_J_ATP_a)-f_HEX1_a-f_PFK_a-f_PFK26_a+f_PGK_a+f_PYK_a-0.15*(7/4)*vPumpg-ATDMP.vATPasesg)/(1-dAMPdATPg)
    # du[UIdx.74] = 0
    du[UIdx.fum_m_a] = 0.5*GeneralConstants.T2Jcorrection*(1000*f_r0509_a/ETC.W_x-f_FUMm_a)
    du[UIdx.mal_L_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_FUMm_a-f_MDHm_a)
    du[UIdx.oaa_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_MDHm_a-f_CSm_a+f_PCm_a)
    du[UIdx.succ_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_SUCOASm_a-1000*f_r0509_a/ETC.W_x)
    du[UIdx.succoa_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_AKGDm_a-f_SUCOASm_a)
    du[UIdx.coa_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_CSm_a-f_PDHm_a-f_AKGDm_a+f_SUCOASm_a)
    du[UIdx.akg_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_ICDHxm_a-f_AKGDm_a+f_GLUDxm_a)
    # du[UIdx.ca2_m_a] = 0
    du[UIdx.icit_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_ACONTm_a-f_ICDHxm_a)
    du[UIdx.cit_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_CSm_a-f_ACONTm_a)
    du[UIdx.accoa_m_a] = 0.5*GeneralConstants.T2Jcorrection*(f_PDHm_a-f_CSm_a)
    # du[UIdx.acac_c_a] = 0
    # du[UIdx.aacoa_m_a] = 0
    du[UIdx.pyr_m_a] = 6.96*f_PYRt2m_a-GeneralConstants.T2Jcorrection*(f_PDHm_a+f_PCm_a)
    du[UIdx.gln_L_c_n] = GeneralConstants.T2Jcorrection*(f_GLNt4_n-f_GLUNm_n)
    du[UIdx.gln_L_e_e] = GeneralConstants.T2Jcorrection*(-f_GLNt4_n+f_GLNt4_a)
    du[UIdx.gln_L_c_a] = GeneralConstants.T2Jcorrection*(-f_GLNt4_a+f_GLNS_a)
    du[UIdx.glu_L_c_a] = GeneralConstants.T2Jcorrection*(0.0266*f_GLUt6_a-f_GLNS_a-f_GLUDxm_a)
    # du[UIdx.notBigg_Va_c_a] = 0 # (1/4e-4)*(-dIPump_a-IBK-IKirAS-IKirAV-IleakA-ITRP_a)
    # du[UIdx.na1_c_a] = 0 # vLeakNag-3*vPumpg+vgstim
    # du[UIdx.k_c_a] = 0 # JNaK_a+(-IleakA-IBK-IKirAS-IKirAV)/(4e-4*843.0*1000.)-RateDecayK_a*(u_k_c_a-u0_ss[95])
    # du[UIdx.k_e_e] = 0 # SmVn/F*ik_density*(eto_n/eto_ecs)-2*vPumpn*(eto_n/eto_ecs)-2*(eto_a/eto_ecs)*vPumpg-JdiffK-((-IleakA-IBK-IKirAS-IKirAV)/(4e-4*843.0*1000.0))
    # du[UIdx.glu_L_syn_syn] = 0
    # du[UIdx.notBigg_VNeu_c_n] = 0 # 1/Cm*(-IL-ina_density-ik_density-ICa-ImAHP-dIPump) #+Isyne+Isyni-IM+Iinj)
    # du[UIdx.na1_c_n] = 0 # vLeakNan-3*vPumpn+vnstim
    # du[UIdx.notBigg_hgate_c_n] = 0 # phi*(hinf-u_notBigg_hgate_c_n)/tauh
    # du[UIdx.notBigg_ngate_c_n] = 0 # phi*(ninf-u_notBigg_ngate_c_n)/taun
    # du[UIdx.ca2_c_n] = 0 # -SmVn/F*ICa-(u_ca2_c_n-u0_ss[102])/tauCa
    # du[UIdx.notBigg_pgate_c_n] = 0 # phi*(p_inf-u_notBigg_pgate_c_n)/tau_p
    # du[UIdx.notBigg_nBK_c_a] = 0 # psiBK*cosh((u_notBigg_Va_c_a-(-0.5*v5BK*tanh((u_ca2_c_a-Ca3BK)/Ca4BK)+v6BK))/(2*v4BK))*(nBKinf-u_notBigg_nBK_c_a)
    # du[UIdx.notBigg_mGluRboundRatio_c_a] = 0
    # du[UIdx.notBigg_IP3_c_a] = 0 # rhIP3a*((u_notBigg_mGluRboundRatio_c_a+deltaGlutSyn)/(KGlutSyn+u_notBigg_mGluRboundRatio_c_a+deltaGlutSyn))-kdegIP3a*u_notBigg_IP3_c_a
    # du[UIdx.notBigg_hIP3Ca_c_a] = 0 # konhIP3Ca_a*(khIP3Ca_aINH-(u_ca2_c_a+khIP3Ca_aINH)*u_notBigg_hIP3Ca_c_a)
    # du[UIdx.ca2_c_a] = 0 # beta_Ca_a*(IIP3_a-ICa_pump_a+Ileak_CaER_a)-0.5*ITRP_a/(4e-4*843.0*1000.)
    # du[UIdx.ca2_r_a] = 0
    # du[UIdx.notBigg_sTRP_c_a] = 0 # (Ca_perivasc/tauTRPCa_perivasc)*(sinfTRPV-u_notBigg_sTRP_c_a)
    # du[UIdx.111] = 0 # notBigg_FinDyn_W2017(t)-notBigg_Fout_W2017(t,u_notBigg_vV_b_b)
    # du[UIdx.notBigg_EET_c_a] = 0 # VprodEET_a*(u_ca2_c_a-CaMinEET_a)-kdeg_EET_a*u_notBigg_EET_c_a
    du[UIdx.notBigg_ddHb_b_b] = f_notBigg_JdHbin-f_notBigg_JdHbout
    du[UIdx.o2_b_b] = f_notBigg_JO2art2cap-(GeneralConstants.eto_n/GeneralConstants.eto_b)*f_notBigg_JO2fromCap2n-(GeneralConstants.eto_a/GeneralConstants.eto_b)*f_notBigg_JO2fromCap2a
    du[UIdx.glc_D_b_b] = f_notBigg_trGLC_art_cap-f_notBigg_JGlc_be
    du[UIdx.glc_D_ecsEndothelium_ecsEndothelium] = 0.32*f_notBigg_JGlc_be-f_notBigg_JGlc_e2ecsBA
    du[UIdx.glc_D_ecsBA_ecsBA] = 1.13*f_notBigg_JGlc_e2ecsBA-f_notBigg_JGlc_ecsBA2a-f_notBigg_JGlc_diffEcs
    du[UIdx.glc_D_c_a] = 0.06*f_notBigg_JGlc_ecsBA2a-f_HEX1_a-f_notBigg_JGlc_a2ecsAN
    du[UIdx.glc_D_ecsAN_ecsAN] = 1.35*f_notBigg_JGlc_a2ecsAN-f_notBigg_JGlc_ecsAN2n+0.08*f_notBigg_JGlc_diffEcs
    du[UIdx.glc_D_c_n] = 0.41*f_notBigg_JGlc_ecsAN2n-f_HEX1_n
    du[UIdx.g6p_c_n] = f_HEX1_n-f_PGI_n-f_G6PDH2r_n
    du[UIdx.g6p_c_a] = f_HEX1_a-f_PGI_a-f_G6PDH2r_a+f_PGMT_a
    du[UIdx.f6p_c_n] = f_PGI_n-f_PFK_n-f_TKT2_n+f_TALA_n
    du[UIdx.f6p_c_a] = f_PGI_a-f_PFK_a-f_PFK26_a-f_TKT2_a+f_TALA_a
    du[UIdx.fdp_c_n] = f_PFK_n-f_FBA_n
    du[UIdx.fdp_c_a] = f_PFK_a-f_FBA_a
    du[UIdx.f26bp_c_a] = f_PFK26_a
    du[UIdx.glycogen_c_a] = f_GLCS2_a-f_GLCP_a
    # du[UIdx.amp_c_n] = 0
    # du[UIdx.amp_c_a] = 0
    du[UIdx.g1p_c_a] = 10*f_GLCP_a-f_PGMT_a-f_GALUi_a
    du[UIdx.g3p_c_n] = f_FBA_n-f_GAPD_n+f_TPI_n-f_TKT2_n-f_TALA_n+f_TKT1_n
    du[UIdx.g3p_c_a] = f_FBA_a-f_GAPD_a+f_TPI_a-f_TKT2_a-f_TALA_a+f_TKT1_a
    du[UIdx.dhap_c_n] = f_FBA_n-f_TPI_n
    du[UIdx.dhap_c_a] = f_FBA_a-f_TPI_a
    du[UIdx.n13dpg_c_n] = f_GAPD_n-f_PGK_n
    du[UIdx.n13dpg_c_a] = f_GAPD_a-f_PGK_a
    du[UIdx.nadh_c_a] = f_GAPD_a-f_LDH_L_a-f_notBigg_vShuttleg
    # du[UIdx.pi_c_n] = 0
    # du[UIdx.pi_c_a] = 0
    du[UIdx.n3pg_c_n] = f_PGK_n-f_PGM_n
    du[UIdx.n3pg_c_a] = f_PGK_a-f_PGM_a
    du[UIdx.n2pg_c_n] = f_PGM_n-f_ENO_n
    du[UIdx.n2pg_c_a] = f_PGM_a-f_ENO_a
    du[UIdx.pep_c_n] = f_ENO_n-f_PYK_n
    du[UIdx.pep_c_a] = f_ENO_a-f_PYK_a
    du[UIdx.pyr_c_n] = f_PYK_n-f_PYRt2m_n-f_LDH_L_n
    du[UIdx.pyr_c_a] = f_PYK_a-f_PYRt2m_a-f_LDH_L_a
    du[UIdx.lac_L_b_b] = f_notBigg_JLacTr_b-f_notBigg_MCT1_LAC_b-f_notBigg_vLACgc
    du[UIdx.lac_L_e_e] = 0.0275*f_notBigg_MCT1_LAC_b-f_L_LACt2r_a-f_L_LACt2r_n+f_notBigg_jLacDiff_e
    du[UIdx.lac_L_c_a] = 0.8*f_L_LACt2r_a+0.022*f_notBigg_vLACgc+f_LDH_L_a
    du[UIdx.lac_L_c_n] = 0.44*f_L_LACt2r_n+f_LDH_L_n
    du[UIdx.nadph_c_n] = f_G6PDH2r_n+f_GND_n-f_notBigg_psiNADPHox_n-f_GTHO_n
    du[UIdx.nadph_c_a] = f_G6PDH2r_a+f_GND_a-f_notBigg_psiNADPHox_a-f_GTHO_a
    du[UIdx.n6pgl_c_n] = f_G6PDH2r_n-f_PGL_n
    du[UIdx.n6pgl_c_a] = f_G6PDH2r_a-f_PGL_a
    du[UIdx.n6pgc_c_n] = f_PGL_n-f_GND_n
    du[UIdx.n6pgc_c_a] = f_PGL_a-f_GND_a
    du[UIdx.ru5p_D_c_n] = f_GND_n-f_RPE_n-f_RPI_n
    du[UIdx.ru5p_D_c_a] = f_GND_a-f_RPE_a-f_RPI_a
    du[UIdx.r5p_c_n] = f_RPI_n-f_TKT1_n
    du[UIdx.r5p_c_a] = f_RPI_a-f_TKT1_a
    du[UIdx.xu5p_D_c_n] = f_RPE_n-f_TKT1_n+f_TKT2_n
    du[UIdx.xu5p_D_c_a] = f_RPE_a-f_TKT1_a+f_TKT2_a
    du[UIdx.s7p_c_n] = f_TKT1_n-f_TALA_n
    du[UIdx.s7p_c_a] = f_TKT1_a-f_TALA_a
    du[UIdx.e4p_c_n] = f_TKT2_n+f_TALA_n
    du[UIdx.e4p_c_a] = f_TKT2_a+f_TALA_a
    du[UIdx.gthrd_c_n] = 2*(f_GTHO_n-f_GTHP_n)+f_GTHS_n
    du[UIdx.gthrd_c_a] = 2*(f_GTHO_a-f_GTHP_a)+f_GTHS_a
    du[UIdx.gthox_c_n] = -f_GTHO_n+f_GTHP_n
    du[UIdx.gthox_c_a] = -f_GTHO_a+f_GTHP_a
    # du[UIdx.creat_c_n] = 0
    du[UIdx.pcreat_c_n] = -f_CKc_n
    # du[UIdx.creat_c_a] = 0
    du[UIdx.pcreat_c_a] = -f_CKc_a
    du[UIdx.camp_c_a] = (u_ca2_c_a/Glycogen.cai0_ca_ion)*(1+GeneralConstants.xNEmod*(u_nrpphr_e_e/(GeneralConstants.KdNEmod+u_nrpphr_e_e)))*f_ADNCYC_a-f_PDE1_a
    # du[UIdx.nrpphr_e_e] = 0
    # du[UIdx.udpg_c_a] = 0
    # du[UIdx.utp_c_a] = 0
    # du[UIdx.notBigg_GS_c_a] = 0
    du[UIdx.notBigg_GPa_c_a] = f_notBigg_psiPHK_a
    du[UIdx.notBigg_GPb_c_a] = -f_notBigg_psiPHK_a

    return du


if __name__ == "__main__":
    # Create a dummy u array
    from multiscale_run.metabolism.initial_conditions import make_u0
    u = make_u0()
    p = np.ones(PIdx.size) * 1.0  # dummy, unused in this simple test
    t = 0.0  # dummy time

    # Call compute_du
    du = compute_du(u, p, t)

    # # Print a few du values to check
    # print("u")
    # print(u)
    # print("p")
    # print(p)
    # print("t")
    # print(t)
    # print("du:")
    # for s, v in zip(UIdx.as_list(), du):
    #     print(s, v)
    # print()
    # if np.any(np.isnan(du)):
    #     print("There are nan values!")
    # if np.any(np.isinf(du)):
    #     print("There are inf values!")
