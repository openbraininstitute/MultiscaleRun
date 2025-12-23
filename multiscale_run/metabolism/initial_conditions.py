import numpy as np

from multiscale_run.metabolism.indexes import PIdx, UIdx


def make_u0() -> np.ndarray:
    """
    Build a u0 array with zeros and default hardcoded values.
    """
    u0 = np.zeros(UIdx.size)

    u0[UIdx.h_m_n] = 1.82084728579186e-05
    u0[UIdx.K_x_n] = 54.88513909303926
    u0[UIdx.mg2_m_n] = 0.6405401937956016
    u0[UIdx.NADHmito_n] = 0.3146584474671007
    u0[UIdx.QH2mito_n] = 0.015506712083093229
    u0[UIdx.CytCredmito_n] = 0.13185025457327085
    u0[UIdx.O2_n] = 0.03148650251580875
    u0[UIdx.ATPmito_n] = 0.7487433393982624
    u0[UIdx.ADPmito_n] = 1.8512566606017409
    u0[UIdx.ATP_mx_n] = 0.20845177459661043
    u0[UIdx.ADP_mx_n] = 1.129008031715835
    u0[UIdx.Pimito_n] = 17.22873019667985
    u0[UIdx.ATP_i_n] = 1.385172099080793
    u0[UIdx.ADP_i_n] = 0.057206724603648985
    u0[UIdx.amp_i_n] = 0.0
    u0[UIdx.ATP_mi_n] = 1.2787221400985913
    u0[UIdx.ADP_mi_n] = 0.05605499445123443
    u0[UIdx.Pi_i_n] = 19.999860977665755
    u0[UIdx.MitoMembrPotent_n] = 152.33918637408712
    u0[UIdx.notBigg_Ctot_m_n] = 2.7
    u0[UIdx.notBigg_Qtot_m_n] = 1.35
    u0[UIdx.h_i_n] = 3.981071705487114e-05
    u0[UIdx.ATP_n] = 1.3846374147608125
    u0[UIdx.FUMmito_n] = 0.07033038347789124
    u0[UIdx.MALmito_n] = 0.3877284278881228
    u0[UIdx.OXAmito_n] = 0.01133083263100033
    u0[UIdx.SUCmito_n] = 0.3913984292428137
    u0[UIdx.SUCCOAmito_n] = 0.002765202443496285
    u0[UIdx.CoAmito_n] = 0.0027278355391079485
    u0[UIdx.AKGmito_n] = 0.07302791984472035
    u0[UIdx.ca2_m_n] = 0.0001
    u0[UIdx.ISOCITmito_n] = 0.03312781257435126
    u0[UIdx.CITmito_n] = 0.3414510962627293
    u0[UIdx.AcCoAmito_n] = 0.040486317761993094
    u0[UIdx.AcAc_n] = 0.0008938613668892289
    u0[UIdx.AcAcCoA_n] = 3.471725572540322e-05
    u0[UIdx.PYRmito_n] = 0.04592802047818836
    u0[UIdx.bHB_n] = 0.002050830230641291
    u0[UIdx.bHB_ecs] = 0.002861722937272813
    u0[UIdx.bhb_c_a] = 0.002235
    u0[UIdx.bHB_b] = 0.2981203841045341
    u0[UIdx.asp_L_m_n] = 1.4
    u0[UIdx.asp_L_c_n] = 1.4
    u0[UIdx.glu_L_m_n] = 10.001887920296111
    u0[UIdx.mal_L_c_n] = 0.45
    u0[UIdx.oaa_c_n] = 0.01
    u0[UIdx.akg_c_n] = 0.2
    u0[UIdx.glu_L_c_n] = 10.000000420931526
    u0[UIdx.NADH_n] = 0.004140780436510287
    u0[UIdx.h_m_a] = 1.82084728579186e-05
    u0[UIdx.K_x_a] = 54.88513909303926
    u0[UIdx.Mg_x_a] = 0.6254020744170418
    u0[UIdx.NADHmito_a] = 0.3622495632039702
    u0[UIdx.QH2mito_a] = 0.010658928492490746
    u0[UIdx.CytCredmito_a] = 0.10755014489041778
    u0[UIdx.O2_a] = 0.03905865747239789
    u0[UIdx.ATPmito_a] = 0.8554395319513812
    u0[UIdx.ADPmito_a] = 1.7445604680486215
    u0[UIdx.ATP_mx_a] = 0.20827897454727567
    u0[UIdx.ADP_mx_a] = 1.1443189511420615
    u0[UIdx.Pimito_a] = 17.625288473162165
    u0[UIdx.ATP_i_a] = 1.29745793823728
    u0[UIdx.ADP_i_a] = 0.044346699541431896
    u0[UIdx.amp_i_a] = 0.0
    u0[UIdx.ATP_mi_a] = 1.1823280190768068
    u0[UIdx.ADP_mi_a] = 0.04362949589266071
    u0[UIdx.Pi_i_a] = 19.999931107524688
    u0[UIdx.MitoMembrPotent_a] = 155.39201516889315
    u0[UIdx.notBigg_Ctot_m_a] = 2.7
    u0[UIdx.notBigg_Qtot_m_a] = 1.35
    u0[UIdx.h_i_a] = 3.981071705487114e-05
    u0[UIdx.ATP_a] = 1.2971907639974427
    u0[UIdx.FUMmito_a] = 0.05005917725596374
    u0[UIdx.MALmito_a] = 0.25524996956098295
    u0[UIdx.OXAmito_a] = 0.004468226870983686
    u0[UIdx.SUCmito_a] = 0.5865999694835419
    u0[UIdx.SUCCOAmito_a] = 0.0016699868314113365
    u0[UIdx.CoAmito_a] = 0.002541368839174815
    u0[UIdx.AKGmito_a] = 0.015159157992632254
    u0[UIdx.ca2_m_a] = 0.0001
    u0[UIdx.ISOCITmito_a] = 0.0360692382798456
    u0[UIdx.CITmito_a] = 0.358985824746709
    u0[UIdx.AcCoAmito_a] = 0.004288644329412937
    u0[UIdx.acac_c_a] = 0.00312
    u0[UIdx.aacoa_m_a] = 0.0006
    u0[UIdx.PYRmito_a] = 0.012983253151168756
    u0[UIdx.GLN_n] = 0.40016780751134395
    u0[UIdx.GLN_out] = 0.19991032677727677
    u0[UIdx.GLN_a] = 0.24979819268840564
    u0[UIdx.glu_L_c_a] = 0.2994675379035365
    u0[UIdx.Va] = -94.73739998434871
    u0[UIdx.Na_a] = 16.27886560396611
    u0[UIdx.K_a] = 100.79307843484172
    u0[UIdx.K_out] = 3.1104211426858464
    u0[UIdx.glu_L_syn_syn] = 2.5e-05
    u0[UIdx.notBigg_VNeu_c_n] = -68.00932293426199
    u0[UIdx.Na_n] = 8.473759755301563
    u0[UIdx.h] = 0.9811237297560305
    u0[UIdx.n] = 0.03467357454611763
    u0[UIdx.Ca_n] = 5.436689205733492e-05
    u0[UIdx.pgate] = 0.03553923881632591
    u0[UIdx.nBK_a] = 7.45614720951229e-06
    u0[UIdx.mGluRboundRatio_a] = 0.0
    u0[UIdx.IP3_a] = 1.1852340589842885e-06
    u0[UIdx.hIP3Ca_a] = 0.6531565346093099
    u0[UIdx.Ca_a] = 5.31000955574647e-05
    u0[UIdx.ca2_r_a] = 0.4
    u0[UIdx.sTRP_a] = 0.00124697236672799
    u0[UIdx.EET_a] = 3.143871670033718e-05
    u0[UIdx.ddHb] = 0.05852770291944967
    u0[UIdx.O2cap] = 7.105220869902977
    u0[UIdx.Glc_b] = 4.555436497117541
    u0[UIdx.Glc_t_t] = 1.4036921120261527
    u0[UIdx.Glc_ecsBA] = 1.302331013714969
    u0[UIdx.Glc_a] = 1.2215129412034003
    u0[UIdx.Glc_ecsAN] = 1.0034276408975709
    u0[UIdx.Glc_n] = 0.9117230433328605
    u0[UIdx.G6P_n] = 0.04518031109219087
    u0[UIdx.G6P_a] = 0.06142242564901545
    u0[UIdx.F6P_n] = 0.007367188108993513
    u0[UIdx.F6P_a] = 0.010139153003705685
    u0[UIdx.FBP_n] = 0.009458862178707486
    u0[UIdx.FBP_a] = 0.029976744727305948
    u0[UIdx.f26bp_a] = 0.012169896922510802
    u0[UIdx.GLY_a] = 13.99969995417289
    u0[UIdx.amp_c_n] = 1e-05
    u0[UIdx.amp_c_a] = 1e-05
    u0[UIdx.G1P_a] = 0.012811280361731594
    u0[UIdx.GAP_n] = 0.0012351454067088853
    u0[UIdx.GAP_a] = 0.0022568560606488503
    u0[UIdx.DHAP_n] = 0.003220803533622665
    u0[UIdx.DHAP_a] = 0.0037897580104066415
    u0[UIdx.n13dpg_c_n] = 0.0060805407271592475
    u0[UIdx.n13dpg_c_a] = 0.008030562619956915
    u0[UIdx.NADH_a] = 0.10927809092221007
    u0[UIdx.pi_c_n] = 20.0
    u0[UIdx.pi_c_a] = 20.0
    u0[UIdx.n3pg_c_n] = 0.01765067153478949
    u0[UIdx.n3pg_c_a] = 0.021463604134103274
    u0[UIdx.n2pg_c_n] = 0.00196123874550032
    u0[UIdx.n2pg_c_a] = 0.0023600313501276823
    u0[UIdx.PEP_n] = 0.0011299114036925676
    u0[UIdx.PEP_a] = 0.0013498159787353333
    u0[UIdx.Pyr_n] = 0.09884562894707946
    u0[UIdx.Pyr_a] = 0.029482442303259512
    u0[UIdx.Lac_b] = 0.6887631395085969
    u0[UIdx.Lac_ecs] = 0.6223377821910432
    u0[UIdx.Lac_a] = 0.6224222941358745
    u0[UIdx.Lac_n] = 0.62189156291357
    u0[UIdx.NADPH_n] = 0.030030028188024867
    u0[UIdx.NADPH_a] = 0.03000617948372434
    u0[UIdx.n6pgl_c_n] = 2.7223858669789458e-06
    u0[UIdx.n6pgl_c_a] = 3.019823774010181e-06
    u0[UIdx.n6pgc_c_n] = 0.0026154588421574165
    u0[UIdx.n6pgc_c_a] = 0.001825222802612153
    u0[UIdx.RU5P_n] = 0.0005499402428921933
    u0[UIdx.RU5P_a] = 0.0006682285740983806
    u0[UIdx.R5P_n] = 1.564984868864245e-05
    u0[UIdx.R5P_a] = 2.6065883215538542e-05
    u0[UIdx.X5P_n] = 0.016834424262979618
    u0[UIdx.X5P_a] = 0.020470510408354833
    u0[UIdx.S7P_n] = 0.019807839436742886
    u0[UIdx.S7P_a] = 0.24954311556796605
    u0[UIdx.E4P_n] = 0.006632954456360935
    u0[UIdx.E4P_a] = 0.006138869748662782
    u0[UIdx.GSH_n] = 1.200006238770546
    u0[UIdx.GSH_a] = 4.300000202932421
    u0[UIdx.GSSG_n] = 0.0119968806147281
    u0[UIdx.GSSG_a] = 0.04299989853382339
    u0[UIdx.creat_c_n] = 5.053977657681814
    u0[UIdx.PCr_n] = 4.98986852470732
    u0[UIdx.creat_c_a] = 5.0757940916174356
    u0[UIdx.PCr_a] = 4.927691727614907
    u0[UIdx.cAMP_a] = 0.039182703258954135
    u0[UIdx.NE_neuromod] = 0.0
    u0[UIdx.udpg_c_a] = 0.109
    u0[UIdx.utp_c_a] = 0.23
    u0[UIdx.notBigg_GS_c_a] = 0.0029999
    u0[UIdx.GPa_a] = 0.0013314628973952977
    u0[UIdx.GPb_a] = 0.06866853710260439

    # u0[UIdx.placeholder0] = 0.047784 #24
    # u0[UIdx.placeholder1] = 0.045 #74
    # u0[UIdx.placeholder2] = 0.0237000024973173 #111

    return u0

def make_parameters() -> np.ndarray:
    p0 = np.zeros(PIdx.size)

    p0[PIdx.notBigg_FinDyn_W2017] = 0.0001
    p0[PIdx.notBigg_Fout_W2017] = 0.0001
    p0[PIdx.notBigg_vV_b_b] = 0.023
    return p0


def override(v, cls, subs):
    for key, value in subs.items():
        v[getattr(cls, key)] = value