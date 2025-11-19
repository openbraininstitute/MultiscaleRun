"""
indexes.py — singleton container for progressive integer indexes.

Usage:
    import MIdx
    MIdx.h_m_n        # -> 0
    MIdx.size
    MIdx.get_comment("pyr_m_n")
    MIdx.as_dict()    # -> {"h_m_n": 0, ...}
"""

from typing import Dict

# index name -> comment (kept as provided)
_PNAMES_WITH_COMMENTS = {
    "ina_density": "",
    "ik_density": "",
    "mito_scale": "",
    "notBigg_FinDyn_W2017": "",
    "notBigg_Fout_W2017": "",
    "notBigg_vV_b_b": "",
}
# index name -> comment (kept as provided)
_UNAMES_WITH_COMMENTS = {
    "h_m_n": "1",
    "k_m_n": "2",
    "mg2_m_n": "3",
    "nadh_m_n": "4",
    "q10h2_m_n": "5",
    "focytC_m_n": "6",
    "o2_c_n": "7",
    "atp_m_n": "8",
    "adp_m_n": "9",
    "notBigg_ATP_mx_m_n": "10",
    "notBigg_ADP_mx_m_n": "11",
    "pi_m_n": "12",
    "atp_i_n": "13",
    "adp_i_n": "14",
    "amp_i_n": "15",
    "notBigg_ATP_mi_i_n": "16",
    "notBigg_ADP_mi_i_n": "17",
    "pi_i_n": "18",
    "notBigg_MitoMembrPotent_m_n": "19",
    "notBigg_Ctot_m_n": "20",
    "notBigg_Qtot_m_n": "21",
    "h_i_n": "22",
    "atp_c_n": "23",
    "fum_m_n": "25",
    "mal_L_m_n": "26",
    "oaa_m_n": "27",
    "succ_m_n": "28",
    "succoa_m_n": "29",
    "coa_m_n": "30",
    "akg_m_n": "31",
    "ca2_m_n": "32",
    "icit_m_n": "33",
    "cit_m_n": "34",
    "accoa_m_n": "35",
    "acac_c_n": "36",
    "aacoa_m_n": "37",
    "pyr_m_n": "38",
    "bhb_c_n": "39",
    "bhb_e_e": "40",
    "bhb_c_a": "41",
    "bhb_b_b": "42",
    "asp_L_m_n": "43",
    "asp_L_c_n": "44",
    "glu_L_m_n": "45",
    "mal_L_c_n": "46",
    "oaa_c_n": "47",
    "akg_c_n": "48",
    "glu_L_c_n": "49",
    "nadh_c_n": "50",
    "h_m_a": "51",
    "k_m_a": "52",
    "mg2_m_a": "53",
    "nadh_m_a": "54",
    "q10h2_m_a": "55",
    "focytC_m_a": "56",
    "o2_c_a": "57",
    "atp_m_a": "58",
    "adp_m_a": "59",
    "notBigg_ATP_mx_m_a": "60",
    "notBigg_ADP_mx_m_a": "61",
    "pi_m_a": "62",
    "atp_i_a": "63",
    "adp_i_a": "64",
    "amp_i_a": "65",
    "notBigg_ATP_mi_i_a": "66",
    "notBigg_ADP_mi_i_a": "67",
    "pi_i_a": "68",
    "notBigg_MitoMembrPotent_m_a": "69",
    "notBigg_Ctot_m_a": "70",
    "notBigg_Qtot_m_a": "71",
    "h_i_a": "72",
    "atp_c_a": "73",
    "fum_m_a": "75",
    "mal_L_m_a": "76",
    "oaa_m_a": "77",
    "succ_m_a": "78",
    "succoa_m_a": "79",
    "coa_m_a": "80",
    "akg_m_a": "81",
    "ca2_m_a": "82",
    "icit_m_a": "83",
    "cit_m_a": "84",
    "accoa_m_a": "85",
    "acac_c_a": "86",
    "aacoa_m_a": "87",
    "pyr_m_a": "88",
    "gln_L_c_n": "89",
    "gln_L_e_e": "90",
    "gln_L_c_a": "91",
    "glu_L_c_a": "92",
    "notBigg_Va_c_a": "93",
    "na1_c_a": "94",
    "k_c_a": "95",
    "k_e_e": "96",
    "glu_L_syn_syn": "97",
    "notBigg_VNeu_c_n": "98",
    "na1_c_n": "99",
    "notBigg_hgate_c_n": "100",
    "notBigg_ngate_c_n": "101",
    "ca2_c_n": "102",
    "notBigg_pgate_c_n": "103",
    "notBigg_nBK_c_a": "104",
    "notBigg_mGluRboundRatio_c_a": "105",
    "notBigg_IP3_c_a": "106",
    "notBigg_hIP3Ca_c_a": "107",
    "ca2_c_a": "108",
    "ca2_r_a": "109",
    "notBigg_sTRP_c_a": "110",
    "notBigg_EET_c_a": "112",
    "notBigg_ddHb_b_b": "113",
    "o2_b_b": "114",
    "glc_D_b_b": "115",
    "glc_D_ecsEndothelium_ecsEndothelium": "116",
    "glc_D_ecsBA_ecsBA": "117",
    "glc_D_c_a": "118",
    "glc_D_ecsAN_ecsAN": "119",
    "glc_D_c_n": "120",
    "g6p_c_n": "121",
    "g6p_c_a": "122",
    "f6p_c_n": "123",
    "f6p_c_a": "124",
    "fdp_c_n": "125",
    "fdp_c_a": "126",
    "f26bp_c_a": "127",
    "glycogen_c_a": "128",
    "amp_c_n": "129",
    "amp_c_a": "130",
    "g1p_c_a": "131",
    "g3p_c_n": "132",
    "g3p_c_a": "133",
    "dhap_c_n": "134",
    "dhap_c_a": "135",
    "n13dpg_c_n": "136",
    "n13dpg_c_a": "137",
    "nadh_c_a": "138",
    "pi_c_n": "139",
    "pi_c_a": "140",
    "n3pg_c_n": "141",
    "n3pg_c_a": "142",
    "n2pg_c_n": "143",
    "n2pg_c_a": "144",
    "pep_c_n": "145",
    "pep_c_a": "146",
    "pyr_c_n": "147",
    "pyr_c_a": "148",
    "lac_L_b_b": "149",
    "lac_L_e_e": "150",
    "lac_L_c_a": "151",
    "lac_L_c_n": "152",
    "nadph_c_n": "153",
    "nadph_c_a": "154",
    "n6pgl_c_n": "155",
    "n6pgl_c_a": "156",
    "n6pgc_c_n": "157",
    "n6pgc_c_a": "158",
    "ru5p_D_c_n": "159",
    "ru5p_D_c_a": "160",
    "r5p_c_n": "161",
    "r5p_c_a": "162",
    "xu5p_D_c_n": "163",
    "xu5p_D_c_a": "164",
    "s7p_c_n": "165",
    "s7p_c_a": "166",
    "e4p_c_n": "167",
    "e4p_c_a": "168",
    "gthrd_c_n": "169",
    "gthrd_c_a": "170",
    "gthox_c_n": "171",
    "gthox_c_a": "172",
    "creat_c_n": "173",
    "pcreat_c_n": "174",
    "creat_c_a": "175",
    "pcreat_c_a": "176",
    "camp_c_a": "177",
    "nrpphr_e_e": "178",
    "udpg_c_a": "179",
    "utp_c_a": "180",
    "notBigg_GS_c_a": "181",
    "notBigg_GPa_c_a": "182",
    "notBigg_GPb_c_a": "183",
}


class _Idx:
    """Internal class used to build the singleton IMdx."""

    def __init__(self, mapping: Dict[str, str]):
        # store mapping (name -> comment)
        self._comments = dict(mapping)
        # create progressive indexes as attributes (name -> int)
        for idx, name in enumerate(mapping):
            setattr(self, name, idx)
        self.size = len(mapping)

    def get_comment(self, name: str) -> str:
        return self._comments.get(name, "")

    def as_dict(self) -> Dict[str, int]:
        """Return name -> index mapping."""
        return {name: getattr(self, name) for name in self._comments}

    def comments_dict(self) -> Dict[str, str]:
        """Return name -> comment mapping."""
        return dict(self._comments)

    def __str__(self) -> str:
        return "\n".join(
            f"{name}: {getattr(self, name)} #{self._comments[name]}" for name in self._comments
        )


# singleton instance exported for module users
PIdx = _Idx(_PNAMES_WITH_COMMENTS)
# singleton instance exported for module users
UIdx = _Idx(_UNAMES_WITH_COMMENTS)


if __name__ == "__main__":
    print("PIdx:")
    print(PIdx)
    print(f"Total: {PIdx.size}")
    print("UIdx:")
    print(UIdx)
    print(f"Total: {UIdx.size}")
