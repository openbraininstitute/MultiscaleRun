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

# index name -> comment
_PNAMES_WITH_COMMENTS = {
    "ina_density": "#0",
    "ik_density": "#1",
    "mito_scale": "#2",
    "notBigg_FinDyn_W2017": "#3",
    "notBigg_Fout_W2017": "#4",
    "notBigg_vV_b_b": "#5",
}
# index name -> comment
_UNAMES_WITH_COMMENTS = {
    "h_m_n": "#1",
    "K_x_n": "Potassium ion in neuronal mito, matrix #2, k_m_n",
    "mg2_m_n": "#3",
    "NADHmito_n": "NADH in neuronal mito #4, nadh_m_n",
    "QH2mito_n": "Reduced ubiquinol in neuronal mito. matrix, #4, q10h2_m_n",
    "CytCredmito_n": "Reduced cytochrome c in neuronal mito. matrix, #5, focytC_m_n",
    "O2_n": "Oxygen in neuronal cytosol, #6, o2_c_n",
    "ATPmito_n": "Free ATP in neuronal mito. matrix, #7, ATPmito_n",
    "ADPmito_n": "Free ADP in neuronal mito. matrix, #8, ADPmito_n",
    "ATP_mx_n": "Magnesium-bound ATP in neuronal mito. matrix, #9, notBigg_ATP_mx_m_n",
    "ADP_mx_n": "Magnesium-bound ADP in neuronal mito. matrix, #10, notBigg_ADP_mx_m_n",
    "Pimito_n": "Phosphate in neuronal mito. matrix, #11, pi_m_n",
    "ATP_i_n": "Free ATP in neuronal mito. IMS, #12, atp_i_n",
    "ADP_i_n": "Free ADP in neuronal mito. IMS, #13, adp_i_n",
    "amp_i_n": "#15",
    "ATP_mi_n": "Magnesium-bound ATP in neuronal mito. IMS, #14, notBigg_ATP_mi_i_n",
    "ADP_mi_n": "Magnesium-bound ADP in neuronal mito. IMS, #15, notBigg_ADP_mi_i_n",
    "Pi_i_n": "Phosphate in neuronal mito. IMS, #16, pi_i_n",
    "MitoMembrPotent_n": "Neuronal mitochondrial membrane potential, #17, notBigg_MitoMembrPotent_m_n",
    "notBigg_Ctot_m_n": "#20",
    "notBigg_Qtot_m_n": "#21",
    "h_i_n": "#22",
    "ATP_n": "ATP in neuronal cytosol, #18, atp_c_n",
    "adp_c_n": "#24",
    "FUMmito_n": "Fumarate in neuronal mito., #19, fum_m_n",
    "MALmito_n": "L-Malate in neuronal mito., #20, mal_L_m_n",
    "OXAmito_n": "Oxaloacetate in neuronal mito., #21, oaa_m_n",
    "SUCmito_n": "Succinate in neuronal mito., #22, succ_m_n",
    "SUCCOAmito_n": "Succinyl-CoA in neuronal mito., #23, succoa_m_n",
    "CoAmito_n": "Coenzyme A in neuronal mito., #24, coa_m_n",
    "AKGmito_n": "Alpha-ketoglutarate in neuronal mito., #25, akg_m_n",
    "ca2_m_n": "#32",
    "ISOCITmito_n": "Isocitrate in neuronal mito., #26, icit_m_n",
    "CITmito_n": "Citrate in neuronal mito., #27, cit_m_n",
    "AcCoAmito_n": "Acetyl-CoA in neuronal mito., #28, accoa_m_n",
    "AcAc_n": "Acetoacetate in neuron (only mito., no cytosolic AcAc in the model), #29, acac_c_n",
    "AcAcCoA_n": "Acetoacetyl-CoA in neuronal mito., #30, aacoa_m_n",
    "PYRmito_n": "Pyruvate in neuronal mito., #31, pyr_m_n",
    "bHB_n": "beta-Hydroxybutyrate in neuronal cytosol, #32, bhb_c_n",
    "bHB_ecs": "beta-Hydroxybutyrate in extracellular space, #33, bhb_e_e",
    "bhb_c_a": "#41",
    "bHB_b": "beta-Hydroxybutyrate in capillaries, #34, bhb_b_b",
    "asp_L_m_n": "#43",
    "asp_L_c_n": "#44",
    "glu_L_m_n": "#45",
    "mal_L_c_n": "#46",
    "oaa_c_n": "#47",
    "akg_c_n": "#48",
    "glu_L_c_n": "#49",
    "NADH_n": "NADH in neuronal cytosol, #37, nadh_c_n",
    "h_m_a": "#51",
    "K_x_a": "Potassium ion in astrocytic mito. matrix, #38, k_m_a",
    "Mg_x_a": "Magnesium ion in astrocytic mito. matrix, #39, mg2_m_a",
    "NADHmito_a": "NADH in astrocytic mito., #40, nadh_m_a",
    "QH2mito_a": "Reduced ubiquinol in astrocytic mito. matrix, #41, q10h2_m_a",
    "CytCredmito_a": "Reduced cytochrome c in astrocytic mito. matrix, #42, focytC_m_a",
    "O2_a": "Oxygen in astrocytic cytosol, #43, o2_c_a",
    "ATPmito_a": "Free ATP in astrocytic mito. matrix, #44, atp_m_a",
    "ADPmito_a": "Free ADP in astrocytic mito. matrix, #45, adp_m_a",
    "ATP_mx_a": "Magnesium-bound ATP in astrocytic mito. matrix, #46, notBigg_ATP_mx_m_a",
    "ADP_mx_a": "Magnesium-bound ADP in astrocytic mito. matrix, #47, notBigg_ADP_mx_m_a",
    "Pimito_a": "Phosphate in astrocytic mito. matrix, #48, pi_m_a",
    "ATP_i_a": "Free ATP in astrocytic mito. IMS, #49, atp_i_a",
    "ADP_i_a": "Free ADP in astrocytic mito. IMS, #50, adp_i_a",
    "amp_i_a": "#65",
    "ATP_mi_a": "Magnesium-bound ATP in astrocytic mito. IMS, #51, notBigg_ATP_mi_i_a",
    "ADP_mi_a": "Magnesium-bound ADP in astrocytic mito. IMS, #52, notBigg_ADP_mi_i_a",
    "Pi_i_a": "Phosphate in astrocytic mito. IMS, #53, pi_i_a",
    "MitoMembrPotent_a": "Astrocytic mitochondrial membrane potential, #54, notBigg_MitoMembrPotent_m_a",
    "notBigg_Ctot_m_a": "#70",
    "notBigg_Qtot_m_a": "#71",
    "h_i_a": "#72",
    "ATP_a": "ATP in astrocytic cytosol, #55, atp_c_a",
    # "placeholder1": ("74", ""),
    "FUMmito_a": "Fumarate in astrocytic mito., #56, fum_m_a",
    "MALmito_a": "L-Malate in astrocytic mito., #57, mal_L_m_a",
    "OXAmito_a": "Oxaloacetate in astrocytic mito., #58, oaa_m_a",
    "SUCmito_a": "Succinate in astrocytic mito., #59, succ_m_a",
    "SUCCOAmito_a": "Succinyl-CoA in astrocytic mito., #60, succoa_m_a",
    "CoAmito_a": "Coenzyme A in astrocytic mito., #61, coa_m_a",
    "AKGmito_a": "Alpha-ketoglutarate in astrocytic mito., #62, akg_m_a",
    "ca2_m_a": "#82",
    "ISOCITmito_a": "Isocitrate in astrocytic mito., #63, icit_m_a",
    "CITmito_a": "Citrate in astrocytic mito., #64, cit_m_a",
    "AcCoAmito_a": "Acetyl-CoA in astrocytic mito., #65, accoa_m_a",
    "acac_c_a": "#86",
    "aacoa_m_a": "#87",
    "PYRmito_a": "Pyruvate in astrocytic mito., #66, pyr_m_a",
    "GLN_n": "Glutamine in neuron, #67, gln_L_c_n",
    "GLN_out": "Glutamine in extracellular space, #68, gln_L_e_e",
    "GLN_a": "Glutamine in astrocytic cytosol, #69, gln_L_c_a",
    "glu_L_c_a": "#92",
    "Va": "Astrocytic membrane potential, #71, notBigg_Va_c_a",
    "Na_a": "Sodium ion in astrocytic cytosol, #72, na1_c_a",
    "K_a": "Potassium ion in astrocytic cytosol, #73, k_c_a",
    "K_out": "Potassium ion in extracellular space, #74, k_e_e",
    "glu_L_syn_syn": "#97",
    "notBigg_VNeu_c_n": "#98",
    "Na_n": "Sodium ion in neuronal cytosol, #77, na1_c_n",
    "h": "Gating variable h of Hodgkin-Huxley model in neuron, #78, notBigg_hgate_c_n",
    "n": "Gating variable n of Hodgkin-Huxley model in neuron, #79, notBigg_ngate_c_n",
    "Ca_n": "Calcium in neuronal cytosol, #80, ca2_c_n",
    "pgate": "Gating variable of M-current in neuron, #81, notBigg_pgate_c_n",
    "nBK_a": "Gating variable of BK channels in astrocyte, #82, notBigg_nBK_c_a",
    "mGluRboundRatio_a": "Ratio of bound metabotropic glutamate receptors in astrocyte, #83, notBigg_mGluRboundRatio_c_a",
    "IP3_a": "IP3 in astrocytic cytosol, #84, notBigg_IP3_c_a",
    "hIP3Ca_a": "Gating variable of IP3-dependent  calcium flow in astrocytic cytosol, #85, notBigg_hIP3Ca_c_a",
    "Ca_a": "Calcium in astrocytic cytosol, #86, ca2_c_a",
    "ca2_r_a": "#109",
    "sTRP_a": "Astrocytic TRPV4 channel open probability, #87, notBigg_sTRP_c_a",
    # "placeholder2": ("111", ""),
    "EET_a": "Epoxyeicosatrienoic acid, #89, notBigg_EET_c_a",
    "ddHb": "Deoxyhemoglobin, #90, notBigg_ddHb_b_b",
    "O2cap": "Oxygen in capillaries, #91, o2_b_b",
    "Glc_b": "D-Glucose in capillaries, #92, glc_D_b_b",
    "Glc_t_t": "D-Glucose in endothelium, #93, glc_D_ecsEndothelium_ecsEndothelium",
    "Glc_ecsBA": "D-Glucose in basal lamina, #94, glc_D_ecsBA_ecsBA",
    "Glc_a": "D-Glucose in astrocytic cytosol, #95, glc_D_c_a",
    "Glc_ecsAN": "D-Glucose in interstitial space, #96, glc_D_ecsAN_ecsAN",
    "Glc_n": "D-Glucose in neuronal cytosol, #97, glc_D_c_n",
    "G6P_n": "D-Glucose 6-phosphate in neuronal cytosol, #98, g6p_c_n",
    "G6P_a": "D-Glucose 6-phosphate in astrocytic cytosol, #99, g6p_c_a",
    "F6P_n": "D-Fructose 6-phosphate in neuronal cytosol, #100, f6p_c_n",
    "F6P_a": "D-Fructose 6-phosphate in astrocytic cytosol, #101, f6p_c_a",
    "FBP_n": "D-Fructose 1,6-bisphosphate in neuronal cytosol, #102, fdp_c_n",
    "FBP_a": "D-Fructose 1,6-bisphosphate in astrocytic cytosol, #103, fdp_c_a",
    "f26bp_a": "D-Fructose 2,6-bisphosphate in astrocytic cytosol, #104, f26bp_c_a",
    "GLY_a": "Glycogen in astrocytic cytosol, #105, glycogen_c_a",
    "amp_c_n": "#129",
    "amp_c_a": "#130",
    "G1P_a": "D-Glucose 1-phosphate in astrocytic cytosol, #106, g1p_c_a",
    "GAP_n": "Glyceraldehyde 3-phosphate in neuronal cytosol, #107, g3p_c_n",
    "GAP_a": "Glyceraldehyde 3-phosphate in astrocytic cytosol, #108, g3p_c_a",
    "DHAP_n": "Dihydroxyacetone phosphate in neuronal cytosol, #109, dhap_c_n",
    "DHAP_a": "Dihydroxyacetone phosphate in astrocytic cytosol, #110, dhap_c_a",
    "n13dpg_c_n": "#136",
    "n13dpg_c_a": "#137",
    "NADH_a": "NADH in astrocytic cytosol, #113, nadh_c_a",
    "pi_c_n": "#139",
    "pi_c_a": "#140",
    "n3pg_c_n": "#141",
    "n3pg_c_a": "#142",
    "n2pg_c_n": "#143",
    "n2pg_c_a": "#144",
    "PEP_n": "Phosphoenolpyruvate in neuronal cytosol, #118, pep_c_n",
    "PEP_a": "Phosphoenolpyruvate in astrocytic cytosol, #119, pep_c_a",
    "Pyr_n": "Pyruvate in neuronal cytosol, #120, pyr_c_n",
    "Pyr_a": "Pyruvate in astrocytic cytosol, #121, pyr_c_a",
    "Lac_b": "L-Lactate in capillaries, #122, lac_L_b_b",
    "Lac_ecs": "L-Lactate in extracellular space, #123, lac_L_e_e",
    "Lac_a": "L-Lactate in astrocytic cytosol, #124, lac_L_c_a",
    "Lac_n": "L-Lactate in neuronal cytosol, #125, lac_L_c_n",
    "NADPH_n": "NADPH in neuronal cytosol, #126, nadph_c_n",
    "NADPH_a": "NADPH in astrocytic cytosol, #127, nadph_c_a",
    "n6pgl_c_n": "#155",
    "n6pgl_c_a": "#156",
    "n6pgc_c_n": "#157",
    "n6pgc_c_a": "#158",
    "RU5P_n": "D-Ribulose 5-phosphate in neuronal cytosol, #132, ru5p_D_c_n",
    "RU5P_a": "D-Ribulose 5-phosphate in astrocytic cytosol, #133, ru5p_D_c_a",
    "R5P_n": "D-Ribose 5-phosphate in neuronal cytosol, #134, r5p_c_n",
    "R5P_a": "D-Ribose 5-phosphate in astrocytic cytosol, #135, r5p_c_a",
    "X5P_n": "D-Xylulose 5-phosphate in neuronal cytosol, #136, xu5p_D_c_n",
    "X5P_a": "D-Xylulose 5-phosphate in astrocytic cytosol, #137, xu5p_D_c_a",
    "S7P_n": "Sedoheptulose 7-phosphate in neuronal cytosol, #138, s7p_c_n",
    "S7P_a": "Sedoheptulose 7-phosphate in astrocytic cytosol, #139, s7p_c_a",
    "E4P_n": "D-Erythrose 4-phosphate in neuronal cytosol, #140, e4p_c_n",
    "E4P_a": "D-Erythrose 4-phosphate in astrocytic cytosol, #141, e4p_c_a",
    "GSH_n": "Reduced glutathione in neuronal cytosol, #142, gthrd_c_n",
    "GSH_a": "Reduced glutathione in astrocytic cytosol, #143, gthrd_c_a",
    "GSSG_n": "Oxidized glutathione in neuronal cytosol, #144, gthox_c_n",
    "GSSG_a": "Oxidized glutathione in astrocytic cytosol, #145, gthox_c_a",
    "creat_c_n": "#173",
    "PCr_n": "Phosphocreatine in neuronal cytosol, #146, pcreat_c_n",
    "creat_c_a": "#175",
    "PCr_a": "Phosphocreatine in astrocytic cytosol, #147, pcreat_c_a",
    "cAMP_a": "Cyclic AMP in astrocytic cytosol, #148, camp_c_a",
    "NE_neuromod": "Norepinephrine in extracellular space, #149, nrpphr_e_e",
    "udpg_c_a": "#179",
    "utp_c_a": "#180",
    "notBigg_GS_c_a": "#181",
    "GPa_a": "Active glycogen phosphorylase in astrocytic cytosol, #150, notBigg_GPa_c_a",
    "GPb_a": "Inactive glycogen phosphorylase in astrocytic cytosol]; #151, notBigg_GPb_c_a",
}


class _Idx:
    """Internal class used to build the singleton IMdx."""

    def __init__(self, mapping: Dict[str, str]):
        # store mapping (name -> (old_index, description))
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

    def as_list(self, idx_name: str | None = None, prefix: str = ""):
        if idx_name is None:
            return [f"{prefix}{name} ({getattr(self, name)}): {self._comments[name]}" for name in self._comments]
        return [f"{prefix}{name} ({getattr(self, name)}): {self._comments[name]}" for name in self._comments if idx_name in name]

    def __str__(self) -> str:
        return "\n".join(
            self.as_list(prefix="PIdx." if self is PIdx else "UIdx.")
        )


# singleton instance exported for module users
PIdx = _Idx(_PNAMES_WITH_COMMENTS)
# singleton instance exported for module users
UIdx = _Idx(_UNAMES_WITH_COMMENTS)

def index_info(idx_name: str | None = None, **_):
    """Print index information. If idx_name is None, prints all indexes.
    Otherwise prints indexes that partially match the name or old_index from both PIdx and UIdx (case-insensitive)."""
    if idx_name is None:
        print(PIdx)
        print()
        print(UIdx)
    else:
        search_term = idx_name.lower()
        pidx_matches = [name for name in PIdx._comments 
                       if search_term in name.lower() or search_term in PIdx._comments[name].lower()]
        uidx_matches = [name for name in UIdx._comments 
                       if search_term in name.lower() or search_term in UIdx._comments[name].lower()]
        
        if pidx_matches:
            for name in pidx_matches:
                comment = PIdx._comments[name]
                print(f"PIdx.{name} ({getattr(PIdx, name)}): {comment}")
        print()
        
        if uidx_matches:
            for name in uidx_matches:
                comment = UIdx._comments[name]
                print(f"UIdx.{name} ({getattr(UIdx, name)}): {comment}")
        
        if not pidx_matches and not uidx_matches:
            print(f"No matches found for '{idx_name}'")


if __name__ == "__main__":
    print("PIdx:")
    print(PIdx)
    print(f"Total: {PIdx.size}")
    print("UIdx:")
    print(UIdx)
    print(f"Total: {UIdx.size}")
