# for the moment, let's not complain for never used vars
# ruff: noqa: F841
import inspect
from dataclasses import dataclass, fields, is_dataclass


@dataclass
class ATDMP:
    qAK: float = 0.92
    vATPasesn: float = 0.0  # 0.0033489929892437376 #0.003348829040159755 #0.010188268272998515 # 0.0 # 0.5*0.1388 #0.0832     % mmol/L/sec
    vATPasesg: float = 0.0  # 0.5*0.1351 #0.1061     % mmol/L/sec
    ATDPtot_n: float = 1.4449961078157665  # 1.4482032555861983
    ATDPtot_a: float = 1.3434724532826217  # 1.3452032555861981

    # ADK
    # check DiNuzzo PMID: 19888285 and ref there adenylate kinase (Rapoport et al, 1976)
    # Winter2017, Lambeth 2002, JayGliaExpand

    # psiADK_n(ATP_n,AMP_n,ADP_n), ATP_n + AMP_n + MET_h_c_n ⇒ 2ADP_n

    Vmaxfadk_n: float = 1.0  # 14.67  #kcat_fadk_n = 14018.6 #Vmaxfadk 14.67

    KmADPADK_n: float = 0.35  # KADPADK_n
    KmATPADK_n: float = 0.27  # KATPADK_n
    KmAMPADK_n: float = 0.32  # KAMPADK_n
    KeqADK_n: float = 2.21

    # psiADK_n1 = ((Vmaxfadk_n*(ATP_n0*AMP_n0)/(KmATPADK_n*KmAMPADK_n) - (((Vmaxfadk_n*(KmADPADK_n^2)) / (KmATPADK_n*KmAMPADK_n*KeqADK_n))*(((ADP_n0)^2)/(KmADPADK_n^2)))) / (1 + ATP_n0/KmATPADK_n + AMP_n0/KmAMPADK_n + (ATP_n0*AMP_n0)/(KmATPADK_n*KmAMPADK_n) + (2*ADP_n0)/KmADPADK_n + ((ADP_n0)^2)/(KmADPADK_n^2)))

    ############################################

    # ADK
    # check DiNuzzo PMID: 19888285 and ref there adenylate kinase (Rapoport et al, 1976)
    # Winter2017, Lambeth 2002, JayGliaExpand

    # psiADK(ATP_a,AMP_a,ADP_a), ATP_a + AMP_a + MET_h_c_a ⇒ 2ADP_a

    Vmaxfadk_a: float = 14.67  # kcat_fadk_a = 14018.6 #Vmaxfadk 14.67

    KmADPADK_a: float = 0.35  # KADPADK
    KmATPADK_a: float = 0.27  # KATPADK
    KmAMPADK_a: float = 0.32  # KAMPADK
    KeqADK_a: float = 2.21

    # psiADK_a1 = ((Vmaxfadk_a*(ATP_a0*AMP_a0)/(KmATPADK_a*KmAMPADK_a) - (((Vmaxfadk_a*(KmADPADK_a^2)) / (KmATPADK_a*KmAMPADK_a*KeqADK_a))*(((ADP_a0)^2)/(KmADPADK_a^2)))) / (1 + ATP_a0/KmATPADK_a + AMP_a0/KmAMPADK_a + (ATP_a0*AMP_a0)/(KmATPADK_a*KmAMPADK_a) + (2*ADP_a0)/KmADPADK_a + ((ADP_a0)^2)/(KmADPADK_a^2)))

    ############################################

    # AC and NEneuromod

    # # ATP_a ⇒  cAMP_a + PPi_a + MET_h_c_a

    # # From J. Biol. Chem.-1997-Dessauer-27787-95.pdf

    # VmaxfAC_a = 3.0 #kcat_fAC_a = 109151.4 #VmaxfAC 3.0 #30.0
    # KmACATP_a = 0.34 # KACATP
    # KicAMPAC_a = 2.3

    # VmaxrAC_a = 0.1 #kcat_rAC_a = 3638.4 #VmaxrAC_a  0.1 #1.0
    # KmpiAC_a = 0.31 #0.12 # KpiAC
    # KmcAMPAC_a = 2.3 # KcAMPAC

    # VmaxfAC_a = 0.3 #3.0 #kcat_fAC_a = 109151.4 #VmaxfAC 3.0 #30.0
    # KmACATP_a = 0.4 # 0.34 # KACATP
    # KicAMPAC_a = 0.045 #2.3

    # VmaxrAC_a = 0.01 #0.1 #kcat_rAC_a = 3638.4 #VmaxrAC_a  0.1 #1.0
    # KmpiAC_a = 0.01 #0.31 #0.12 # KpiAC
    # KmcAMPAC_a = 2.0 #2.3 # KcAMPAC

    # VmaxfAC_a = 0.3 #3.0 #kcat_fAC_a = 109151.4 #VmaxfAC 3.0 #30.0
    # KmACATP_a = 0.4 # 0.34 # KACATP
    # KicAMPAC_a = 0.04533 #0.045 #0.0465 #2.3

    # 0.045 -> -2.2e-7
    # 0.0453  -> -1.783216198374761e-8
    # 0.0454 -> 4.93348351140038e-8
    # 0.0456  -> 1.8329278509024457e-7
    # 0.046 -> 4.4971786195144035e-7

    # VmaxrAC_a = 0.01 #0.1 #kcat_rAC_a = 3638.4 #VmaxrAC_a  0.1 #1.0
    KmpiAC_a: float = 0.01  # 0.31 #0.12 # KpiAC
    # KmcAMPAC_a = 2.0 #2.3 # KcAMPAC

    #
    VmaxfAC_a: float = 0.003  # 3.0 #kcat_fAC_a = 109151.4 #VmaxfAC 3.0 #30.0
    KmACATP_a: float = 0.8  # 0.34 # 0.34 # KACATP
    KicAMPAC_a: float = 0.045  # 0.256 #0.04533 #0.045 #0.0465 #2.3

    VmaxrAC_a: float = 0.0001  # 0.1 #kcat_rAC_a = 3638.4 #VmaxrAC_a  0.1 #1.0
    KmcAMPAC_a: float = 0.4  # 2.7 #8.8 #2.3 #8.8 #2.7 #2.0 #2.3 # KcAMPAC

    # Adenylate cyclase ATP ⇒ cAMP + Pi #Ppi
    # assuming competitive inh by cAMP in f dir
    # psiAC(ATP_a,cAMP_a,Pi_a) = (a[11]/cai0_ca_ion)*( ((kcat_fAC_a*concentration_enzyme_transporter_AC_a*ATP_a/(KmACATP*(1+cAMP_a/KicAMPAC)) - kcat_rAC_a*concentration_enzyme_transporter_AC_a*cAMP_a*PPi_a/(KmpiAC*KmcAMPAC))/(1 + ATP_a/(KmACATP*(1+cAMP_a/KicAMPAC) )+ cAMP_a/KmcAMPAC + (cAMP_a*PPi_a)/(KmcAMPAC*KmpiAC) + PPi_a/KmpiAC))  )

    # # without cai for optimiz but with PPi_a instead of Pi_a for gem
    # psiAC_a1 = ((VmaxfAC_a*ATP_a0/(KmACATP_a*(1+cAMP_a0/KicAMPAC_a)) - VmaxrAC_a*cAMP_a0*PPi_a0/(KmpiAC_a*KmcAMPAC_a))/(1 + ATP_a0/(KmACATP_a*(1+cAMP_a0/KicAMPAC_a) )+ cAMP_a0/KmcAMPAC_a + (cAMP_a0*PPi_a0)/(KmcAMPAC_a*KmpiAC_a) + PPi_a0/KmpiAC_a))

    # #psiAC(NE_neuromod,ATP_a,cAMP_a,PPi_a)


@dataclass
class BfInput:
    # vV dyn BF Winter 2017
    F_0: float = 0.012
    delta_F: float = 0.42

    tau_v: float = 35.0

    t_0: float = 200.0
    t_fin: float = 20.0  # 40.0 # global_par_t_en_D

    t_1: float = 2.0

    C_O_a: float = 8.34  # 7.78346 #8.34 #9.14 #Calvetti # 8.35 Jlv # 8.34 #Winter2017 # C_O_a:7.78346 in opt: 202110220825

    # PScap = 10.
    PScapA: float = 0.8736  # 0.2175 #Jolivet #10. Winter
    PScapNAratio: float = 1.9  # 3.8
    # PScapN = PScapNAratio*PScapA #0.747 #Jolivet #40.5 # Winter
    KO2b: float = 0.0361
    HbOP: float = 8.6
    param_degree_nh: float = 2.73  # param_degree_JO2 = 1/param_degree_nh


@dataclass
class Creatine:
    # Calvetti2018
    # # psiCrKinase_n(Cr_n,ATP_n,ADP_n,PCr_n), Cr_n + ATP_n ⇒ ADP_n + PCr_n + MET_h_c_n

    # V_Cr_n = 10.0 #16666.67  #kcat_Cr_n = 935138.5 #V_Cr_n  16666.67
    # mu_Cr_n = 0.01
    # Km_Cr_n = 495.0

    # V_PCr_n = 10.0 #16666.67   #kcat_PCr_n = 935138.5 #V_PCr_n  16666.67
    # mu_PCr_n = 100.0
    # Km_PCr_n = 528.0

    # # psiCrKinase_n1 = V_Cr_n  * (Cr_n0 / (Cr_n0 + Km_Cr_n)) * ( (ATP_n0/ADP_n0)/ ( mu_Cr_n + ATP_n0/ADP_n0 )) - ( V_PCr_n * (PCr_n0 / (PCr_n0 + Km_PCr_n)) * ( ADP_n0/ATP_n0 ) / ( mu_PCr_n + ADP_n0/ATP_n0 ) )

    # #######################################################

    # #psiCrKinase_a(Cr_a,ATP_a,ADP_a,PCr_a), Cr_a + ATP_a ⇒ ADP_a + PCr_a + MET_h_c_a

    # V_Cr_a = 10.0 #16666.67 #kcat_Cr_a = 668433.5 #V_Cr_a  16666.67
    # mu_Cr_a = 0.01 # par[281]
    # Km_Cr_a = 495.0 # par[282]

    # V_PCr_a = 10.0 #16666.67 #kcat_PCr_a = 668433.5 #V_PCr_a  16666.67
    # mu_PCr_a = 100.0
    # Km_PCr_a = 528.0

    # # psiCrKinase_a1 = V_Cr_a * (Cr_a0 / (Cr_a0 + Km_Cr_a)) * ( (ATP_a0/ADP_a0) / ( mu_Cr_a + ATP_a0/ADP_a0 ))  -  (V_PCr_a * (PCr_a0 / (PCr_a0 + Km_PCr_a)) * ( ADP_a0/ATP_a0 ) / ( mu_PCr_a + ADP_a0/ATP_a0 ))

    # Jolivet2015 + opt par
    Crtot: float = 10.0  # 5.0 #10.0 in Jlv

    kCKnps: float = 0.0214016075483191  # 0.027854224286550353
    # kCKnms = 0.0008979238618658251

    kCKgps: float = 0.00178189983486018  # 0.00178189983486018 #0.0003859785697371309
    # kCKgms = 1.2499574733414296e-5

    # creatine upd for better opt:
    # kCKnms -> KeqCKnpms*kCKnps
    # kCKgms -> KeqCKgpms*kCKgps

    # psiCrKinase_n1(PCr_n,ATP_n,ADP_n)  =  kCKnps*PCr_n*ADP_n - KeqCKnpms*kCKnps*(Crtot - PCr_n)*ATP_n # kCKnps*PCr_n*ADP_n - kCKnms*(Crtot - PCr_n)*ATP_n
    # psiCrKinase_a1(PCr_a,ATP_a,ADP_a)  =  kCKgps*PCr_a*ADP_a - KeqCKgpms*kCKgps*(Crtot - PCr_a)*ATP_a # kCKgps*PCr_a*ADP_a - kCKgms*(Crtot - PCr_a)*ATP_a

    KeqCKnpms: float = 0.04265840286184623  # 0.0453633356986354 #0.03223654166881234 #0.0008979238618658251/0.027854224286550353 #kCKnms/kCKnps
    KeqCKgpms: float = 0.034  # KeqCKgpms = 0.0375 #0.0283089638639555 #0.032384115889975654 #1.2499574733414296e-5/0.0003859785697371309 #kCKgms/kCKgps
    # ini: 0.032236541668812340.032384115889975654


@dataclass
class Ephys:
    # # Na/K-ATPase
    # kPumpn  =   2.49e-06       # cm (mmol/L)-1 sec-1
    # kPumpg  =   4.64e-07       # cm (mmol/L)-1 sec-1
    KmPump: float = 0.5  # mmol/L
    # vPumpg0 =   0.0708         # mmol/L sec-1

    SmVn: float = 2.5e04  # cm-1
    SmVg: float = 2.5e04  # cm-1
    # gNan    =   0.0155         # mS cm-2
    # gNag    =   0.00623        # mS cm-2

    # Ratio of excitatory conductance
    glia: float = 50.0  # mV
    #
    # Neuronal parameters
    Cm: float = 1e-03  # mF/cm2
    gL: float = 0.02  # mS/cm2

    gNa: float = 56.0  # 40.0             # mS/cm2
    gK: float = 6.0  # 18.0             # mS/cm2
    g_M: float = 0.075  # not Jlv, enzymes/enzymes_preBigg/gen_mix.ipynb

    gCa: float = 0.02  # mS/cm2
    gmAHP: float = 6.5  # mS/cm2
    KD: float = 30e-03  # mmol/L
    tauCa: float = 150e-03  # sec
    Ca0: float = 0.5e-04  # mmol/L
    EK: float = -80.0  # mV
    ECa: float = 120.0  # mV
    Ee: float = 0.0  # mV
    Ei: float = -80.0  # mV
    phi: float = 4.0  # phih         #
    # phin : float   =   4.0              #
    ##

    kPumpn: float = 2.2e-06
    gNan: float = 0.0136
    gNag: float = 0.0061
    gKpas: float = 0.04  # 0.05 #0.2035  ############
    kPumpg: float = 4.5e-07
    vPumpg0: float = 0.0687

    gKn: float = 0.05  # approx between Calv, Jlv, enzymes/enzymes_preBigg/gen_mix.ipynb
    gKg: float = 0.05  # approx between Calv, Jlv, enzymes/enzymes_preBigg/gen_mix.ipynb

    # qAK  = 0.92
    # A    = 2.212                                           # mmol/L

    tau_max: float = 0.6  # not jlv, approx ms-s, 608ms /enzymes/enzymes_preBigg/gen_mix.ipynb

    RateDecayK_a: float = 0.07

    ImaxNaKa: float = 1.45
    INaKaKThr: float = 20.0  # 16 is estim in W2013 # !!!!!!!!!!!!
    INaKaNaThr: float = 30.0  # 1 is estim in W2013 # !!!!!!!!!!!!

    VKirAV: float = 31.15

    VKirS: float = 26.8

    VleakA: float = -40.0

    ###
    VprodEET_a: float = 72.0
    kdeg_EET_a: float = 7.1
    CaMinEET_a: float = 5e-5  # 5e-6 #1e-4  # !!!!!!!!!!!!
    EETshift: float = 2000.0  # mV 4.0 mV is [EET]*EETshift  #0.002  # 2. # approx  # !!!!!!!!!!!!

    Ca3BK: float = 0.0004
    Ca4BK: float = 0.00015

    v4BK: float = 14.5
    v5BK: float = 8.0
    v6BK: float = -13.0

    psiBK: float = 2.664  # 0.02 #  !!!!!!!!!!!!

    EBK: float = -80.0  # -95. # !!!!!!!!!!!!

    KGlutSyn: float = 4.0  # 8.82  ###########
    deltaGlutSyn: float = 0.001235
    rhIP3a: float = 0.0048
    kdegIP3a: float = 1.25

    konhIP3Ca_a: float = 2000.0  # 2e-3 # 2
    khIP3Ca_aINH: float = 1e-4
    Pleak_CaER_a: float = 1e-3  # 2.5e-3 #5.2e-3 # # !!!!!!!!!!!!

    beta_Ca_a: float = 0.025  # 0.0244              #in W2013 !!!!!!!!!!!

    VCa_pump_a: float = 0.055  # 0.05worked #0.02  # !!!!!!!!!!!!
    KpCa_pump_a: float = 0.00019  # 0.000192

    ImaxIP3_a: float = 1.0  # 2.88 in W2013 !!!!!!!!!!!
    KIIP3_a: float = 1e-5  # 3.0e-5 in W2013 !!!!!!!!!!!
    KCaactIP3_a: float = 0.00017

    Ca_perivasc: float = 5.0e-3
    tauTRPCa_perivasc: float = 20.0  # 1.5 #2.0 #0.9 #in W2013 !!!!!!!!!!!

    VTRP: float = 6.0

    r0TRPVsinf: float = 0.0237  # 0.23wwithe2TRPVsinf = 0.25 #0.032w with e2TRPVsinf = 0.1 #0.034f #0.032w #0.03 # 0.0237  # !!!!!!!!!!!!

    # eTRPVsinf : float= ((rTRPVsinf-r0TRPVsinf)/r0TRPVsinf)
    e2TRPVsinf: float = 0.046  # 0.045 #0.05f #0.04r #0.06f #0.02r #0.025 #0.1w
    kTRPVsinf: float = 0.101  # 0.102r #0.1 # !!!!!!!!!!!!

    gammaCaaTRPVsinf: float = 5e-5  # 5e-5worked #5.0e-7  #1e-6 #1e-5 #5.0e-5 # 0.2uM in W2012 # 0.01uM in W2013 !!!!!!!!!!!
    gammaCapTRPVsinf: float = 0.32  # w # 0.3r #0.35 #w  #0.2worked
    v1TRPsinf_a: float = 120.0
    v2TRPsinf_a: float = 13.0

    epsilon: float = (
        1.0  # 9.33 # 1/s # Calvetti2018 #epsilon=1.333333333 # Cressman2011 # 1.2 Cressman2009
    )
    mu_glia_ephys: float = 0.1  # 0.01  #0.1 # Calvetti2018
    # mu_pump_ephys = 0.1

    kbath: float = 4.0  # 6.3 #4.0 # #kbath=4.0 Cressman2011 #3. CapoRangel ... Calvetti2019 #5.03 #4.2 #6.3 # mM # Calvetti2018

    gamma: float = 5.99  # but gamma-ephys isn't in use, because different ephys model in the end gamma is only used for mito-ETC functions #5. #0.045
    glia_c: float = 30.0  # 20.75 # mM/s # Calvetti2018 #glia=66.666666666 # Cressman2011

    Na_n2_baseNKA: float = (
        18.0  # 15.5 #15.7 #10.0 #14.70 # 18                                # Jglia
    )

    K_n_Rest: float = 120.0  # 130. #140.0
    # Na_ecs_Rest : float= 130. #140. #144.0
    Na_n_Rest: float = 8.0  # 9.5 #10.5 #9.5 #10.5 #8. #10. #10.5

    # Jolivet conc
    Na_out: float = 150.0  # 153.5 #
    # Na_n0 : float= 8.5
    # Na_a0 : float= 15.

    synInput: float = 1e-12

    gbar: float = 7.8e-06  # mS cm-2 sec
    finf: float = 3.5  # Hz
    f0: float = 32  # Hz
    tau: float = 2.5
    Ne: float = 240.0

    # synaptic glutamate
    amplGR: float = 1.1  # 25.
    tauG: float = 2.0  # 2.7
    KsynGlutPulse: float = 0.4  # 8.8

    def __post_init__(self):
        self.gKirV: float = 6.75 * self.gKpas  # 0.1*2* #7*gKpas
        self.gKirS: float = 40 * self.gKpas  # 4*gKpas # 0.1* #40*gKpas
        self.gleakA: float = self.gKpas  # 0.1*
        self.gBK: float = 54.0 * self.gKpas  # 200. ##1000*gKpas # 200. #0.2 # 200pS  # !!!!!!!!!!!!
        self.gTRP: float = (
            10 * self.gKpas
        )  # w  #11.5*gKpas #10*gKpas worked #13.5*gKpas  # 1e-5* !!!!!!!!!!!!


@dataclass
class ETC:
    # diff from Theurey2019:

    # ADTPtot total Adenosine phosphates in cytosol  # needs opt
    # state_fact # needs opt
    # Init[7] # O2  # Theurey2019 works with my O2

    # ADTP_tot_n    = 1.448e-3 #    #1e-3*(ATP_n0 + ADP_n0) #2.6e-3  # total Adenosine phosphates in cytosol, calculated from Evans_77
    # state_fact  = 0.967  #10/11      #ATP_n0/(ATP_n0 + ADP_n0)  #10/11

    # ATP_e       = state_fact*ADTP_tot  # ini ATP level
    # ADP_e       = ADTP_tot-ATP_e       # ini ADP level

    ######################################################

    # fixed par
    etcF: float = 0.096484  # kJ mol^{-1} mV^{-1}
    etcR: float = 8314e-6  # Universal gas constant (kJ * mol^{-1} * K^{-1}]
    etcT: float = 273.15 + 37  # Temperature (K), 37 degree

    dG_C1o: float = -69.37  # kJ mol^{-1}
    dG_C3o: float = -32.53  # kJ mol^{-1}
    dG_C4o: float = -122.94  # kJ mol^{-1}
    dG_F1o: float = 36.03  # kJ mol^{-1}
    n_A: float = 3.0  # numbers of proteins used by ATP synthase

    # concentrations and pH
    # pH_e    = 7.4            # External pH (cytosol)
    # H_e     = 10^(-pH_e)  == C_H_cyt_n   #  cytosolic hydrogen concentration (Molar)
    K_i: float = 120e-3  # K_i IM potassium-concentration
    Mg_tot: float = 20e-3  # Mg_tot  IM magnesium-concentration
    # Pi_e    = 20e-3          # Pi_e    IM phosphate-concentration

    NADtot: float = 726e-6  # NADtot mito
    # Ctot0       = 2.70e-3    # Cyt-c (total IMS Cyt-C, Cred+Cox, M]  # Cyt-c from Beard. Total IMS Cyt-c, Cred+Cox, molar
    # Qtot0       = 1.35e-3    # total IMS Ubiquinol, Q+QH2, M

    W_c: float = (
        1 / 0.0575
    )  # Volume fraction cytosol/mitochondria # 0.0575 is mito vol fraction from supp of Santuy2018 doi: 10.1093/cercor/bhy159 #1/0.06 0.06 is mitochondrial fraction Ward 2007
    W_m: float = 0.143 / 0.20  # mitochondrial water space (ml water / ml mito]

    # Potassium-Hydrogen-Antiport
    x_KH: float = 2.9802e7  # x_KH      # K+ / H+ antiporter activity

    # Matrix buffer and membrane capacitance
    CIM: float = 6.7568e-6  # CIM       # Inner Membrane capacitance

    # c_inc   = 1               # Cyt-c after release set to 0.1#
    # t12cyto = 90                       # cyt-c release half time Waterhouse 2000 (seconds)
    # Cfin    = Ctot0*W_i/W_c*c_inc      # final cytochrome c after release in IMS given by re-equilibration of the
    # IMS water space with the rest of the cell (0.1#)
    # c_inc is used to modify OXPHOS-contributing cyt-c after release

    # potassium uniporter and adenylate kinase neglected
    x_K: float = 0  # Passive potassium transporter activity
    x_AK: float = 0  # AK activity
    K_AK: float = 0  # Adenelyte Kinase switched off

    # Parameters for complex I
    x_C1 = 1.0200e003  # x_C1       # Complex I activity

    # Parameters for complex III
    x_C3: float = 0.2241  # x_C3      # Complex III activity
    k_Pi3: float = 0.192e-3  # k_Pi3     # Complex III / Pi parameter
    k_Pi4: float = 25.31e-3  # k_Pi4     # Complex III / Pi parameter

    # Parameters for complex IV
    x_C4: float = 3.2131e-004  # x_C4      # Complex IV activity
    k_O2: float = 1.2e-4  # k_O2      # kinetic constant for complex IV M

    # Parameters for OM transporters
    gamma: float = 5.99  # gamma     # MOM area per unit volume micron^{-1}
    x_A: float = 85.0  # x_A       # MOM permeability to nucleotides (micron s^{-1})
    x_Pi2: float = 327.0  # x_Pi2     # MOM permeability to phosphate (micron s^{-1})

    # Phosphate-Hydrogen-Cotransport
    k_dHPi: float = 10 ** (-6.75)  # k_dHPi    # H/Pi co-transpor Molar form factor 1 binding
    k_PiH: float = (
        0.45082e-3  # k_PiH     # H+/Pi co-transport activity form factor 2 Michaelis constant
    )
    x_Pi1: float = 3.85e5  # x_Pi1     # H+/Pi co-transport activity

    # Parameters for ATP synthase and Mg-binding to ATP?ADP
    x_MgA: float = 1e6  # x_MgA     # Mg2+ binding activity

    # Parameters for input function
    k_Pi1: float = 0.13413e-3  # k_Pi1      # Dehydrogenase flux input
    k_Pi2: float = 0.677e-3  # k_Pi2      # Dehydrogenase flux input

    ######################################################

    # Proton leak activity
    x_Hle: float = 149.61265600173826  # 150.0               # x_Hle     # Proton leak activity
    x_Ht: float = 2044.5370854408536  # 2000.0               # x_Ht      # MOM permeability to protons (micron s^{-1})

    # adj for eq: 0.9654561819314937
    r_DH: float = 4.35730398512522  # 4.3          # r_DH       # Input-flux: Initial disturbance of equilibrium

    x_buff: float = 1437.0652678883314  # 200/(0.5*T2Jcorrection) # #100                 # x_buff    # Inner Matrix hydrogen buffer capacity

    # optimised parameters

    # Parameters for input function
    x_DH: float = 0.0478558445772299  # 0.04702218860608453 #0.05896      # x_DH       # Dehydrogenase activity

    # Parameters for Adenosine Transferase
    x_ANT: float = (
        0.0647001029937813  # 0.07649900124686723 #0.0020              # x_ANT     # ANT activity
    )
    k_mADP: float = 1.03045032866899e-05  # 1.0588243052994988e-5 #3.50e-6             # k_mADP    # ANT Michaelis-Menten constant

    # Cytosolic ATP production and consumption
    # K_ADTP_dyn = 0.5912763309268644 #3.42      # K_ADTP_dyn Cytosolic ATP production
    # x_ATPK   = 0.30499319022776666 # 0.504    # x_ATPK
    # K_ADTP_cons = 1.1895556584725608 #1.0     # K_ADTP_cons Cytosolic ATP consumption

    # Parameters for ATP synthase and Mg-binding to ATP?ADP
    x_F1: float = (
        7099.66908851658  # 6912.715469614502 #6829.4        # x_F1      # F1Fo ATPase activity
    )
    K_DT: float = 0.00166023273526023  # 0.001855689326651793 #0.000192             # K_DT      # Mg/ATP binding constant (M)
    K_DD: float = 0.000409766157053928  # 0.00036972016989755054 #347e-6              # K_DD      # Mg/ADP binding constant (M)

    ######################################################
    # Astrocyte

    # ADTP_tot_a    = 1.345e-3 #    #1e-3*(ATP_n0 + ADP_n0) #2.6e-3  # total Adenosine phosphates in cytosol, calculated from Evans_77

    # ATP_e0 = 1.3 # == Init[23]     # ATP_c, cytosolic ATP
    # ADP_e0 = 0.045 # == Init[24]   # ADP_c, cytosolic ADP

    # only params that may differ from neuronal

    # Proton leak activity
    x_Hle_a: float = 149.61265600173826  # 150.0               # x_Hle     # Proton leak activity

    # Potassium-Hydrogen-Antiport
    x_KH_a: float = 2.9802e7  # x_KH      # K+ / H+ antiporter activity

    # Matrix buffer and membrane capacitance
    x_buff_a = 1437.0652678883314  # 200/(0.5*T2Jcorrection) #  100                 # x_buff    # Inner Matrix hydrogen buffer capacity

    # potassium uniporter and adenylate kinase neglected
    x_K_a: float = 0  # Passive potassium transporter activity
    x_AK_a: float = 0  # AK activity
    K_AK_a: float = 0  # Adenelyte Kinase switched off

    # Parameters for complex I
    x_C1_a: float = 1.0200e003  # x_C1       # Complex I activity

    # Parameters for complex III
    x_C3_a: float = 0.2241  # x_C3      # Complex III activity
    k_Pi3_a: float = 0.192e-3  # k_Pi3     # Complex III / Pi parameter
    k_Pi4_a: float = 25.31e-3  # k_Pi4     # Complex III / Pi parameter

    # Parameters for complex IV
    x_C4_a: float = 3.2131e-004  # x_C4      # Complex IV activity
    k_O2_a: float = 1.2e-4  # k_O2      # kinetic constant for complex IV M

    # Parameters for OM transporters
    x_Ht_a: float = 2044.5370854408536  # 2000.0               # x_Ht      # MOM permeability to protons (micron s^{-1})
    gamma_a: float = 5.99  # gamma     # MOM area per unit volume micron^{-1}
    x_A_a: float = 85.0  # x_A       # MOM permeability to nucleotides (micron s^{-1})
    x_Pi2_a: float = 327.0  # x_Pi2     # MOM permeability to phosphate (micron s^{-1})

    # Phosphate-Hydrogen-Cotransport
    k_dHPi_a: float = 10 ** (-6.75)  # k_dHPi    # H/Pi co-transpor Molar form factor 1 binding
    k_PiH_a: float = (
        0.45082e-3  # k_PiH     # H+/Pi co-transport activity form factor 2 Michaelis constant
    )
    x_Pi1_a: float = 3.85e5  # x_Pi1     # H+/Pi co-transport activity

    # Parameters for ATP synthase and Mg-binding to ATP?ADP
    x_MgA_a: float = 1e6  # x_MgA     # Mg2+ binding activity

    # Parameters for input function
    k_Pi1_a: float = 0.13413e-3  # k_Pi1      # Dehydrogenase flux input
    k_Pi2_a: float = 0.677e-3  # k_Pi2      # Dehydrogenase flux input

    ######################################################

    # optimised parameters

    # adj for eq: 0.9654561819314937
    r_DH_a: float = 4.51551099390501  # 4.3          # r_DH       # Input-flux: Initial disturbance of equilibrium

    # Parameters for input function
    # x_DH_a   =  0.04702218860608453 #0.05896      # x_DH       # Dehydrogenase activity
    x_DH_a: float = 0.014771869267445427  # 0.014885075252276352 #0.0151125164947073 #0.014882801669692953 # 0.041477965015268535 # 0.0412 # 0.04150217281642099 # 0.04702218860608453

    # Parameters for Adenosine Transferase
    x_ANT_a: float = (
        0.0881948452324846  # 0.07649900124686723 #0.0020              # x_ANT     # ANT activity
    )
    k_mADP_a: float = 1.07960040439672e-05  # 1.0588243052994988e-5 #3.50e-6             # k_mADP    # ANT Michaelis-Menten constant

    # Cytosolic ATP production and consumption
    # K_ADTP_dyn_a = 0.5912763309268644 #3.42      # K_ADTP_dyn Cytosolic ATP production
    # x_ATPK_a   = 0.30499319022776666 # 0.504    # x_ATPK
    # K_ADTP_cons_a = 1.1895556584725608 #1.0     # K_ADTP_cons Cytosolic ATP consumption

    # Parameters for ATP synthase and Mg-binding to ATP?ADP
    x_F1_a: float = (
        6306.50439347496  # 6912.715469614502 #6829.4        # x_F1      # F1Fo ATPase activity
    )
    K_DT_a: float = 0.00194323827864375  # 0.001855689326651793 #0.000192             # K_DT      # Mg/ATP binding constant (M)
    K_DD_a: float = 0.000328048467890892  # 0.00036972016989755054 #347e-6              # K_DD      # Mg/ADP binding constant (M)

    def __post_init__(self):
        self.etcRT: float = self.etcR * self.etcT  # kJ  mol^{-1}
        self.W_x: float = 0.9 * self.W_m  # Matrix water space (ml water / ml mito]
        self.W_i: float = 0.1 * self.W_m  # IM water space (ml water / ml mito]


@dataclass
class Gaba:
    # psiGAD_inh_n(GLU_n), GLU_n + MET_h_c_n ⇒ GABA_inh_n + MET_co2_c_n

    glutamatergic_gaba_scaling: float = 0.1  # 0.1 for GLU-neurons

    VmaxGAD_inh_n: float = 0.000178
    KmGAD_inh_n: float = 4.0
    # from Thesis of Evelyn Rodriguez: A MATHEMATICAL MODEL OF NEUROCHEMICAL MECHANISMS IN A SINGLE GABA NEURON

    # psiGAD_inh_n(GLU_n) = glutamatergic_gaba_scaling * VmaxGAD_inh_n*GLU_n/(KmGAD_inh_n + GLU_n)
    # psiGAD_inh_n1 = glutamatergic_gaba_scaling * VmaxGAD_inh_n*GLU_n0/(KmGAD_inh_n + GLU_n0)

    # psiGLU_GABA is 0.13 umol per gram tissue per minute. # Yamashita 2018: vesicular GABA uptake rate is 5–6 times slower than the glutamate uptake rate

    ###############################################

    # psiGADcatab_inh_n(GABA_inh_n), GABA_inh_n ⇒ SUCmito_n

    # combo of reactions in Bigg:
    # ABUTD,4ABUTtm,ABTArm,SSALxm(r0178)

    kGADcatab_inh_n: float = 0.0005  # 0.00101

    # psiGADcatab_inh_n(GABA_inh_n) = glutamatergic_gaba_scaling*kGADcatab_inh_n * GABA_inh_n
    # psiGADcatab_inh_n1 = glutamatergic_gaba_scaling*kGADcatab_inh_n * GABA_inh_n0


@dataclass
class GeneralParameters:
    R: float = 8.31  # J/(K*mol)
    T: float = 310.0  # Kelvin, 37 C
    F: float = 9.64853e04  #
    RTF: float = 26.73  # mV

    eto_n: float = 0.45  # Jolivet2015 # 0.4 # volume fraction neuron Calvetti2018      #
    eto_a: float = 0.25  # 0.3 # volume fraction astrocyte Calvetti2018   # 0.25 Jolivet2015
    eto_ecs: float = 0.2  # 0.3 # volume fraction ecs Calvetti2018       # 0.2 Jolivet2015
    eto_b: float = (
        0.0055  # 0.04 # volume fraction blood Calvetti2018      # 0.0055 Jolivet2015, Winter2017
    )
    beta = eto_n / eto_ecs  # 1.33 # Calvetti2018; in Cressman2011 it was set to 7.0

    # Compare J_C4 from Theurey with vMitooutn from Jolivet: 3.5926631697208284 times higher respiration (C4) in Theurey as compared to Jolivet (vMitooutn)
    # 1/3.5926631697208284 = 0.2783450473253539 = T2Jcorrection
    # make J_C4 (with proper 1000* /W_) be same as 0.6*vMitooutn (see du for O2, see enzymes_preBigg/OXPHOS_ETC_Theurey2019de_mMmod_n2test.ipynb ) and correspondingly change all other mito rates

    T2Jcorrection: float = 0.2783450473253539  # 1.3*0.2783450473253539 #1.3049872091414738*0.2783450473253539  # 0.2783450473253539

    def __post_init__(self):
        self.beta: float = (
            self.eto_n / self.eto_ecs
        )  # 1.33 # Calvetti2018; in Cressman2011 it was set to 7.0


@dataclass
class Generalizations:
    # mito resp from Jlv2015
    # VrespMitoout_n = 0.1610
    # VrespMitoout_a = 0.0627
    # KO2MitoResp = 0.001
    # KRespADP_n = 3.328e-03
    # KRespADP_a = 4.989e-04
    # KRespNADH_n = 4.54e-02
    # KRespNADH_a = 2.66e-02

    VrespMitoout_n: float = 0.140644217754747  # 0.15640216013767116
    VrespMitoout_a: float = 0.0510063287190737  # 0.06115387526422048

    KO2MitoResp: float = 0.001

    KRespADP_n: float = 0.0557248838326987  # 0.3495441819775649
    KRespADP_a: float = 0.0102874918177607  # 0.045393594641510326

    KRespNADH_n: float = 0.13114593324930549
    KRespNADH_a: float = 0.0759898967510787

    # NADH Shuttles a Jolivet opt
    TgNADH_jlv: float = 55.0410655992489  # 51.94256357630623
    MgCyto_jlv: float = 0.0002614  # 2.614e-04
    MgMito_jlv: float = 9620.0  # 9.620e+03

    # NADH Shuttles n Jolivet opt

    TnNADH_jlv: float = 2910.22500248421  # 2691.2265435495747 #1.1709070145980331*2298.411838000185 #0.9361685524612757*0.9996042792515688*0.6924570931165768*1.3051626594529149*1.462361970041893*0.8672648386372539*2142.799630588424 #2348.64 # 9446 # mmol/L/sec
    MnCyto_jlv: float = 4.653e-08
    MnMito_jlv: float = 366600.0  # 3.666e+05

    KmMito: float = 0.04
    KmMito_a: float = 0.02  # 0.04

    KmNADn_jlv: float = (
        2.023244602040409  # 4.171638354722493*0.485 #2.8886769438173014*0.485 #4.85e-01
    )
    KmNADg_jlv: float = (
        162.04744400627905  # 4.237642364180937*38.24 #2.8567630357548386*38.24 # mmol/L
    )

    VMaxMitoinn: float = 0.877982001488671  # 1.110778742993905  #0.147
    VMaxMitoing: float = 34.5066477078802  # 42.837139022091534 #0.07658716521503295 * 5.31

    V_oxphos_n: float = 4.60513160667386
    V_oxphos_a: float = 2.45307864305658
    K_oxphos_n: float = 1.0
    K_oxphos_a: float = 1.0
    mu_oxphos_n: float = 0.00778541423822839
    mu_oxphos_a: float = 0.0478833989798708
    nu_oxphos_n: float = 0.244089708012957
    nu_oxphos_a: float = 0.0615914841992225


@dataclass
class GLCtransport:
    C_Glc_a: float = 4.6  # C_Glc_a = 4.65 #4.75 #5.2 #5.25 #5.5 # DOI 10.1002/glia # 4.75 in Jolivet # 4.8 Winter2017Copasi  #5.5 #Glc_b0 + 0.5    #Glc_b0 + 0.8 # aprox from Calvetti and Nehlig1992  # check it

    # concentration_enzyme_transporter_GLUT1_cap = 0.000208/5 # /5 because five-fold more carriers in parenchymal cells than in endothelium  DOI 10.1002/glia.20375
    # kcat_TbGlc = 1149.0*5 # calc from TbGlc 0.239 Jolivet and concGlut1, *5 because /5 in conc because five-fold more carriers in parenchymal cells than in endothelium  DOI 10.1002/glia.20375

    # # TmaxBBB = 0.023 mM/s # DOI 10.1002/glia
    # # KztBBB = 5 mM # DOI 10.1002/glia

    # KbGlc_b = 8.0 # GLUT1 on BBB Ronowska2018  Simpson 2007  #4.6 #0.6 #5.0 #4.60 # mM # Km GLC  1-2 mM for GLC influx; Km GLC is 20-30 mM for GLC efflux # Wayne Alberts Basic Neurochemistry 8th edition 2012

    # DiNuzzo2010 DiNuzzo2010_1.pdf

    # blood -> endoth
    TmaxGLCce: float = 2.21  # 0.239 #<JLV 2.2 #2.55 #3.0 #2.5 #5. #1.0 #2.0 #1.2 # 0.4 #0.3 #0.15 #0.1 # ok #0.05 #0.023 #5.67 in DiNuzzo2010
    KeG: float = 10.3  # luT1Barros2007 #8. #10. in DiNuzzo2010 # 8 in Barros2007
    ReGoi: float = 1.0
    ReGio: float = 1.0
    ReGee: float = 1.0

    # endoth -> ecsBA
    TmaxGLCeb: float = 20.0  # 0.239 #10.0 #4.0 #3.5 #1.5 #0.8 # 1.2 #1.5 #0.6 #0.3 #ok with TmaxGLCce = 0.1 #0.2 # ok w/o diff #0.25 #0.023 #0.2 #0.085 #0.1 #0.026 # estim #6.41 in DiNuzzo2010
    KeG2: float = 12.5  # ablBarros2007 #8. #10. in DiNuzzo2010 # 8 in Barros2007
    ReGoi2: float = 1.0
    ReGio2: float = 1.0
    ReGee2: float = 1.0

    # ecsBA -> a
    TmaxGLCba: float = 8.0  # 2.45 #0.147 #<JLV 20.0 #12.0 #0.1 #0.08 #5.5 #2.5 #1.0 #0.5 #0.4 #0.2 # ok #0.6 #0.34 #0.023 #0.35 #0.35 #0.2 #0.147 #Jlv2015 #0.08 in DiNuzzo2010
    KeG3: float = 8.0  # 10. in DiNuzzo2010 # 8 in Barros2007
    ReGoi3: float = 1.0
    ReGio3: float = 0.73
    ReGee3: float = 0.73

    # a -> ecsAN
    TmaxGLCai: float = 0.032  # 1.0 #0.3 #0.2 #0.4 #0.6 #0.023 #0.1 #0.147 #0.14 in DiNuzzo2010
    KeG4: float = 8.0  # 10. in DiNuzzo2010 # 8 in Barros2007
    ReGoi4: float = 1.0
    ReGio4: float = 1.36
    ReGee4: float = 1.36

    # ecsAN -> n
    TmaxGLCin: float = (
        0.4  # 0.1 #0.041 #<JLV #0.5 #1.0 #1.1 #1.2 #0.6 #0.023 #0.35 #0.041 #0.58 in DiNuzzo2010
    )
    KeG5: float = 2.8  # 4. #DiNuzzo2010 # 2.8 in Barros2007
    ReGoi5: float = 1.0
    ReGio5: float = 0.72
    ReGee5: float = 0.72

    # diffusion
    kGLCdiff: float = 0.29  # 0.2875 #0.023 #0.03 #0.01 #0.023

    # # derived from Barros2007
    # KztINb2endo = 5.
    # KztINendo2eBA = 5.
    # KztINeBA2a = 5.
    # KztINa2ecsAN = 5.
    # KztINecsAN2n = 5.
    # Kitb2endo = 21.
    # Kitendo2eBA = 21.
    # KitecsBA2a = 21.
    # Kita2ecsAN = 21.
    # KitecsAN2n = 21.


@dataclass
class Gltgln:
    # SNAT n: psiSNAT_GLN_n(GLN_out,GLN_n), GLN_out ⇒ GLN_n

    TmaxSNAT_GLN_n: float = 0.07614698345131839  # 0.02331661188845118 # < after opt # 0.039
    KmSNAT_GLN_n: float = 1.1  # Chaudhry 1999
    coeff_gln_ratio_n_ecs: float = 2.5  # 1.0506973592641118 # < after opt # 2.5

    # #psiSNAT_GLN_n(GLN_out,GLN_n) = TmaxSNAT_GLN_n*(GLN_out-GLN_n/coeff_gln_ratio_n_ecs)/(KmSNAT_GLN_n+GLN_n)
    # psiSNAT_GLN_n1 = TmaxSNAT_GLN_n*(GLN_out0 - GLN_n0/coeff_gln_ratio_n_ecs)/(KmSNAT_GLN_n+GLN_n0)

    #######################################

    # GLS n: psiGLS_n(GLN_n,GLUmito_n), GLN_n ⇒ GLUmito_n

    # bigg "psiGLS_n":["GLNtm_n","GLUNm_n","GLUt2m_n"]

    VmGLS_n: float = 330.14406166650446  # 0.02921417471855462 # < after opt # 0.01
    KeqGLS_n: float = 25.0  # 12.0
    KmGLNGLS_n: float = 12.0
    KiGLUGLS_n: float = 45.0

    # #psiGLS_n(GLN_n,GLUmito_n) = VmGLS_n*( GLN_n - GLUmito_n/KeqGLS_n )/ (KmGLNGLS_n*(1.0 + GLUmito_n/KiGLUGLS_n) + GLN_n  )
    # psiGLS_n1 = VmGLS_n*( GLN_n0 - GLUmito_n0/KeqGLS_n )/ (KmGLNGLS_n*(1.0 + GLUmito_n0/KiGLUGLS_n) + GLN_n0  )

    #######################################

    # synGlutRelease

    glut_vesicle_deltaConc: float = 0.1  # mM Flanagan2018
    coeff_synGlutRelease: float = 1.5  # 0.33

    # ! ATTENTION ! v_thr depends on saveat (and tstops)

    # # when solving with saveat 1e-4:
    # v_thr =  -60. #-2.732

    # when solving with saveat 1e-1:
    v_thr: float = 60.0  # -2.732

    # synGlutRelease(V) =  glut_vesicle_deltaConc*exp(-((V+v_thr)/coeff_synGlutRelease)^2) / (coeff_synGlutRelease * 1.772 )

    ##########################################

    # psiEAAT12(Va,Na_a,GLUT_syn,GLUT_a,K_a,K_out),  GLUT_syn ⇒  Va + GLUT_a
    # bigg GLUt6(), k_c + glu__L_e + h_e + 3.0 na1_e ⇌ glu__L_c + h_c + 3.0 na1_c + k_e
    # bigg closest rn: GLUt6: k_c + glu__L_e + h_e + 3.0 na1_e ⇌ glu__L_c + h_c + 3.0 na1_c + k_e

    # Flanagan 2018

    # GLTGLN_r01_EAAT12_a

    Na_syn_EAAT: float = 150.0  # 150 to be same as out #140.0
    H_syn_EAAT: float = 4e-05
    H_ast_EAAT: float = 6e-05
    SA_ast_EAAT: float = 2.8274e-13  # m2
    alpha_EAAT: float = 0.41929231117352916  # 0.0011781014781337903 # < after opt # 1e-5 #1e-06
    beta_EAAT: float = 0.035  # 0.0292
    K_ast_EAAT: float = 100.0
    Vol_syn: float = 1e-18
    Vol_astEAAT: float = 3.76e-17

    # EAAT1  / GLT-1
    # VrevEAAT = (R*T/(2*F))* log( ((Na_syn_EAAT/Na_a)^3) *  (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/GLUT_a)   *   (K_a/K_out )  )

    #  VrevEAAT = (R*T/(2*F))* log( clamp(((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_ast_EAAT/  clamp(K_out,1e-12,K_out))  ,1e-12,  ((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_ast_EAAT/  clamp(K_out,1e-12,K_out))   ) ) # simplified K
    ##worked with this before 26may2020 VrevEAAT = (R*T/(2*F))* log( clamp(((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_a/  clamp(K_out,1e-12,K_out))  ,1e-12,  ((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_a/  clamp(K_out,1e-12,K_out))   ) ) # simplified K

    # VrevEAAT() = (R*T/(2*F))* log( clamp(((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_a/  clamp(K_out,1e-12,K_out))  ,1e-12,  ((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_a/  clamp(K_out,1e-12,K_out))   ) ) # simplified K
    # VEAAT() =  (1/(2*F))* SA_ast_EAAT * (  -alpha_EAAT*exp(-beta_EAAT*(Va - VrevEAAT)) )  # # Va = Va0
    # psiEAAT12() = - ((1/(2*F))* SA_ast_EAAT * (  -alpha_EAAT*exp(-beta_EAAT*(Va - (R*T/(2*F))* log( clamp(((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_ast_EAAT/  clamp(K_out,1e-12,K_out))  ,1e-12,  ((Na_syn_EAAT/ clamp(Na_a,1e-12,Na_a)  )^3) * (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/  clamp(GLUT_a,1e-12,GLUT_a)   ) * (K_ast_EAAT/  clamp(K_out,1e-12,K_out))   ) )          )) ) ) / Vol_syn

    # VEAAT(Va,Na_a,GLUT_syn,GLUT_a,K_a,K_out) =  (1/(2*F))* SA_ast_EAAT * (  -alpha_EAAT*exp(-beta_EAAT*(Va - ((R*T/(2*F))* log( ((Na_syn_EAAT/Na_a)^3) *  (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/GLUT_a)   *   (K_a/K_out )  )))) )  # # Va = Va0

    # worked in full sys:
    # psiEAAT12(Va,Na_a,GLUT_syn,GLUT_a,K_a,K_out) = - 0.1* ((1/(2*F))* SA_ast_EAAT * (  -alpha_EAAT*exp(-beta_EAAT*(Va - ((R*T/(2*F))* log( ((Na_syn_EAAT/Na_a)^3) *  (H_syn_EAAT/H_ast_EAAT)  *  (GLUT_syn/GLUT_a)   *   (K_a/K_out )  )))) )) / Vol_syn  #worked with this before 26may2020

    # #psiEAAT121 = - ((1/(2*F*1e-3))* SA_ast_EAAT * (  -alpha_EAAT*exp(-beta_EAAT*(Va0 - ((R*T/(2*F*1e-3))*log( ((Na_syn_EAAT/Na_a0)^3) *  (H_syn_EAAT/H_ast_EAAT)  *   (GLUT_syn0/GLUT_a0)   *   (K_a0/K_out0 )  )))) ))
    # psiEAAT121 = - ((1/(2*F*1e-3)) * (  -alpha_EAAT*exp(-beta_EAAT*(Va0 - ((R*T/(2*F*1e-3))*log( ((Na_syn_EAAT/Na_a0)^3) *  (H_syn_EAAT/H_ast_EAAT)  *   (GLUT_syn0/GLUT_a0)   *   (K_a0/K_out0 )  )))) ))

    # #/ Vol_syn  #worked with this before 26may2020

    # # check it, should have Vol_syn but Domain error in log if Vol_syn without clamp, but clamp is not easily compatible with Catalyst and not biological

    ##########################################

    # psiGDH_simplif_a(NADmito_a,GLUmito_a,NADHmito_a,AKGmito_a), GLUmito_a + NADmito_a ⇒ AKGmito_a + NADHmito_a
    # bigg GDHm glu__L_m + h2o_m + nad_m ⇌ akg_m + h_m + nadh_m + nh4_m

    # GLTGLN_r02_GDH_a

    VmGDH_a: float = 0.0192685649342926  # 0.02  #0.1 #0.02
    KeqGDH_a: float = 1.5  # 1.0 #0.646 #0.34 #0.3
    KiNAD_GDH_a: float = 1.0
    KmGLU_GDH_a: float = 3.5  # 0.33 Mezhenska2019
    KiAKG_GDH_a: float = 0.25  # 4.2 Mezhenska2019
    KiNADH_GDH_a: float = 0.004
    KmNADH_GDH_a: float = 0.04
    KmAKG_GDH_a: float = 1.1  # 0.36 Mezhenska2019
    KiGLU_GDH_a: float = 3.5  # 9.0  Mezhenska2019

    ##########################################

    # psiGLNsynth_a(GLUT_a,ATP_a,ADP_a),  GLUT_a + ATP_a ⇒ GLN_a + ADP_a

    # GLTGLN_r03_GLNsynth_a

    VmaxGLNsynth_a: float = (
        0.020022679766390446  # 0.0013164531825672209 # < after opt #  0.01 #0.039
    )
    KmGLNsynth_a: float = 2.0  # 3.5 #2.0  # 3.5 LISTROM1997
    muGLNsynth_a: float = 0.01

    # Calvetti2011, Pamiljans1961

    # bigg GLNS atp_c + glu__L_c + nh4_c ⇌ adp_c + gln__L_c + h_c + pi_c

    ##########################################

    # psiSNAT_GLN_a(GLN_a,GLN_out),  GLN_a ⇒ GLN_out

    # GLTGLN_r04_SNAT_a

    TmaxSNAT_GLN_a: float = 0.054730164766604375  # 0.039  #0.008
    KmSNAT_GLN_a: float = 1.1
    coeff_gln_ratio_a_ecs: float = 1.0

    # #SNAT GLN transporter
    # psiSNAT_GLN_a1 = TmaxSNAT_GLN_a*(GLN_a0-GLN_out0)/(KmSNAT_GLN_a+GLN_a0)

    # #bigg GLNt4: gln__L_e + na1_e → gln__L_c + na1_c


@dataclass
class Glycogen:
    # Glycogen

    # based on DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151

    # Glycogen synthase
    # VmaxGS_a = 0.07585 # 0.00153 #0.1 #0.5 #DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 0.000153 in Cloutier2009 0.0001528 in cellml Cloutier2009
    kL2_GS_a: float = 0.4502909779144298  # 3.4 # JC2018 #3.33 #0.017 #0.01 # 1.53e-4 mM/s Cloutoer2009 #0.017 #mmol/L per s #DiNuzzo2010 PMID: 20827264 #3.33 prev par opt Jay
    kmL2_GS_a: float = 1.4  # 0.57 # JC2018

    # Glycogen phosphorylase
    k_L2_GS_a: float = 0.8008668792292503  # 0.34  # JC2018
    km_L2_GS_a: float = 1.4  # JC2018

    VmaxGP_a: float = 0.001843542832727982  # 5.41521636193213E-06 # 0.00000525 # 0.000005 #0.00005 #0.0001 #0.001 #0.008 #DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 4.92e-5 in Cloutier2009 4.922e-5 in cellml Cloutier2009
    KmGP_AMP_a: float = 0.1  # 1e-5 # 1e-5 adj to new u0 24aug22 #0.01 # adj AMP to match glycogen dynamics in DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 0.016 DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151
    hGPa: float = 1.5

    # adapted from Lambeth
    # Phosphoglucomutase
    Vmaxfpglm_a: float = 1.8474212896979174  # 0.00095469565397463 # 0.64 #0.001 #0.005 #0.01 #0.1 #adj to gp flux at act # 8mM/s - 0.48 M/min Lambeth
    KmG6PPGLM_a: float = (
        0.001  # 0.0024 #0.03  # adj from conc diff 0.03*0.06/0.75 # g6p = 0.75 Lambeth
    )
    KmG1PPGLM_a: float = (
        0.01  # 0.0107 # adj from conc diff 0.063*0.01/0.0589 #0.063 # g1p = 0.0589  Lambeth
    )
    KeqPGLM_a: float = 4.9  # 6.5 # 16.62 #1.0048450801727364*6.5 #7.05 #7.01 # adj from conc ratio to flux close to GP flux at steady state #0.45

    # VmaxPDE_a = 1.92e-5 #0.00105*exp(-4) with approx conc from mol atlas #1050.0
    VmaxPDE_a: float = 1e-3  # 1.92e-5 #0.00105*exp(-4) with approx conc from mol atlas #1050.0
    Kmcamppde_a: float = 0.0055  # mM #5500.0
    # psiPDE_a(cAMP_a) = VmaxPDE_a*cAMP_a/(Kmcamppde_a + cAMP_a)

    # details glycogen regulation
    # GSAJay
    kg8_GSAJay: float = 5.0
    st_GSAJay: float = 0.003
    kmg8_GSAJay: float = 0.00012
    s1_GSAJay: float = 100.0
    kg2_GSAJay: float = 0.5
    kg7_GSAJay: float = 20.257289129639318  # 1.012864456481966*20.0  # kg7_GSAJay = 20.0
    kmg7_GSAJay: float = 0.015

    # Phosphorylase kinase act  0 ⇒ PHKa
    cai0_ca_ion: float = 5e-05
    kg3_PHKact: float = 20.0
    kt_PHKact: float = 0.0025
    kmg3_PHKact: float = 0.004
    kg4_PHKact: float = 5.0
    kmg4_PHKact: float = 0.0011

    # PHK
    kg5_PHK: float = 1915.1920260832771  # 20.0
    pt_PHK: float = 0.007
    kmg5_PHK: float = 0.01
    s1_PHK: float = 100.0
    kg2_PHK: float = 0.5
    kg6_PHK: float = 500.0  # 5.0
    kmg6_PHK: float = 0.005
    s2_PHK: float = 0.001
    kgi_PHK: float = 10.0
    kmind_PHK: float = 2e-06

    # PKA1,2
    kgc1_PKA12: float = 1e-06
    k_gc1_PKA12: float = 0.01

    kgc2_PKA12: float = 1e-06
    k_gc2_PKA12: float = 0.01

    # GP
    Vmaxfgpa: float = 0.001  # 4.93e-5 #Cloutier2009 # 0.008 DiNuzzo2010 #0.33

    Km_GLY_b_GP_a_a: float = 0.15
    Ki_G1P_GP_a_a: float = 10.1
    Ki_GLY_fGP_a_a: float = 2.0
    Km_Pi_GP_a_a: float = 4.0
    KeqGPa: float = 0.42

    Ki_Pi_G_P_a_a: float = 4.7
    Km_GLY_fGP_a_a: float = 1.7

    ###
    Vmaxfgpb: float = 0.5

    KiGLYbGP_b_a: float = 4.4
    Km_G1P_GP_b_a: float = 1.5
    Ki_GLY_fGP_b_a: float = 15.0
    Km_Pi_GP_b_a: float = 0.2
    KeqGPb: float = 0.42

    AMPnHGPb = 1.5  # 1.75  # 1.5 DiNuzzo2010
    Km_AMP_GP_b_a = 0.016  # DiNuzzo2010 #1.9e-06
    Ki_Pi_G_P_b_a = 4.6
    Ki_G1P_GP_b_a = 7.4

    #### UDPGP
    VmaxfUDPGP: float = 0.004420628605834113  # 0.0045555170380946215 #0.0015762057284464041*2.890179217014261 # 1.374710748327394*1.070600857717005*0.01253505948380228 #
    VmaxrUDPGP: float = 0.017682514423336453  # 0.018222068152378486 # 0.0015762057284464041*11.560716868057044 # 1.374710748327394*1.070600857717005*0.8599116744575482* 0.026768820961076727*0.027228381148077584*2.5
    KutpUDPGP: float = 0.05  # KutpUDPGP
    Kg1pUDPGP: float = 0.1
    KpiUDPGP: float = 0.2  # 200.0 # 200 as adj for Pi instead of PPi #0.2
    KUDPglucoUDPGP_a: float = 0.05  # KglucoUDPGP


@dataclass
class Glycolysis:
    # hexokinase
    VmaxHK_n: float = 0.51617647  # 0.075 #<flux0.00325  #0.050435 #<JLV #0.016 #0.01175 #0.0235 * 0.5 assuming sep half by half 0.0065 mM/s between n and a # 0.0235 is derived to have steady rate approx 0.0065 mM/s  #0.0068  w/o ATP in rate eq # Barros2007  #VmaxHK is 6 to 9 uM/sec https://doi.org/10.1093/cercor/bhs309
    # VmaxHK_n = 0.050435 #<JLV #0.016 #0.01175 #0.0235 * 0.5 assuming sep half by half 0.0065 mM/s between n and a # 0.0235 is derived to have steady rate approx 0.0065 mM/s  #0.0068  w/o ATP in rate eq # Barros2007  #VmaxHK is 6 to 9 uM/sec https://doi.org/10.1093/cercor/bhs309
    KmHK_n: float = 0.05  # Barros2007 KIATPhexn = 1.

    # KIATPhex_na = 0.558001157065081 #0.6 #0.95 #1.
    KIATPhex_n: float = 0.554  # KIATPhex_n = 0.558001157065081 #0.6 #0.95 #1.
    KIATPhex_a: float = 0.554  # KIATPhex_a = 0.558001157065081 #0.6 #0.95 #1.

    # KIATPhex_n = 0.558001157065081
    # KIATPhex_a = 0.558001157065081  #0.5575 #0.558001157065081 #0.6 #0.95 #1.
    # 0.5 up
    # 0.55 # slightly up, stim resp, import to cells from ecs
    # 0.554 import to cells from ecs
    # 0.556 import to cells from ecs
    # 0.557 ANLS, a ok n slightly up
    # 0.558001157065081 # almost steady, a slightly down # ANLS
    # 0.6 down

    nHhexn: float = 4.0

    VmaxHK_a: float = 0.4129411  # 0.06 #<flux0.00325 #0.185 #<JLV #0.013 #0.012 #0.0101 #0.0202 * 0.5 assuming sep half by half 0.0065 mM/s between n and a #0.0202 is derived to have steady rate approx 0.0065 mM/s  #0.0068 # Barros2007 #VmaxHK is 6 to 9 uM/sec https://doi.org/10.1093/cercor/bhs309
    # VmaxHK_a = 0.185 #<JLV #0.013 #0.012 #0.0101 #0.0202 * 0.5 assuming sep half by half 0.0065 mM/s between n and a #0.0202 is derived to have steady rate approx 0.0065 mM/s  #0.0068 # Barros2007 #VmaxHK is 6 to 9 uM/sec https://doi.org/10.1093/cercor/bhs309
    KmHK_a: float = 0.05  # Barros2007 KIATPhexn = 1.
    # KIATPhexa = 0.6 #0.95 #1.
    nHhexa: float = 4.0

    KiHKG6P_n: float = 0.01021  # 0.0102 #0.009206930693069307 0.0102 # Ki 0.017 from doi:10.1038/jcbfm.2010 scaled to difference of G6P steady state concentrations
    KiHKG6P_a: float = 0.0137  # 0.0132 #KiHKG6P_a = 0.0102 # Ki 0.017 from doi:10.1038/jcbfm.2010 scaled to difference of G6P steady state concentrations

    # KmATPHK_n = 0.2354545455 #0.37 #0.4 mM Garfinkler1987, 0.37 Berndt2015
    # KmATPHK_a = 0.1229090909 #0.208 #mM Garfinkler1987, 0.37 Berndt2015 # #0.208 - astrocyte specific Lai 1999 PMID: 10488914

    # fluxes Hex
    # n = 0.003246320878748037
    # a = 0.00325030914023512

    #####################################
    # PGI: Cloutier2009,Berndt2015
    # From Bouzier-Sore doi: 10.3389/fnagi.2015.00089 - (PGI) is a near-equilibrium enzyme that has been shown to be highly active at converting F6P into G6P in certain cells and/or tissues, such as, e.g., neurons (Gaitonde et al., 1989)

    # Vmax_fPGI_n = 0.5 #Cloutier2009 pdf # 0.5 in cellml Cloutier2009
    # Vmax_rPGI_n = 0.45 #Cloutier2009 pdf #0.45 in cellml Cloutier2009
    # Km_G6P_fPGI_n = 0.49 # 0.5 #0.593 # KfPGI Gaitonde PMID: 2709006  # 0.5 in cellml Cloutier2009
    # Km_F6P_rPGI_n = 0.08 #0.095 # KrPGI Gaitonde PMID: 2709006  # 0.06 in cellml Cloutier2009

    # Vmax_fPGI_a = 0.5 #Cloutier2009 pdf # 0.5 in cellml Cloutier2009
    # Vmax_rPGI_a = 0.45 #Cloutier2009 pdf #0.45 in cellml Cloutier2009
    # Km_G6P_fPGI_a = 0.49 # 0.5 #0.593 # KfPGI Gaitonde PMID: 2709006  # 0.5 in cellml Cloutier2009
    # Km_F6P_rPGI_a = 0.08 #0.095 # KrPGI Gaitonde PMID: 2709006  # 0.06 in cellml Cloutier2009

    Vmax_fPGI_n: float = 0.5109590762636075  # 0.5224916273904385 #0.6075442059699083  # 0.5 #Cloutier2009 pdf # 0.5 in cellml Cloutier2009
    # Vmax_rPGI_n = 0.5467897853729176 # 0.45 #Cloutier2009 pdf #0.45 in cellml Cloutier2009
    Km_G6P_fPGI_n: float = 0.593  # KfPGI Gaitonde PMID: 2709006  # 0.5 in cellml Cloutier2009
    Km_F6P_rPGI_n: float = 0.095  # KrPGI Gaitonde PMID: 2709006  # 0.06 in cellml Cloutier2009

    Vmax_fPGI_a: float = 0.5408672262560398  # 0.5231442728059117 #0.5231442728059117 #0.6085598341799668 #0.6085598341799668 #0.5 #Cloutier2009 pdf # 0.5 in cellml Cloutier2009
    # Vmax_rPGI_a = 0.5477038507619701 #0.5477038507619701 #0.45 #Cloutier2009 pdf #0.45 in cellml Cloutier2009
    Km_G6P_fPGI_a: float = (
        0.593  # 0.593 # KfPGI Gaitonde PMID: 2709006  # 0.5 in cellml Cloutier2009
    )
    Km_F6P_rPGI_a: float = (
        0.095  # 0.095 # KrPGI Gaitonde PMID: 2709006  # 0.06 in cellml Cloutier2009
    )

    #####################################

    # PFK
    # combo from Winter2017, Berndt2015, DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151

    # From Bouzier-Sore doi: 10.3389/fnagi.2015.00089 - PFK1 in neurons represents a glycolysis bottleneck (Almeida et al., 2004).
    # PFK1 in situ activity is very low in neurons when compared with neighbor astrocytes (Almeida et al., 2004).
    # Such a low PFK1 activity is due to the virtual absence of PFKFB3 (Herrero-Mendez et al., 2009),
    # in situ PFK1 activity is ∼four-fold lower in neurons when compared with astrocytes (Almeida et al., 2004).

    # VmaxPFK_n = 0.42 #0.11 # DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 0.44 Winter2017
    # VmaxPFK_a = 0.2 #0.06 # DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 0.2 Winter2017
    VmaxPFK_n: float = 0.3511362207540195  # 0.35252996309065393 # 0.369795304963641 #0.435 # 0.42 #0.11 # DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 0.44 Winter2017
    VmaxPFK_a: float = 0.15208109403904177  # 0.14812183418703848 # 0.1554503408943446 #0.20496159880969 #0.25 #0.435 #0.235 #0.2 #0.06 # DiNuzzo2010_2_glycogen.pdf doi:10.1038/jcbfm.2010.151 # 0.2 Winter2017

    KmPFKF6P_n: float = 0.05170785  # 0.03913 # adj from Winter2017 for difference in conc: 0.03913 = 0.18*0.01/0.046  # (0.0642857 + 0.03913)/2 = 0.05170785
    KmPFKF6P_a: float = 0.035  # 0.05170785 #0.0642857 # adj from Winter2017 for difference in conc: 0.0642857 = 0.18*0.01/0.028 # (0.0642857 + 0.03913)/2 = 0.05170785

    KiPFK_ATP_na: float = (
        0.666155029035142  # 0.6 # adj for diiff ATP DiNuzzo2010,Winter2017,Jolivet2015
    )
    KiPFK_ATP_n: float = (
        0.666155029035142  # 0.6 # adj for diiff ATP DiNuzzo2010,Winter2017,Jolivet2015
    )
    KiPFK_ATP_a: float = (
        0.666155029035142  # 0.6 # adj for diiff ATP DiNuzzo2010,Winter2017,Jolivet2015
    )

    # KiPFK_ATP_a = 0.6 # adj for diiff ATP DiNuzzo2010,Winter2017,Jolivet2015
    nPFKn: float = 4.0  # DiNuzzo2010,Winter2017,Jolivet2015
    nPFKa: float = 4.0  # DiNuzzo2010,Winter2017,Jolivet2015

    KmF26BP_PFK_a: float = 0.0042  # 0.00485 #0.00475 #0.005 # 0.001 #adj for conc #0.0042 # Berndt2015, repeated par in pdf: 0.0042 and 0.005
    nPFKf26bp_a: float = 5.5  # Berndt2015
    KoPFK_f26bp_a: float = 0.55  # Berndt2015

    #####################################

    # PFK2 PFKFB3

    # From Bolanos doi:10.1016/j.tibs.2009.10.006 - Isoform 3 (PFKFB3) displays the highest (~700 fold) kinase to bisphosphatase ratio
    # its activity is almost exclusively dedicated to the generation of F2,6P2

    # kinase
    Vmax_PFKII_g: float = 0.0031731959656441096  # 0.00333019366990191 #0.00333019366990191 #0.003 #0.01 #0.052 #0.06 # 0.026 # adj, no AMP in eq, Vmax opt in Berndt2015 #0.0026

    Kmf6pPFKII_g: float = (
        0.027  # 0.027 #0.016 # F26BP_J. Biol. Chem.-1984-Kitajima-6896-903.pdf #0.027
    )
    KmatpPFKII_g: float = 0.0675993571084336  # 0.0675993571084336 #0.055 #0.15 # F26BP_J. Biol. Chem.-1984-Kitajima-6896-903.pdf  #0.055
    # Km_act_ampPFKII_g = 0.073
    Km_act_adpPFKII_g: float = 0.0667721029996198  # 0.0667721029996198 #0.056 #0.062 # F26BP_J. Biol. Chem.-1984-Kitajima-6896-903.pdf #0.056

    # Fructose-2,6-bisphosphatase # Berndt 2015
    Vmax_f26pase_g: float = 0.052  # 0.052
    Km_f26bp_f_26pase_g: float = (
        0.07  # 0.07 #0.001 #F26BP_J. Biol. Chem.-1984-Kitajima-6896-903.pdf #0.07
    )
    Ki_f6p_f_26_pase_g: float = (
        0.02  # 0.02 #0.0015 #F26BP_J. Biol. Chem.-1984-Kitajima-6896-903.pdf #0.02
    )

    #####################################

    # ALD

    # Berndt2015

    # Vmaxald_n = 4.01 #Vmaxald_n = 4.0 #1.5 #0.47 #4.7 #46.8  # adj
    Vmaxald_n: float = 1.400146917265416  # 1.405738558339811 #1.47463603942376 #1.42 #4.01 #4.0 #1.5 #0.47 #4.7 #46.8  # adj

    # Keqald_n = 0.01 #0.005 #0.0976 # Berndt2015
    Keqald_n: float = 0.1  # PMID: 5357024 liver

    KmfbpAld_n: float = 0.003
    KmgapAld_n: float = 0.08
    KmdhapAld_n: float = 0.03

    # Vmaxald_a = 4.01 # 4.0 #1.5 # 0.47 #4.7 #46.8  # adj
    Vmaxald_a: float = 3.2308258205047813  # 3.1524640987394714 #3.313845197899958 #1.42579935322302 # 1.42 # 4.01 #4.0 #1.5 # 0.47 #4.7 #46.8  # adj

    # Keqald_a = 0.01 #0.005 #0.0976 #Berndt2015
    Keqald_a: float = 0.0005  # 0.1

    KmfbpAld_a: float = 0.003  # 0.003
    KmgapAld_a: float = 0.08  # 0.08
    KmdhapAld_a: float = 0.03  # 0.03

    #####################################

    # TPI

    # Berndt2015

    # ATTENTION!

    # Vmaxtpi_n =  1000000.0
    # Keqtpi_n =  0.05 #0.125 #0.05 #0.1 #0.045 # Berndt hepatokin #0.0545
    # KmdhapTPI_n = 0.84
    # KmgapTPI_n =   1.65

    # Vmaxtpi_a =  1000000.0
    # Keqtpi_a =  0.05 # 0.126 #0.125 #0.05 #0.1 #0.045 # Berndt hepatokin #0.0545
    # KmdhapTPI_a = 0.84
    # KmgapTPI_a = 1.65

    Vmaxtpi_n: float = 0.9842422040175792  # 0.9881749131463432 #1.03661007322829 #1.0 #1000000.0
    Keqtpi_n: float = (
        20.0  # PMID: 5357024 #0.05 #0.125 #0.05 #0.1 #0.045 # Berndt hepatokin #0.0545
    )
    KmdhapTPI_n: float = 0.6  # 0.84
    KmgapTPI_n: float = 0.4  # 1.65

    Vmaxtpi_a: float = 1.0263480086710068  # 1.0014347584951384 #1.05267198236797 # 1.05267198236797 #1.0 #1000000.0
    Keqtpi_a: float = (
        20.0  # PMID: 5357024 #0.05 # 0.126 #0.125 #0.05 #0.1 #0.045 # Berndt hepatokin #0.0545
    )
    KmdhapTPI_a: float = 0.6  # 0.84
    KmgapTPI_a: float = 0.4  # 1.65

    #####################################

    # GAPDH

    # Berndt2015 brain, Berndt2018 hepatokin

    Vmaxgapdh_n: float = 182.64561255814576  # 182.63166317515197 #187.048654473353 #193.6294833757099 #250.0 #1000.0 #72000.0

    Keqgapdh_na: float = 0.2  # 0.0015 #0.028 #0.0868 #0.04 #0.0868

    KmnadGpdh_n: float = 0.00947604205269482  # 0.01  #0.027 #0.01  or 0.027
    KmGapGapdh_n: float = 0.101
    KmpiGpdh_n: float = 3.9  # 67.8260869565 #67.8 after Pi changes to ETC-Pi # 3.9
    KmnadhGapdh_n: float = 0.00817504585255996  # 0.008
    KmBPG13Gapdh_n: float = 0.0035

    Vmaxgapdh_a: float = 3388.635929380235  # 3301.602157609392 #3388.71025575609 #3096.9093812733613 #250.0  #1000.0 #72000.0

    # Keqgapdh_a = 0.028 #0.0868 #0.04 #0.0868
    KmnadGpdh_a: float = 0.0106952634603107  # 0.01  #0.027 #0.01  or 0.027
    KmGapGapdh_a: float = 0.101
    KmpiGpdh_a: float = 3.9  # 67.8260869565 #67.8 after Pi changes to ETC-Pi # 3.9
    KmnadhGapdh_a: float = 0.008659493402079  # 0.008
    KmBPG13Gapdh_a: float = 0.0035

    # Vmaxgapdh_n = 7000.0 #72000.0
    # Keqgapdh_n = 0.026 #0.0868 #0.04 #0.0868
    # KmnadGpdh_n =  0.01  #0.027 #0.01  or 0.027
    # KmGapGapdh_n = 0.101
    # KmpiGpdh_n = 3.9
    # KmnadhGapdh_n = 0.008
    # KmBPG13Gapdh_n = 0.0035

    # Vmaxgapdh_a = 7000.0 #72000.0
    # Keqgapdh_a = 0.026 #0.0868 #0.04 #0.0868
    # KmnadGpdh_a =  0.01  #0.027 #0.01  or 0.027
    # KmGapGapdh_a = 0.101
    # KmpiGpdh_a = 3.9
    # KmnadhGapdh_a = 0.008
    # KmBPG13Gapdh_a = 0.0035

    #####################################

    # PGK: Phosphoglycerate kinase
    # Berndt2015

    # Vmaxpgk_n = 12. #5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    # Keqpgk_n = 1310.0
    # Kmbpg13pgk_n = 0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_n = 0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_n = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_n = 0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_a = 12. #5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a =  1310.0
    # Kmbpg13pgk_a = 0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_a = 0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_a = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_a = 0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_n = 13. #5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    # Keqpgk_n = 1310.0
    # Kmbpg13pgk_n = 0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_n = 0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_n = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_n = 0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_a = 13. #5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a =  1310.0
    # Kmbpg13pgk_a = 0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_a = 0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_a = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_a = 0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_n = 13. #5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    # Keqpgk_n = 2500. #1830. #1310.0
    # Kmbpg13pgk_n = 0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_n = 0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_n = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_n = 0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_a = 13. #5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a = 2500. #1830. # 1310.0
    # Kmbpg13pgk_a = 0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_a = 0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_a = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_a = 0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_n = 13. #5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    # Keqpgk_n = 2600. #1830. #1310.0
    # Kmbpg13pgk_n = 0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_n = 0.3 #0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_n = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_n = 0.4 #0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_a = 13. #5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a = 2600. #1830. # 1310.0
    # Kmbpg13pgk_a = 0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_a = 0.3 #0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_a = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_a = 0.4 #0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_n = 13. # 5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    # Keqpgk_n = 2600. #1830. #1310.0
    # Kmbpg13pgk_n = 0.1 #0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_n = 0.45 #0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_n = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_n = 0.33 #0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_a = 13. # 5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a = 2600. #1830. # 1310.0
    # Kmbpg13pgk_a = 0.1 #0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_a = 0.45 #0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_a = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_a = 0.33 #0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_n = 13. # 5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    # Keqpgk_n = 2600. #1830. #1310.0
    # Kmbpg13pgk_n = 0.1 #0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_n = 0.33 #0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_n = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_n = 0.33 #0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    # Vmaxpgk_a = 13. # 5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a = 2600. #1830. # 1310.0
    # Kmbpg13pgk_a = 0.1 #0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmadppgk_a = 0.33 #0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmpg3pgk_a = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    # Kmatppgk_a = 0.33 #0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    Vmaxpgk_n: float = (
        90.8064278816738  # 100.0 #13. #5.5 # scaled in comparison of ratios with GAPDH Vmax #396.0
    )
    Keqpgk_na: float = 2600.0  # 1830. #1310.0

    Kmbpg13pgk_n: float = 0.1  # 0.063 # 0.0022 # Berndt2018 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    Kmadppgk_n: float = 0.350477947537394  # 0.3 #0.2 #0.4 #0.25 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    Kmpg3pgk_n: float = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    Kmatppgk_n: float = 0.38728441113536  # 0.4 #0.4 #0.25 #0.42 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    Vmaxpgk_a: float = 95.5247294642638  # 100. #13. #13. #5.5 # scaled in comparison of ratios with GAPDH Vmax 396.0
    # Keqpgk_a = 2600. #1830. # 1310.0
    Kmbpg13pgk_a: float = 0.1  # 0.063 # Km BPG13 = 0.063 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    Kmadppgk_a: float = 0.363316278693795  # 0.3 #0.2 #0.4 #0.42  # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    Kmpg3pgk_a: float = 0.67  # Km PG3 = 0.67 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS
    Kmatppgk_a: float = 0.431968764786817  # 0.4 #0.4 #0.25 # Km f ATP = 0.42 mM, Km r ATP = 0.25 mM HARMESH K. SHARMA and MORTON ROTHSTEIN 1983 ALTERED BRAIN PHOSPHOGLYCERATE KINASE FROM AGING RATS

    #####################################

    # PGM
    # Berndt2015

    Vmaxpgm_n: float = 1.0002776306165402  # 0.12 #472.0 # scaled to PGK #14400.0
    Keqpgm_n: float = 0.1814
    Kmpg3pgm_n: float = 0.22
    Kmpg2pgm_n: float = 0.28

    Vmaxpgm_a: float = 1.0  # 0.12 #472.0 # scaled to PGK #14400.0
    Keqpgm_a: float = 0.1814
    Kmpg3pgm_a: float = 0.22
    Kmpg2pgm_a: float = 0.28

    #####################################

    # ENOLASE
    # Berndt2015

    # Vmaxenol_n = 1.8 #216000.0

    # Keqenol_n = 0.7 #0.5 Berndt2015 # 1.7 Berndt2018
    # Kmpg2enol_n = 0.05
    # Km_pep_enol_n = 0.15

    # Vmaxenol_a = 1.8 #216000.0

    # Keqenol_a = 0.7 #0.5
    # Kmpg2enol_a = 0.05
    # Km_pep_enol_a = 0.15

    Vmaxenol_n: float = 12.0  # 1.8 #216000.0

    Keqenol_n: float = 0.8  # 0.7 #0.5 Berndt2015 # 1.7 Berndt2018
    Kmpg2enol_n: float = 0.05
    Km_pep_enol_n: float = 0.15

    Vmaxenol_a: float = 12.0  # 1.8 #216000.0
    Keqenol_a: float = 0.8  # 0.7 #0.5
    Kmpg2enol_a: float = 0.05
    Km_pep_enol_a: float = 0.15

    #####################################

    # Pyruvate Kinase PK
    # Berndt2015,Jolivet2015

    # Vmaxpk_n = 4. #5. #36.7 # Jolivet #23.76 # Berndt

    # Km_pep_pk_n = 0.074
    # Km_adp_pk_n = 0.25 #0.42
    # Ki_ATP_pk_n = 1. #4.4 # 2.2 #

    # Vmaxpk_a = 5. #10.0 #23.76 # 135.2 # Jolivet #23.76 # Berndt

    # Km_pep_pk_a = 0.074
    # Km_adp_pk_a = 0.25 #0.42
    # Ki_ATP_pk_a = 1. #4.4 #2.2 #

    # Vmaxpk_n = 4. #36.7 # Jolivet #23.76 # Berndt

    # Km_pep_pk_n = 0.074
    # Km_adp_pk_n = 0.42
    # Ki_ATP_pk_n = 4.4 # 2.2 #

    # Vmaxpk_a = 5.0 #23.76 # 135.2 # Jolivet #23.76 # Berndt

    # Km_pep_pk_a = 0.074
    # Km_adp_pk_a = 0.42
    # Ki_ATP_pk_a = 4.4 #2.2 #

    # Vmaxpk_n = 4. #36.7 # Jolivet #23.76 # Berndt

    # Km_pep_pk_n = 0.08 #0.074
    # Km_adp_pk_n = 0.5
    # Ki_ATP_pk_n = 4.4 # 2.2 #

    # Vmaxpk_a = 5.0 #23.76 # 135.2 # Jolivet #23.76 # Berndt

    # Km_pep_pk_a = 0.08 #0.074
    # Km_adp_pk_a = 0.5
    # Ki_ATP_pk_a = 4.4 #2.2 #

    # Vmaxpk_n = 4. #36.7 # Jolivet #23.76 # Berndt
    # Km_pep_pk_n = 0.08 #0.074
    # Km_adp_pk_n = 0.5
    # Ki_ATP_pk_n = 4. #4.4 # 2.2 #

    # Vmaxpk_a = 4.2 #23.76 # 135.2 # Jolivet #23.76 # Berndt
    # Km_pep_pk_a = 0.08 #0.074
    # Km_adp_pk_a = 0.5
    # Ki_ATP_pk_a = 4. #4.4 #2.2 #

    # Vmaxpk_n = 20.  #36.7 # Jolivet #4. #36.7 # Jolivet #23.76 # Berndt
    # # Km_pep_pk_n = 0.08 #0.074
    # # Km_adp_pk_n = 0.5
    # # Ki_ATP_pk_n = 4. #4.4 # 2.2 #

    # Vmaxpk_a = 20. #135.2 # Jolivet #4.2 #23.76 # 135.2 # Jolivet #23.76 # Berndt
    # # Km_pep_pk_a = 0.08 #0.074
    # # Km_adp_pk_a = 0.5
    # # Ki_ATP_pk_a = 4. #4.4 #2.2 #

    # Vmaxpk_n = 20.  #36.7 # Jolivet #4. #36.7 # Jolivet #23.76 # Berndt
    # Km_pep_pk_n = 0.13 #0.08 #0.074
    # Km_adp_pk_n = 2.3 #0.5
    # Ki_ATP_pk_n = 0.9 #4.4 # 2.2 #

    # Vmaxpk_a = 20. #135.2 # Jolivet #4.2 #23.76 # 135.2 # Jolivet #23.76 # Berndt
    # Km_pep_pk_a = 0.13  #0.08 #0.074
    # Km_adp_pk_a = 2.3 #0.5
    # Ki_ATP_pk_a = 0.9 #4.4 #2.2 #

    # Vmaxpk_n = 1200. #20.  #36.7 # Jolivet #4. #36.7 # Jolivet #23.76 # Berndt
    # Km_pep_pk_n = 0.1 #0.5 #0.074
    # Km_adp_pk_n = 0.28  #0.5
    # Ki_ATP_pk_n = 1. #2.2 #

    # Vmaxpk_a = 1200. #20. #135.2 # Jolivet #4.2 #23.76 # 135.2 # Jolivet #23.76 # Berndt
    # Km_pep_pk_a = 0.1  #0.5 #0.074
    # Km_adp_pk_a = 0.28 #0.5
    # Ki_ATP_pk_a = 1. #2.2 #

    # From DOI 10.1074/jbc.M508490200
    # with K:
    # VmaxPK = 1245.83 mM/s #299 umol/min/mg protein  -> 1000*299*0.25/60 = 1245.83 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    # KmPEP = 0.13 mM
    # KmADP = 2.3

    # VmaxPK = 1187.5 mM/s #285 umol/min/mg protein  -> 1000*285*0.25/60 = 1187.5 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    # KmPEP = 0.033 mM or 0.065 mM
    # KmADP = 0.28 mM or 0.25 mM

    # Keq=38900. # DOI 10.1074/jbc.M111422200

    # KersonGarfinkelMildvan1966 PMID: 6022859
    # fwd
    # Km_pep_pk_n = 0.075 #0.1 #0.5 #0.074
    # Km_adp_pk_n = 0.2 #0.28  #0.5
    # Ki_ATP_pk_n = 0.34 # 0.13 in text
    # KiPyrPK_n = 0.01
    # # rev
    # KmPyrPK_n = 13.  # 10. table
    # KmATPPK_n = 0.01  # 0.86 table
    # adj KersonGarfinkelMildvan1966 PMID: 6022859
    # psiPK_n(PEP_n,ADP_n,ATP_n,Pyr_n) = Vmaxpk_n*PEP_n*ADP_n / ( 1 + Km_adp_pk_n/ADP_n + (Km_pep_pk_n/PEP_n)*(1 + Pyr_n/KiPyrPK_n) +  (Km_adp_pk_n/ADP_n)*(Km_pep_pk_n/PEP_n)*(1 + Pyr_n/KiPyrPK_n) )

    # Mulukutla2015: ordered bi bi mechanism

    # VmfPK_n = 1245.83  # 1.0002776306165402*1245.83 # From DOI 10.1074/jbc.M508490200 #1.68  # 1200. #80. #
    # VmrPK_n = 0.032 #1245.83/38900 # where Keq=38900. from DOI 10.1074/jbc.M111422200 #0.004

    # Km_pep_PK_n = 0.1 # approx avg PMID: 6022859 and DOI 10.1074/jbc.M508490200
    # Km_adp_PK_n = 0.24  # approx avg PMID: 6022859 and DOI 10.1074/jbc.M508490200

    # Km_pyr_PK_n = 11.5 #15.0 #12.0 # 11.5 # PMID: 6022859 avg text+table
    # Km_Mg_atp_PK_n =  0.01 # text # 0.86 table  # PMID: 6022859

    # L_pk_n = 0.389
    # K_atpPK_n = 0.34 # 0.13 in text #3.39

    # VmfPK_a = 1275. #1269.1963812533515 # 1245.83  # From DOI 10.1074/jbc.M508490200 #1.68
    # VmrPK_a = 0.032 #1245.83/38900 # where Keq=38900. from DOI 10.1074/jbc.M111422200 #0.004

    # Km_pep_PK_a = 0.1 # approx avg PMID: 6022859 and DOI 10.1074/jbc.M508490200
    # Km_adp_PK_a = 0.24  # approx avg PMID: 6022859 and DOI 10.1074/jbc.M508490200

    # Km_pyr_PK_a =  10.363500082938396 # 11.5 # PMID: 6022859 avg text+table
    # Km_Mg_atp_PK_a =  0.01 # text # 0.86 table  # PMID: 6022859

    # L_pk_a = 0.389
    # K_atpPK_a = 0.34 # 0.13 in text #3.39

    # Berndt2015 + opt
    Vmaxpk_n: float = 7.48969758041304  # 7.843117959791727 #23.76

    Km_pep_pk_n: float = 0.074  # 0.1 # approx avg PMID: 6022859 and DOI 10.1074/jbc.M508490200
    Km_adp_pk_n: float = (
        0.562062013433244  # 0.42 # 0.24  # approx avg PMID: 6022859 and DOI 10.1074/jbc.M508490200
    )
    Ki_ATP_pk_n: float = 1.88029571803631  # 2.2 #4.4

    Vmaxpk_a: float = 8.88447689329492  # 8.789368481405708 #23.76

    Km_pep_pk_a: float = 0.074
    Km_adp_pk_a: float = 0.510068084908044  # 0.42
    Ki_ATP_pk_a: float = 1.76791009718649  # 2.2 #4.4


@dataclass
class Gshgssg:
    # psiGSSGR_n(GSSG_n,NADPH_n), GSSG_n + NADPH_n ⇒ 2GSH_n + NADP_n

    Vmf_GSSGR_n: float = 0.006  # 0.296193997692182 # 8.625213760987834e-6 # 0.0001 #0.0025 #kcat_f_GSSGR_n = 210.0 # Vali PMID: 17936517 10.7 # 0.0025 # 8.925 mM/h Reed2008 #Vmax_GSSGR_n #kcat_r_GSSGR_n = 210.0 # Vali PMID: 17936517 #0.12 #Vmr_GSSGR_n 0.000029 #0.00029 # par[382] # 0.0000005

    # KmGSSGRGSSG_n =  0.11112641937846 # 0.0642364727884081 # 0.0652 #PMID: 4018089 0.107 # mM 0.072 mM 0.107 mM # Reed 2008
    # KmGSSGRNADPH_n =  0.0100081583265437 # 0.00883424633339055 # 0.00401498478437164 #0.00852 #PMID: 4018089 0.0104 # mM Reed 2008
    # # simplified version, Reed2008; Vali PMID: 17936517
    KmGSSGRGSSG_n: float = 0.0652  # PMID: 4018089 0.107 # mM 0.072 mM 0.107 mM # Reed 2008
    KmGSSGRNADPH_n: float = 0.00852  # PMID: 4018089 0.0104 # mM Reed 2008

    ############################

    # psiGSSGR_a(GSSG_a,NADPH_a), GSSG_a + NADPH_a ⇒  2GSH_a + NADP_a

    Vmf_GSSGR_a: float = 0.003  # 0.323856399322304 #0.0025 #kcat_f_GSSGR_a = 210.0 # Vali PMID: 17936517 4.35 #Vmf_GSSGR_a  0.0025 # 8.925 mM/h Reed2008 #Vmax_GSSGR_n #Vmf_GSSGR_a   1.5 #15.27 # par[381]

    # kcat_r_GSSGR_a = 210.0 # Vali PMID: 17936517 0.05 #Vmr_GSSGR_a 0.000029 #0.00029 # par[382] # 0.0000005
    # KmGSSGRGSSG_a = 0.0825167868170385 #0.0652 #PMID: 4018089 #0.107 # mM 0.072 mM 0.107 mM # Reed 2008
    # KmGSSGRNADPH_a = 0.019192925530061 #0.00852 #PMID: 4018089 #0.0104 # mM Reed 2008

    KmGSSGRGSSG_a: float = 0.0652  # PMID: 4018089 #0.107 # mM 0.072 mM 0.107 mM # Reed 2008
    KmGSSGRNADPH_a: float = 0.00852  # PMID: 4018089 #0.0104 # mM Reed 2008

    # denom_offset_a = 1.73

    # # simplified version, Reed2008; Vali PMID: 17936517
    # psiGSSGR_a1 = (Vmf_GSSGR_a*GSSG_a0*NADPH_a0 ) / ( ( KmGSSGRGSSG_a + GSSG_a0 )*( KmGSSGRNADPH_a + NADPH_a0 )  )   # GSSG_a + NADPH_a ⇒  2GSH_a + NADP_a

    ############################

    # Mulukutla2015, Reed2008
    # psiGPX_n(GSH_n), 2GSH_n  ⇒ GSSG_n

    V_GPX_n: float = 0.001072378746836681  # 0.00173937423839227 # 0.00001  #0.00125 #kcat_GPX_n = 2.0 # Vali PMID: 17936517 2.7  0.00125 #4.33 # par[380]  # 4.5 mM/h
    KmGPXGSH_n: float = 0.571655480073944  # 0.571655480073944 # 0.5152645026510133 # 1.33 #0.133 # Vali PMID: 17936517 1.33 #mM # Reed2008
    # KmH2O2_n = 0.00009 # mM # can add H2O2 inhib see Reed 2008 for parameters and eq

    ############################

    # Mulukutla2015, Reed2008
    # psiGPX_a(GSH_a), 2GSH_a  ⇒  GSSG_a

    V_GPX_a: float = 0.0011730710542436833  # 0.0011730407957506474 #0.0011730286476087722 #0.00149823791984372 #0.00125 #kcat_GPX_a = 2.0 # Vali PMID: 17936517 #1.96 #V_GPX_a 0.00125 #4.33 # par[380]  # 4.5 mM/h
    KmGPXGSH_a: float = 1.13224874593032  # 1.33 #0.133 # Vali PMID: 17936517 #1.33 #mM # Reed2008
    # KmH2O2_a = 0.00009 # mM # can add H2O2 inhib see Reed 2008 for parameters and eq

    # psiGPX_a1 = V_GPX_a * GSH_a0 / (GSH_a0 + KmGPXGSH_a)

    VmaxGSHsyn_n: float = 1.5e-5
    KmGSHsyn_n: float = 0.03  # approx based on Reed2008

    VmaxGSHsyn_a: float = 1.5e-5
    KmGSHsyn_a: float = 0.03  # approx based on Reed2008

    glycine_n: float = 10.0  # PMID: 10719892 #0.924
    glycine_a: float = 2.0  # PMID: 10719892 #0.924
    glutamylCys_n: float = 0.021375  # 0.021 #0.022 #0.0098
    glutamylCys_a: float = 0.4  # 0.022 #0.0098
    KeGSHSyn_n: float = 5.6
    KeGSHSyn_a: float = 5.6
    Km_glutamylCys_GSHsyn_n: float = 0.022
    Km_glycine_GSHsyn_n: float = 0.3
    Km_glutamylCys_GSHsyn_a: float = 0.022
    Km_glycine_GSHsyn_a: float = 0.3

    # glutathioneSyntase1(GSH_n) = VmaxGSHsyn_n*GSH_n/(GSH_n + KmGSHsyn_n)
    # glutathioneSyntase1(GSH_n0)


@dataclass
class Ketones:
    # bHB art-cap

    C_bHB_a: float = 0.3  # 0.18

    # JbHBTrArtCap1 = (2*(C_bHB_a - bHB_b0)/eto_b)*(global_par_F_0 * (1+global_par_delta_F*(1/(1+exp((-4.59186)*(100-(global_par_t_0+global_par_t_1-3))))-1/(1+exp((-4.59186)*(100-(global_par_t_0+global_par_t_1+global_par_t_fin+3)))))))

    ################################

    # MCT bhb b

    # MCT1_bHB_b(bHB_b,bHB_ecs), bHB_b ⇒ ∅
    # (eto_b/eto_ecs)*(bHB_b,bHB_ecs), ∅ ⇒ bHB_ecs  # eto_b/eto_ecs = 0.0275

    VmaxMCTbhb_b: float = 0.35559905936750225  # 0.29 #mM/s # Neves 2012
    KmMCT1_bHB_b: float = 12.5  # mM # Perez-Escuredo 2016 Table 2
    # KmMCT1_bHB_a = 6.03 #mM - astrocyte #Jay's alt from Achanta and Rae 2017, with subref Tildon 1994

    # MCT1_bHB_b1 = VmaxMCTbhb_b*(bHB_b0/(bHB_b0 + KmMCT1_bHB_b) - bHB_ecs0/(bHB_ecs0 + KmMCT1_bHB_b))

    ################################

    # MCT bhb a: MCT1_bHB_a(bHB_ecs,bHB_a), bHB_ecs ⇒ bHB_a

    VmaxMCTbhb_a: float = 0.29  # mM/s # Neves 2012
    KmMCT1_bHB_a: float = 6.03  # mM astrocytes Achanta and Rae 2017, with subref Tildon 1994  #12.5 #mM # Perez-Escuredo 2016 Table 2
    # KmMCT1_bHB_a = 6.03 #mM #Jay's alt from Achanta and Rae 2017, with subref Tildon 1994

    ## Jay comment: besides MCT1, there is also the pyruvate transporter for bHB: betaOHB is poor substrate for the
    ## mitochondrial pyruvate carrier (KM = 5.6 mM; although its metabolite acetoacetate is carried with
    ## reasonable affinity (0.56 mM)"" Achanta and Rae 2017, Halestrap  1978 Biochem J.
    ## Not sure if we'll ever need this mechanism for bHB, maybe for AcAc

    # MCT1_bHB_a1 = VmaxMCTbhb_a*(bHB_ecs0/(bHB_ecs0 + KmMCT1_bHB_a) - bHB_a0/(bHB_a0 + KmMCT1_bHB_a))

    ################################

    # MCT bhb n: MCT2_bHB_n(bHB_ecs,bHB_n), bHB_ecs ⇒ bHB_n

    VmaxMCTbhb_n: float = 0.29032861767118245  # 0.29 #mM/s # Neves 2012
    KmMCT2_bHB_n: float = 1.2  # mM # Perez-Escuredo 2016 https://doi.org/10.1016/j.bbamcr.2016.03.013 Table 2 # Ronowska 2018

    # MCT2_bHB_n1 = VmaxMCTbhb_n*(bHB_ecs0/(bHB_ecs0 + KmMCT2_bHB_n) - bHB_n0/(bHB_n0 + KmMCT2_bHB_n))

    ################################

    # bHBDH_n(NAD_n,bHB_n), NAD_n + bHB_n  ⇒  AcAc_n + NADH_n

    # beta-hydroxybutyrate dehydrogenase is exclusively located in mitochondria (DOI: 10.1002/iub.2367)
    # but here I was using cytosolic conc just as approximation

    Vmax_bHBDH_f_n: float = 0.05139599967731973  # 0.532 #0.532 # 0.9063430122643024 #1.2 # 0.532 # Nielsen 1973, check units
    Vmax_bHBDH_r_n: float = 0.012848999919329931  # 0.665 #0.665 # 0.5358569280430245 #0.4 # 0.665 # Nielsen 1973, check units
    # Keq_bHBDH_n  0.033 # Nielsen 1973

    # Km_AcAc_BHBD_n = 0.39 # 0.26784852162653866 #0.39 mM   # brain mito Dombrowski 1977
    # Km_NADH_BHBD_n = 0.05 #mM   # brain mito Dombrowski 1977
    # Km_NAD_B_HBD_n = 0.39 # 0.17691521110119537 # 0.39 mM # brain mito, similar in brain and liver Dombrowski 1977
    # Km_betaHB_BHBD_n = 0.45 # 0.4574168440640211 #1.98 #mM #brain mito, similar in brain and liver Dombrowski 1977
    # Ki_NADH_BHBD_r_n = 0.3 # 0.38858801604311016 # 0.22 # mM in direction AcAc to bHB # brain mito Dombrowski 1977
    # Ki_NAD_B_HBD_f_n = 0.45 # 1.0508306759981987 # 1.5 # mM Nielsen 1973

    Km_AcAc_BHBD_n: float = (
        0.2  # 0.45 #0.39 # 0.26784852162653866 #0.39 mM   # brain mito Dombrowski 1977
    )
    Km_NADH_BHBD_n: float = 0.05  # mM   # brain mito Dombrowski 1977
    Km_NAD_B_HBD_n: float = 0.2  # 0.39 # 0.17691521110119537 # 0.39 mM # brain mito, similar in brain and liver Dombrowski 1977
    Km_betaHB_BHBD_n: float = (
        0.45  # 0.4574168440640211 #1.98 #mM #brain mito, similar in brain and liver Dombrowski 1977
    )
    Ki_NADH_BHBD_r_n: float = 0.39  # 0.3 # 0.38858801604311016 # 0.22 # mM in direction AcAc to bHB # brain mito Dombrowski 1977
    Ki_NAD_B_HBD_f_n: float = 0.45  # 1.0508306759981987 # 1.5 # mM Nielsen 1973

    ################################

    # SCOT_n: SCOT_n(SUCCOAmito_n,AcAc_n,AcAcCoA_n,SUCmito_n), SUCCOAmito_n + AcAc_n  ⇒  AcAcCoA_n + SUCmito_n

    VmaxfSCOT_n: float = 2.6842893020795207  # 1.68 # 1.67 #mM/s # calc from kcat from WhiteJencks and conc of SCOT (gene OXCT1) in mol atlas
    VmaxrSCOT_n: float = 0.08787851881807955  # 0.055 #0.08 # 0.08 adj for conc #0.12  # mM/s # calc from kcat from WhiteJencks and conc of SCOT (gene OXCT1) in mol atlas

    Km_AcAc_SCOT_n: float = 0.25  # 0.16 #mM    # or 0.2 mM in Hersh (ref from White Jencks 1975)
    Km_AcAcCoA_SCOT_n: float = 0.19  # mM   # or 0.93 mM in Hersh (ref from White Jencks 1975)
    Km_SUC_SCOT_n: float = (
        23.0  # mM   # Km_Succinate_SCOT_n or 36 mM in Hersh (ref from White Jencks 1975)
    )
    Km_SucCoA_SCOT_n: float = 4.2  # mM
    Ki_AcAc_SCOT_n: float = 0.78  # 0.29 #mM  # or 0.78 mM in Hersh (ref from White Jencks 1975)
    Ki_AcAcCoA_SCOT_n: float = 0.033  # mM     # or 0.17 mM in Hersh (ref from White Jencks 1975)
    Ki_SUC_SCOT_n: float = (
        0.54  # mM    # Ki_Succinate_SCOT_n or 1.0 mM in Hersh (ref from White Jencks 1975)
    )
    Ki_SucCoA_SCOT_n: float = 2.4  # mM   # or 1.9 mM in Hersh (ref from White Jencks 1975)

    # combo f r as SCOT_n() for TD chem pot bigg: OCOAT1m

    ################################

    # thiolase (gene ACAT1)

    # thiolase_n(CoAmito_n,AcAcCoA_n), CoAmito_n + AcAcCoA_n ⇒ 2AcCoAmito_n
    # bigg: 2.0 accoa_m → aacoa_m + coa_m

    # also can adjust for brain thiolase activity is 8% of heart thiolase activity # table 1 from Yang 1987

    # Vmax_thiolase_f_n = 2.13 #0.5 # approx #2.13 # mM/s # Gilbert: kf is 360 sec-1 # 360*exp(1.78)*1e-3

    # #Vmax_thiolase_r_n = 2.37e-5 #Gilbert: kr is 4e-3 sec-1  # 4e-3*exp(1.78)*1e-3

    # #Km_AcCoA_thiolase_r_n = 0.237 #mM (rat liver) # Huth 1982
    # #Km_AcAcCoA_thiolase_r_n = 0.035 #mM #35 uM (peroxisomes), 80 uM (cytosol) # Antonenkov2000 FEBS

    # Km_AcAcCoA_thiolase_f_n = 0.021 #0.021 #mM #21.0 uM # Gilbert thiolase II heart (ketone bodies utilization) # 0.01 mM Huth 1982 # 9 uM (peroxisomes), 16 uM (cytosol) # Antonenkov2000 FEBS
    # #Km_AcCoA_thiolase_f_n = 0.0085 #mM #8.5 uM # Gilbert thiolase II heart (ketone bodies utilization) # 0.09 mM (rat liver) # Huth 1982
    # Km_CoA_thiolase_f_n = 0.056 #0.056 #mM #56.0 uM    # Gilbert thiolase II heart (ketone bodies utilization) #0.025 mM Huth 1982 # 8 uM (peroxisomes), 20 uM (cytosol) # Antonenkov2000 FEBS
    # Ki_CoA_thiolase_f_n =  0.05 #mM Huth 1982
    # #Ki_AcAcCoA_thiolase_r_n = 0.0016 #mM Huth 1982

    Vmax_thiolase_f_n: float = (
        1.0  # 2.13 #0.5 # approx #2.13 # mM/s # Gilbert: kf is 360 sec-1 # 360*exp(1.78)*1e-3
    )

    # Vmax_thiolase_r_n = 2.37e-5 #Gilbert: kr is 4e-3 sec-1  # 4e-3*exp(1.78)*1e-3

    # Km_AcCoA_thiolase_r_n = 0.237 #mM (rat liver) # Huth 1982
    # Km_AcAcCoA_thiolase_r_n = 0.035 #mM #35 uM (peroxisomes), 80 uM (cytosol) # Antonenkov2000 FEBS

    Km_AcAcCoA_thiolase_f_n: float = 0.021  # 0.021 #mM #21.0 uM # Gilbert thiolase II heart (ketone bodies utilization) # 0.01 mM Huth 1982 # 9 uM (peroxisomes), 16 uM (cytosol) # Antonenkov2000 FEBS
    # Km_AcCoA_thiolase_f_n = 0.0085 #mM #8.5 uM # Gilbert thiolase II heart (ketone bodies utilization) # 0.09 mM (rat liver) # Huth 1982
    Km_CoA_thiolase_f_n: float = 0.056  # 0.056 #mM #56.0 uM    # Gilbert thiolase II heart (ketone bodies utilization) #0.025 mM Huth 1982 # 8 uM (peroxisomes), 20 uM (cytosol) # Antonenkov2000 FEBS
    Ki_CoA_thiolase_f_n: float = 0.05  # mM Huth 1982
    # Ki_AcAcCoA_thiolase_r_n = 0.0016 #mM Huth 1982

    # eq type based on eq18 https://www.qmul.ac.uk/sbcs/iubmb/kinetics/ek4t6.html#p52

    # thiolase_n1 = Vmax_thiolase_f_n*CoAmito_n0*AcAcCoA_n0 / ( Ki_CoA_thiolase_f_n * Km_AcAcCoA_thiolase_f_n + Km_AcAcCoA_thiolase_f_n*CoAmito_n0 +     Km_CoA_thiolase_f_n*AcAcCoA_n0 + CoAmito_n0*AcAcCoA_n0)


@dataclass
class Lactate:
    # LAC
    # Jolivet, Calvetti, Simpson, DiNuzzo...

    # LDH
    # # LDH a
    # VmfLDH_a = 780.0 #Winter2017 #4160.00 #Calvetti 1110. # DiNuzzo # 1.59 #Jolivet2015
    # VmrLDH_a = 32.0 #Winter2017 #3245.00 #Calvetti # 25. # DiNuzzo #0.071 # Jolivet pdf # 0.099 Joliivet matlab
    # # LDH n
    # VmfLDH_n = 2000. #Winter2017 #1436.00 #Calvetti #2000. # DiNuzzo 72.3 #Jolivet2015
    # VmrLDH_n = 15. #Winter2017  #1579.83 #Calvetti # 44.8 # DiNuzzo 0.72 #  Jolivet pdf   # 0.768 Joliivet matlab

    # KeqLDH = 1.62*(10^11) M^(-1) # https://doi.org/10.3389/fnins.2015.00022 # The equilibrium constant is strongly in favor of La− (1.62 × 10^11 M^−1) (Lambeth and Kushmerick, 2002)

    # OBrien2007 DOI 10.1007/s11064-006-9132-9
    # The main difference in LDH kinetics between the neuronal and glial preparations is found in the rates of the reverse reaction,
    # conversion of lactate to pyruvate,
    # which was more than two-fold higher in synaptosol than in astrocytes,
    # with Vmax values of 268 lmol/min/ mg protein versus 123 lmol/min/mg protein, respectively.

    # LDH a: Berndt2018 (astrocytes express liver isoform LDH5)
    # LDH n: Berndt2015

    # LDH
    # Params and mechanism from OBrien2007 DOI 10.1007/s11064-006-9132-9 eq derived according to mechanism + Calvetti2018 for redox dependence

    # # LDH a
    # nu_LDH1f_a = 0.1 #0.01 # adj for redox ratio diff #0.1 #Calvetti2018
    # VmfLDH1_a = 7816.67 #4160.0 #Calvetti2018  # 1876 umol/min/mg protein OBrien2007 -> 1000*1876*0.25/60 = 7816.67 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    # KmLDH1pyr_a = 0.084 # OBrien2007 #6.24 #Calvetti2018

    # nu_LDH1r_a = 10. #100. # adj for redox ratio diff # 10.0 #Calvetti2018
    # VmrLDH1_phase1_a = 225.0 #single phased 3245.0 #Calvetti2018   # 54 umol/min/mg protein OBrien2007 -> 1000*54*0.25/60 = 225 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    # VmrLDH1_phase2_a = 512.5 # 123 umol/min/mg protein OBrien2007 -> 1000*123*0.25/60 = 512.5 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037

    # KmLDH1lac_phase1_a = 1.5 # OBrien2007
    # KmLDH1lac_phase2_a = 8.6 # OBrien2007

    # # LDH n  LDH5_synaptic + LDH1_n
    # nu_LDH5f_n = 0.1 #0.01 # adj for redox ratio diff # 0.1 #Calvetti2018
    # VmfLDH5_n = 4845.83  # 1163 umol/min/mg protein OBrien2007 -> 1000*1163*0.25/60 = 4845.83  mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    # KmLDH5pyr_n = 0.0296 # OBrien2007 #6.24 #Calvetti2018

    # nu_LDH5r_n = 10. #100. # adj for redox ratio diff # 10.0 #Calvetti2018
    # VmrLDH5_phase1_n = 533.33  # 128 umol/min/mg protein OBrien2007 -> 1000*128*0.25/60 = 533.33 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    # VmrLDH5_phase2_n = 1116.67  # 268 umol/min/mg protein OBrien2007 -> 1000*268*0.25/60 = 1116.67 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037

    # KmLDH5lac_phase1_n = 1.73  # OBrien2007
    # KmLDH5lac_phase2_n = 7.77  # OBrien2007

    # adj Vmax for abs val at relevant scale?

    # Params and mechanism from OBrien2007 DOI 10.1007/s11064-006-9132-9 eq derived according to mechanism + Calvetti2018 for redox dependence

    # LDH a
    VmfLDH1_a: float = 7816.67  # 4160.0 #7816.67 #4160.0 #Calvetti2018  # 1876 umol/min/mg protein OBrien2007 -> 1000*1876*0.25/60 = 7816.67 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    VmrLDH1_phase1_a: float = 225.0  # single phased 3245.0 #Calvetti2018   # 54 umol/min/mg protein OBrien2007 -> 1000*54*0.25/60 = 225 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    VmrLDH1_phase2_a: float = 512.5  # 123 umol/min/mg protein OBrien2007 -> 1000*123*0.25/60 = 512.5 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037

    KmLDH1pyr_a: float = 0.084  # OBrien2007 #6.24 #Calvetti2018
    KmLDH1lac_phase1_a: float = 1.5  # OBrien2007
    KmLDH1lac_phase2_a: float = 8.6  # OBrien2007

    nu_LDH1f_a: float = 0.1  # 0.01 # adj for redox ratio diff #0.1 #Calvetti2018

    # LDH n  LDH5_synaptic + LDH1_n
    VmfLDH1_n: float = 7816.67  # 4160.0 #7816.67 #4160.0 #Calvetti2018  # 1876 umol/min/mg protein OBrien2007 -> 1000*1876*0.25/60 = 7816.67 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    VmrLDH1_phase1_n: float = 225.0  # single phased 3245.0 #Calvetti2018   # 54 umol/min/mg protein OBrien2007 -> 1000*54*0.25/60 = 225 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    VmrLDH1_phase2_n: float = 512.5  # 123 umol/min/mg protein OBrien2007 -> 1000*123*0.25/60 = 512.5 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037

    KmLDH1pyr_n: float = 0.084  # OBrien2007 #6.24 #Calvetti2018
    KmLDH1lac_phase1_n: float = 1.5  # OBrien2007
    KmLDH1lac_phase2_n: float = 8.6  # OBrien2007

    nu_LDH1f_n: float = 0.1  # 0.01 # adj for redox ratio diff #0.1 #Calvetti2018

    VmfLDH5_n: float = (
        0.999637815739898 * 4845.83
    )  # 1163 umol/min/mg protein OBrien2007 -> 1000*1163*0.25/60 = 4845.83  mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    VmrLDH5_phase1_n: float = (
        0.999637815739898 * 533.33
    )  # 128 umol/min/mg protein OBrien2007 -> 1000*128*0.25/60 = 533.33 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037
    VmrLDH5_phase2_n: float = (
        0.999637815739898 * 1116.67
    )  # 268 umol/min/mg protein OBrien2007 -> 1000*268*0.25/60 = 1116.67 mM/s # *0.25 from Nazaret2009 doi:10.1016/j.jtbi.2008.09.037

    nu_LDH5f_n: float = 0.1  # 0.01 # adj for redox ratio diff # 0.1 #Calvetti2018

    KmLDH5pyr_n: float = 0.0296  # OBrien2007 #6.24 #Calvetti2018
    KmLDH5lac_phase1_n: float = 1.73  # OBrien2007
    KmLDH5lac_phase2_n: float = 7.77  # OBrien2007

    # art -> cap
    C_Lac_a: float = 0.75  # 0.55 #0.55 - 0.10113109309463841 #0.6 #0.82 #0.55 #0.815 #Lac_b0 #0.82 #Lac_b0 - 0.10113109309463841 #0.82 #1.22 #1.6 #0.82 #1.222 # 0.5 #1.225 #1.22 #1.25 #1.0 #0.85 # #0.82 #0.5 Jolivet2015 # 1. #0.9 #1.0 # Leegsma-Vogt PMID: 11746404 #0.82 # set slightly higher than Lac_b from http://dx.doi.org/10.1016/j.cmet.2015.10.010

    # using simple transport equations for Lac, because we don't model precisely H which are important for equations (like equations in DiNuzzo)

    # cap -> ecs
    TbLac: float = (
        (1 / 0.0275) * 0.3
    )  # 0.28 #0.17 # Calvetti #0.00587 # Winter2017 0.3 #0.275 # 0.25 #Jolivet2015 0.3 # Jolivet matlab #0.29 # 0.26 ce 0.3 eb DiNuzzo2010 DiNuzzo2010_1.pdf # 0.00587 Winter2017 #0.25 #Jolivet pdf #0.17 # mM/s
    KbLac: float = 1.0  # 5. #3.5 #1.0 #1.87 #1.0 #Jolivet, Leegsma-Vogt PMID: 11746404 #5.00 # mM Calvetti # 0.5 Winter2017 # 3.5-10 mM Perez-Escuredo https://doi.org/10.1016/j.bbamcr.2016.03.013

    # ecs <-> a
    # Jolivet2015, Calvetti2018
    TaLac: float = (
        (1 / 0.8) * 107.0
    )  # 0.035 #1.04167 #0.250 umol/min/mg Broer et al., 1997 DOI: 10.1002/jnr.20294 -> 1000*0.250*0.25/60 = 1.04167 mM/s # *0.25 from Nazaret2009    #66.67 #Calvetti #0.057 # Winter2017 # 107. #Jolivet matlab #106.1 #Jolivet pdf #66.67 Calvetti # ecsBA2a: 0.03 mM/s DiNuzzo2010, a2ecsAN: 0.04 mM/s DiNuzzo2010, ecsBA2a:1.2e-15 mmol/sec Simpson2007, a2ecsAN: 1.5e-14 mmol/sec Simpson 2007
    Km_Lac_a: float = 3.5  # Jolivet2015 #6.0 # 0.5 Winter2017  #3.5-10.0 mM https://doi.org/10.1016/j.bbamcr.2016.03.013 # 3.5-7.0 mM from Dienel 2019 https://doi.org/10.1002/jnr.24387   #15.0 # par[35]

    # ecs <-> n
    TnLac: float = (
        (1 / 0.44) * 23.5
    )  # 0.07 #66.67 #Calvetti # 0.2175 #Winter2017 # 23.5 #Jolivet matlab #24.3 Jolivet pdf #66.67 Calvetti# 0.07 mM/s DiNuzzo2010, Simpson 2007 predicted: 4.9e-15 mmol/sec
    Km_LacTr_n: float = 0.74  # Jolivet2015 #0.6 # 0.5 Winter2017  # 0.5-0.75 mM from https://doi.org/10.1016/j.bbamcr.2016.03.013 # 0.7 from Dienel 2019 https://doi.org/10.1002/jnr.24387     # 0.025 # par[37]

    TMaxLACgc: float = (1 / 0.022) * 2.43e-03
    KtLACgc: float = 1.0

    # ecs diffusion
    betaLacDiff: float = 0  # 0.001 # s-1 www.pnas.org􏱵cgi􏱵doi􏱵10.1073􏱵pnas.0605864104
    # Lac_ecs0 = Lac_ecs0

    VmfLDH_a: float = 8.74949881831907  # 8.445290697870174 #0.9722314374674746*1124.6166207771603 #1486.8293841083846 # 1.71
    # VmrLDH_a = 0.4331118732235805 # 0.9999030676455061*4.0693155124381875*1.107525198132424*0.099  #0.9722314374674746*67.2 #0.050693455630342395 #0.08044909945699166 # 0.099

    VmfLDH_n: float = 241.739831262545  # 226.35715419383556 #0.39617499995813404*4710.989517511934 #6059.141369229505 #78.1
    # VmrLDH_n = 0.7556440067499692 #0.999978541778008*0.9713032773071247*1.1049568944911459*0.768  #0.39617499995813404*36.18 #40.273541408198604*0.8929243326451762 #2.4067213774881893 #0.768

    KeLDH_a: float = 0.046994407267851  # 0.051284424505696105
    KeLDH_n: float = 0.00329708625924639  # 0.0033382819705485936

    def __post_init__(self):
        self.nu_LDH1r_a: float = (
            1 / self.nu_LDH1f_a
        )  # 10. #100. # adj for redox ratio diff # 10.0 #Calvetti2018
        self.nu_LDH1r_n: float = (
            1 / self.nu_LDH1f_n
        )  # 10. #100. # adj for redox ratio diff # 10.0 #Calvetti2018
        self.nu_LDH5r_n: float = (
            1 / self.nu_LDH5f_n
        )  # 10. #100. # adj for redox ratio diff # 10.0 #Calvetti2018


@dataclass
class MAS:
    # AAT mito n (GOT mito n): psiAAT_n(ASPmito_n,AKGmito_n,OXAmito_n,GLUmito_n), AKGmito_n + ASPmito_n ⇒ OXAmito_n + GLUmito_n

    # Mulukutla2015:  ping pong bi bi mechanism

    VfAAT_n: float = 1.2829135841551298  # after opt #0.1 #0.3 #32.  # Berndt2015 #0.13

    KiAKG_AAT_n: float = 1.9  # Recasens1980 #26.5
    KeqAAT_n: float = (
        0.14  # 0.147 in Berndt2015     # because AAT/GOT near-equilibrium DOI: 10.1002/iub.2367
    )

    KmAKG_AAT_n: float = 1.3  # Magee1971  #0.344 # WILCOCK1973 #3.54 # Recasens1980 #3.22
    KmASP_AAT_n: float = 0.5  # Magee1971  #1.56 # WILCOCK1973 #0.58 # Recasens1980 #0.89
    KiGLU_AAT_n: float = 10.7

    KiASP_AAT_n: float = 263.0  # Recasens1980 #3.9
    KmOXA_AAT_n: float = 0.1  # Magee1971  # 0.1-0.25 Quang Khai HUYNH 1980 #0.088
    KmGLU_AAT_n: float = 3.5  # Magee1971  #16.66 # 10.0-25.0 Quang Khai HUYNH 1980 #32.5

    # AAT/GOT was psiMAAT_n
    # alpha_AAT_n = (1.0 + AKGmito_n/KiAKG_AAT_n)

    # before 27 may2020 psiAAT_n = VfAAT_n*(ASPmito_n*AKGmito_n - OXAmito_n*GLUmito_n/KeqAAT_n) /  ( KmAKG_AAT_n*ASPmito_n +  KmASP_AAT_n*alpha_AAT_n*AKGmito_n + ASPmito_n*AKGmito_n + KmASP_AAT_n*AKGmito_n*GLUmito_n/KiGLU_AAT_n + (  KiASP_AAT_n*KmAKG_AAT_n/(KmOXA_AAT_n*KiGLU_AAT_n)  )*  ( KmGLU_AAT_n*ASPmito_n*OXAmito_n/KiASP_AAT_n + OXAmito_n*GLUmito_n +  KmGLU_AAT_n*alpha_AAT_n*OXAmito_n + KmOXA_AAT_n*GLUmito_n )  )

    # psiAAT_n  = VmaxmitoAAT_n*(ASPmito_n*AKGmito_n-OXAmito_n*GLUmito_n/KeqmitoAAT_n) # it was psiMAAT_n

    # GOT2 and MDH2, enzymes that are usually assumed to be close to equilibrium  DOI: 10.1002/iub.2367

    # psiAAT_n1 = VfAAT_n*(ASPmito_n0*AKGmito_n0 - OXAmito_n0*GLUmito_n0/KeqAAT_n) /  ( KmAKG_AAT_n*ASPmito_n0 +  KmASP_AAT_n*(1.0 + AKGmito_n0/KiAKG_AAT_n)*AKGmito_n0 + ASPmito_n0*AKGmito_n0 + KmASP_AAT_n*AKGmito_n0*GLUmito_n0/KiGLU_AAT_n + (  KiASP_AAT_n*KmAKG_AAT_n/(KmOXA_AAT_n*KiGLU_AAT_n)  )*  ( KmGLU_AAT_n*ASPmito_n0*OXAmito_n0/KiASP_AAT_n + OXAmito_n0*GLUmito_n0 +  KmGLU_AAT_n*(1.0 + AKGmito_n0/KiAKG_AAT_n)*OXAmito_n0 + KmOXA_AAT_n*GLUmito_n0 )  )

    ###############################

    # cMDH n: psicMDH_n(MAL_n,NAD_n,OXA_n,NADH_n), MAL_n + NAD_n ⇒ OXA_n + NADH_n
    # MAS_r01_cMDH_n

    VmaxcMDH_n: float = 11.927187547739674  # after opt #10. #0.16 #

    Keqcmdh_n: float = 3.15e-5  # because MDH near-equilibrium DOI: 10.1002/iub.2367 #0.000402 #
    Kmmalcmdh_n: float = 0.77  # Berndt2015 #0.35 #
    Kmnadcmdh_n: float = 0.05  # Berndt2015
    Kmoxacmdh_n: float = 0.04  # Berndt2015
    Kmnadhcmdh_n: float = 0.05  # Berndt2015

    # # GOT2 and MDH2, enzymes that are usually assumed to be close to equilibrium  DOI: 10.1002/iub.2367

    ###############################

    # psiCAAT_n(ASP_n,AKG_n,OXA_n,GLU_n), ASP_n + AKG_n ⇒ OXA_n + GLU_n
    # MAS_r02_cAAT_n

    VfCAAT_n: float = 0.6248605383756786  # 0.023594697230144117 # after opt #0.3 #32.

    KiAKG_CAAT_n: float = 1.0  # 17.0 # Recasens1980 #0.73 #26.5  # 1-3  KRISTA1972
    KeqCAAT_n: float = (
        0.358  # 0.36    # because AAT/GOT near-equilibrium DOI: 10.1002/iub.2367 #2.5 #1.56
    )

    KmAKG_CAAT_n: float = 0.15  # Magee1971 #0.085 # WILCOCK1973 #0.54 # Recasens1980 # 0.06-0.1 Quang Khai HUYNH 1980 # 0.17 KRISTA1972 #3.22

    KmASP_CAAT_n: float = 6.7  # Magee1971 #1.55 # WILCOCK1973 #1.13  Recasens1980 # 1.81-2.5 Quang Khai HUYNH 1980 # 2.0  KRISTA1972  #0.89

    KiGLU_CAAT_n: float = 10.7

    KiASP_CAAT_n: float = 21.0  # Recasens1980 #3.9

    KmOXA_CAAT_n: float = 0.11  # Magee1971 #0.5 #0.33-0.5  Quang Khai HUYNH 1980 #0.088

    KmGLU_CAAT_n: float = 5.0  # Magee1971  #12.5  #Quang Khai HUYNH 1980 #32.5

    # psiCAAT_n = VmaxcAAT_n*(ASP_n*AKG_n-OXA_n*GLU_n/KeqcAAT_n) #changed to below 27may2020
    # alpha_CAAT_n = (1.0 + AKG_n/KiAKG_CAAT_n)

    ###############################

    # AGC (aralar,citrin) n: psiAGC_n(ASPmito_n,GLU_n,ASP_n,GLUmito_n,MitoMembrPotent_n),  ASPmito_n + GLU_n ⇒ GLUmito_n + ASP_n

    # MAS_r03_AGC_n

    # Berndt2015

    Vmaxagc_n: float = 0.0001830479496983698  # after opt #0.0069
    Km_aspmito_agc_n: float = 0.05
    Km_glu_agc_n: float = 5.6
    Km_asp_agc_n: float = 0.05
    Km_glumito_agc_n: float = 2.8

    # Aspartate/glutamate carrier [64] Berndt 2015
    # Asp_mito + glu_cyt + h_cyt ↔ Asp_cyt + glu_mito + h_mito
    # Vmaxagc_n = 3200.0
    # Keqagc_n =  0.968 # from NEDERGAARD 1991: 7.01/7.24 # hcyt/hext  # was 1.737 in Berndt 2015 - mistake in Berndt2015 ??  # Hcyt_n/Hext #
    # Vmm_n = -0.14 #-140.0 mV
    # Km_aspmito_agc_n = 0.05
    # Km_glu_agc_n = 2.8
    # Km_asp_agc_n = 0.05
    # @reaction_func VAGC_n(ASPmito_n,GLU_n,ASP_n,GLUmito_n) = Vmaxagc_n*(ASPmito_n*GLU_n - ASP_n*GLUmito_n/ exp(-Vmm_n)^(F/(R*T))*Keqagc_n ) / ((ASPmito_n+Km_aspmito_agc_n)*(GLU_n+Km_glu_agc_n) + (ASP_n+Km_asp_agc_n)*(GLUmito_n+Km_glu_agc_n))

    # From DOI: 10.1002/iub.2367:
    # cytosolic Ca stimulation of the aspartate–glutamate transporter
    # It is possible that this calcium stimulation plays a physiological role in heart and brain

    # psiAGC_n1 = Vmaxagc_n*(ASPmito_n0*GLU_n0 - ASP_n0*GLUmito_n0 / ((exp(MitoMembrPotent_n0)^(F/(R*T))) *  (C_H_cyt_n/C_H_mito_n)) ) / ((ASPmito_n0+Km_aspmito_agc_n)*(GLU_n0+Km_glu_agc_n) + (ASP_n0+Km_asp_agc_n)*(GLUmito_n0+Km_glumito_agc_n))

    ###############################

    # MAKGC n: psiMAKGC_n(MAL_n,AKGmito_n,MALmito_n,AKG_n), AKGmito_n + MAL_n ⇒ MALmito_n + AKG_n

    # MAS_r04_MAKGC_n

    Vmaxmakgc_n: float = 0.000262718660265385  # after opt # 0.0005 #0.0004267 #

    # KeqMakgc_n = 2.28
    Km_mal_mkgc_n: float = 0.4
    Km_akgmito_mkgc_n: float = 0.2
    Km_malmito_mkgc_n: float = 0.71
    Km_akg_mkgc_n: float = 0.1

    # psiMAKGC_n1 = Vmaxmakgc_n*( MAL_n0*AKGmito_n0 - MALmito_n0*AKG_n0) / ((MAL_n0+Km_mal_mkgc_n)*(AKGmito_n0+Km_akgmito_mkgc_n)+(MALmito_n0+Km_malmito_mkgc_n)*(AKG_n0+Km_akg_mkgc_n))


@dataclass
class PPP_a:
    ### PPP: Winter2017, Stincone 2015; Nakayama 2005; Sabate 1995 rat liver; Kauffman1969 mouse brain; Mulukutla(2015) Multiplicity of Steady States in Glycolysis and Shift of Metabolic State in Cultured Mammalian Cells. PLoS ONE; Cakir 2007

    # PPP_r01_G6PDH

    VmaxG6PDH_a: float = 477.195127843729  # 478.1665057289348 #0.05 #0.0803931164211058 #0.065 #0.29057 #0.05  #0.29057 # 5.9e-06
    KeqG6PDH_a: float = (
        0.008  # 0.00709854391636249 #0.00548183269281042 #0.004996308250689027 #22906.4
    )
    K_G6P_G6PDH_a: float = 0.03  # 0.0169812873724678 #0.0158229604461531 #6.91392e-5 #0.047 # avg  29-65 uM # 6.91392e-05 W17  # 29-65 uM book Neurochemistry Lajtha 2007 NeurochemistryEnergeticsBook.pdf  # 0.036
    K_NADP_G6PDH_a: float = 0.13  # 0.113800580992371 #0.117925904076472 #1.31616e-05 #0.0105 # avg 4-17 uM  1.31616e-05 # 4-17 uM book Neurochemistry Lajtha 2007 NeurochemistryEnergeticsBook.pdf # 0.0048
    K_GL6P_G6PDH_a: float = 0.0180932  # 0.01 # 0.0001 #0.0180932
    K_NADPH_G6PDH_a: float = 2e-05  # 2.56105031786788E-05 #2.51285420418258E-05 #0.00050314 #0.00015 #0.00050314 #0.0035 #0.00050314 # Ki NADPH = 3.5 uM book Neurochemistry Lajtha 2007 NeurochemistryEnergeticsBook.pdf # Ki 0.0011

    # r02: 6PGL

    Vmax6PGL_a: float = 8.839100733681803  # 8.85709967646198 #0.0008 #0.00788831166500804 #0.039 #0.18 #0.09 #0.184701
    Keq6PGL_a: float = 961.0  # 900.0 #1883.78898381691 #2116.69452134578 #531174.
    K_GL6P_6PGL_a: float = 0.0180932  # 0.1 #0.05 #0.0180932
    K_GO6P_6PGL_a: float = 2.28618

    # r03: GND = 6-Phosphogluconate Dehydrogenase (6PGDH): 6-Phosphogluconate(GO6P) + NADP+ → ribulose 5-phosphate(RU5P) + CO2 +NADPH+H+

    Vmax6PGDH_a: float = 1.7337940118891872e7  # 1.751250837536649e7 #1.09999997755265 #1.24786813651401 #1.25214497008764 #1.0 #1.31377
    Keq6PGDH_a: float = 37.38848579759115  # 36.1122375263804 #38.468548761728 #37.38848579759115 #<calc from diff conc #4.0852e+07
    K_GO6P_6PGDH_a: float = 3.23421e-5  # 0.095 #0.1 #0.045 #0.0292 # 3.23421e-05
    K_NADP_6PGDH_a: float = 0.200000007547866  # 0.0497813299366745 #0.0576096039029965 #3.11043e-6 #0.019 #0.018 #0.015 #0.0135 #3.11043e-06
    K_RU5P_6PGDH_a: float = 0.0537179  # 0.008 #0.0092 #0.008 # 0.01 # 0.0537179
    K_NADPH_6PGDH_a: float = 4.00000000000001e-05  # 1.12019685952319E-06 #4.20356220270474E-06 #0.000207914971003531 #0.000312185665026002 #0.00050314 #0.00022 #0.00050314

    # r04: RKI =  Ribose Phosphate Isomerase (RPI): Ribulose 5-phosphate(RU5P) ↔ ribose 5- phosphate(R5P)

    VmaxRPI_a: float = 0.014902971468358402  # 0.014755585701982987 #1.00292379461223E-05 #1.52507680529037E-05 #0.000821984 #0.0005 #0.00077 # 0.000821984
    KeqRPI_a: float = 35.9999996723297  # 0.126866566749418 #19.3244443714851 # 35.4534 #3.2356652575518643 #3.3 #3.125 # #15. # 35.4534 #0.0282061
    K_RU5P_RPI_a: float = 0.0537179  # 0.8 #0.78 #0.05 #0.0537179
    K_R5P_RPI_a: float = 0.778461  # 9.1 #0.1 #0.01 #0.5 # 0.778461

    # r05: Ribulose Phosphate Epimerase (RPE): Ribulose 5-phosphate(RU5P) ↔ xylulose 5-phosphate(X5P)

    VmaxRPE_a: float = 0.4272424527742825  # 0.4312364583332894 #0.000282932456807714 #0.000613070392724124 #0.00775925 #0.0025 #0.005 #0.00775925
    KeqRPE_a: float = (
        33.0  # 32.6687224847549 #32.2532017229088 #39.2574 #1.95 #1.99 #1.85 #18. #39.2574
    )
    K_RU5P_RPE_a: float = 0.0537179  # 0.85 #0.5 # 0.2 #0.19 # 0.0537179
    K_X5P_RPE_a: float = 0.603002  # 0.5 #0.1 # 0.5 #0.603002

    # r06  Transketolase1

    VmaxTKL1_a: float = 0.004900238015784919  # 0.004851923236920396 #5.64368567678176E-05 #9.9999999977701E-05 #9.94132171852896E-05 #0.000244278 #0.00025 #0.0012 # adj # 0.00244278 #0.000244278
    KeqTKL1_a: float = 9860.43282385396  # 5000.00000000203 #39178.8180651246 #23251.6522242321 #6.748985939209286e6 #1652870.0 #1.65287e+06 #1.62 # doi: https://doi.org/10.1101/2022.02.04.478659 1.65287e+06
    K_X5P_TKL1_a: float = 0.000173625  # 0.2 #0.14 #0.18 #0.0900868125 #avg #0.18 #MCINTYRE,Thornburn,Kuhel1989  #0.000173625
    K_R5P_TKL1_a: float = (
        0.000585387  # 0.3 #0.1502926935 #0.3 #MCINTYRE,Thornburn,Kuhel1989  #0.000585387
    )
    K_GAP_TKL1_a: float = 0.049985901384741  # 0.0999999989783367 # 0.04 #0.168333 #0.15 #0.16 #0.38 #0.2741665 #0.38 #MCINTYRE,Thornburn,Kuhel1989  #0.168333
    K_S7P_TKL1_a: float = (
        0.192807  # 0.19 #0.2 #0.86 #0.5264035 # 0.86 # MCINTYRE,Thornburn,Kuhel1989 #0.192807
    )

    # r07  Transketolase2

    VmaxTKL2_a: float = 0.13463638716265247  # 0.14217744212878244 #1.03590012376634E-05 #1.61989424649748E-05 # 1.39858900748084E-05 #0.000137124 #0.00015 #0.007 # adj #0.000137124
    KeqTKL2_a: float = 0.142052917466236  # 0.233169977422005 #0.0523571502829637 #0.09015406283113593 #0.0777764 #0.5 #0.1 #0.05 #0.08 #0.1 #adj #0.0777764
    K_F6P_TKL2_a: float = (
        1.99901443230202  # 1.35866198941061 #1.46286766935271 #0.0799745 #0.08 #0.34 #0.0799745
    )
    K_GAP_TKL2_a: float = 0.28731529730184  # 0.187782778894276 #0.2 #0.168333 #0.16 #0.38 #0.168333
    K_X5P_TKL2_a: float = 0.603002  # 0.16 #0.603002
    K_E4P_TKL2_a: float = 0.109681  # 0.044 #0.109681

    # r08 Transaldolase (TAL): S7P + GAP ↔ E4P + F6P

    VmaxTAL_a: float = 30.710157982217925  # 32.59368782582155 #5.00000000000037E-06 #0.000243124200741458 #0.0005070714579269 #0.0080394 # 0.007 #0.01 #adj #0.0080394
    KeqTAL_a: float = 0.95  # 0.0999999999999998 #0.0265464507333482 #0.024031729718689693 # 0.323922 #0.3 #0.323922 # 0.95 #
    K_GAP_TAL_a: float = 1.99999999999998  # 0.530662851113242 #1.14526908778254 #0.168333 #0.168333
    K_S7P_TAL_a: float = 0.192807
    K_F6P_TAL_a: float = 5.00000000000008e-05  # 0.00245714807732048 #0.00557726396440652 #0.0799745
    K_E4P_TAL_a: float = 0.109681

    # NADPH oxidase
    k1NADPHox_a: float = 0.005509761591955474  # 0.005596013520709597 #3.43387752876666E-06 #2.39662714394727E-05 #3.78431669786565E-05 #0.000209722 #0.000209722


@dataclass
class PPP_n:
    ### PPP: Winter2017, Stincone 2015; Nakayama 2005; Sabate 1995 rat liver; Kauffman1969 mouse brain; Mulukutla(2015) Multiplicity of Steady States in Glycolysis and Shift of Metabolic State in Cultured Mammalian Cells. PLoS ONE; Cakir 2007

    # PPP_r01_G6PDH

    # ZWF = Glucose 6-phosphate Dehydrogenase (G6PDH):  Glucose 6-phosphate(G6P) + NADP+(NADP) ↔ 6-phospho-glucono-1,5-lactone(GL6P) + NADPH + H+ ###
    VmaxG6PDH_n: float = (
        2413.389592436078  # 0.150144617884625 # 0.130010113583145 #0.53895900801198 #0.586458
    )
    KeqG6PDH_n: float = 0.00674385476573124  # 0.00548183269281042 #0.005002081708789302 #22906.4
    K_G6P_G6PDH_n: float = 0.0109183101365999  # 6.91392e-05 #0.01  #0.0142523987811961 # 0.0158229604461531 #0.0261692706915093 #6.91392e-05
    K_NADP_G6PDH_n: float = (
        0.0835423944062894  # 0.10608175747939 # 0.117925904076472 #0.0621260938598377 #1.31616e-05
    )
    K_GL6P_G6PDH_n: float = 0.0180932  # 0.01
    K_NADPH_G6PDH_n: float = 5.7841990084678e-05  # 2.87650878408365E-05 # 2.51285420418258E-05 #1.05119349399397E-05 #0.00050314

    # r02: 6PGL

    # SOL = 6-Phosphogluconolactonase (6PGL): 6-Phosphoglucono-1,5-lactone(GL6P) + H2 O → 6-phosphogluconate(GO6P)
    Vmax6PGL_n: float = (
        8711.029873731239  # 0.00162744832170299 #0.0779750236619484 #0.300002217429445 #0.373782
    )
    Keq6PGL_n: float = 961.0  # 933.79300277648 #2116.69452134578 #531174.
    K_GL6P_6PGL_n: float = 0.0180932
    K_GO6P_6PGL_n: float = 2.28618

    # r03: GND = 6-Phosphogluconate Dehydrogenase (6PGDH): 6-Phosphogluconate(GO6P) + NADP+ → ribulose 5-phosphate(RU5P) + CO2 +NADPH+H+

    # GND = 6-Phosphogluconate Dehydrogenase (6PGDH): 6-Phosphogluconate(GO6P) + NADP+ → ribulose 5-phosphate(RU5P) + CO2 +NADPH+H+
    Vmax6PGDH_n: float = (
        80.41773386353813  # 2.39373833940569 #2.50428994017528 #2.0000015929249 #2.6574
    )
    Keq6PGDH_n: float = (
        23.4988291155184  # 23.2831288483441 #23.4988291155184 #23.389469865437693 #4.0852e+07
    )
    K_GO6P_6PGDH_n: float = 3.23421e-05
    K_NADP_6PGDH_n: float = 0.0330619252781597  # 0.0576096039029965 #0.199999612436424 #3.11043e-06
    K_RU5P_6PGDH_n: float = 0.0537179
    K_NADPH_6PGDH_n: float = (
        5.2529395568622e-05  # 0.000312185665026002 #2.00000197818523E-05 #0.00050314
    )

    # r04: RKI =  Ribose Phosphate Isomerase (RPI): Ribulose 5-phosphate(RU5P) ↔ ribose 5- phosphate(R5P)
    # RKI =  Ribose Phosphate Isomerase (RPI): Ribulose 5-phosphate(RU5P) ↔ ribose 5- phosphate(R5P)
    VmaxRPI_n: float = 0.013057366069767283  # 2.27562615941395E-06 #1.52507680529037E-05 #0.0010000001580841 #0.00165901
    KeqRPI_n: float = 0.587090549959032  # 19.3244443714851 #35.4534
    K_RU5P_RPI_n: float = 0.0537179
    K_R5P_RPI_n: float = 0.778461

    # r05: Ribulose Phosphate Epimerase (RPE): Ribulose 5-phosphate(RU5P) ↔ xylulose 5-phosphate(X5P)
    # R5PE has about 10‐fold higher activity in mammalian tissue than does R5PI (Novello and McLean, 1968) - book Neurochemistry Lajtha 2007 NeurochemistryEnergeticsBook.pdf
    # Ribulose Phosphate Epimerase (RPE): Ribulose 5-phosphate(RU5P) ↔ xylulose 5-phosphate(X5P)
    VmaxRPE_n: float = 0.2039985464986835  # 3.78141492912804E-05 #0.000613070392724124 #0.0100000519904446 #0.0156605
    KeqRPE_n: float = 34.9820646657167  # 32.2532017229088 #39.2574
    K_RU5P_RPE_n: float = 0.0537179
    K_X5P_RPE_n: float = 0.603002

    # r06  Transketolase1

    # Transketolase TKL 1,2
    VmaxTKL1_n: float = 0.004950133634259906  # 4.99999381232524E-05 #9.94132171852896E-05 #0.000100000000723543 #0.000493027
    KeqTKL1_n: float = 9860.43282385396  # 23251.6522242321 #6.136173332909908e6 #1652870.0
    K_X5P_TKL1_n: float = 0.000173625
    K_R5P_TKL1_n: float = 0.000585387
    K_GAP_TKL1_n: float = 0.00499217405386077  # 0.0199199125588176 #0.100000072700887 #0.168333
    K_S7P_TKL1_n: float = 0.192807

    # r07  Transketolase2

    VmaxTKL2_n: float = 0.030468555594855798  # 5.61436923030841E-06 #1.39858900748084E-05 #0.000121191639770347 #0.000276758
    KeqTKL2_n: float = (
        0.142052917466236  # 0.0585732500846428 #0.07821611436297593 #0.07776450379275156 #0.0777764
    )
    K_F6P_TKL2_n: float = 1.38310526172865  # 1.46286766935271 # 0.458132513897045 #0.0799745
    K_GAP_TKL2_n: float = 0.123421366286679  # 0.0998077937106258 #0.892390735815738 #0.168333
    K_X5P_TKL2_n: float = 0.603002
    K_E4P_TKL2_n: float = 0.109681

    # r08 Transaldolase (TAL): S7P + GAP ↔ E4P + F6P

    # Transaldolase (TAL): S7P + GAP ↔ E4P + F6P

    VmaxTAL_n: float = 77.12873595245502  # 0.000672290592103076 #0.0010141429158538 #0.00500000013544425 #0.0162259
    KeqTAL_n: float = 3.0  # 0.0649345422904358 #0.0153189035204859 #0.015129601518014119 #0.323922
    K_GAP_TAL_n: float = 1.434093758861  # 1.14526908778254 #0.899999415343457 #0.168333
    K_S7P_TAL_n: float = 0.192807
    K_F6P_TAL_n: float = 0.00045967540870832  # 0.00557726396440652 #0.015000019459948 #0.0799745
    K_E4P_TAL_n: float = 0.109681

    # NADPH oxidase
    k1NADPHox_n: float = (
        0.0009369376443550519  # 5.53110470372277E-06 #3.78431669786565E-05 #0.000423283 #0.00281384
    )


@dataclass
class PyrCarb:
    # PYRCARB pyruvate carboxylase:  PYRmito_a + ATPmito_a ⇒ OXAmito_a + ADPmito_a

    VmPYRCARB_a: float = 0.00755985436706299  # 0.00770594375034992 # < from opt a #0.1 #11.97

    muPYRCARB_a: float = 0.01
    CO2_mito_a: float = 1.2
    KeqPYRCARB_a: float = 1.0
    KmPYR_PYRCARB_a: float = 0.05638211229110231  # < from opt a #0.22
    KmCO2_PYRCARB_a: float = 3.2

    # psiPYRCARB_a1 = ( (ATPmito_a0/ADPmito_a0)/(muPYRCARB_a +  (ATPmito_a0/ADPmito_a0)))*VmPYRCARB_a*(PYRmito_a0*CO2_mito_a - OXAmito_a0/KeqPYRCARB_a)/(  KmPYR_PYRCARB_a*KmCO2_PYRCARB_a +  KmPYR_PYRCARB_a*CO2_mito_a + KmCO2_PYRCARB_a*PYRmito_a0 + CO2_mito_a*PYRmito_a0)    # PYRmito_a + ATPmito_a ⇒ OXAmito_a + ADPmito_a


@dataclass
class PyrTrCytoMito:
    # PyrTr cyto2mito

    # Berndt2015,Jolivet2015

    # Vmax_PYRtrcyt2mito_n = 6.0 #12.8 #128. #1.1 #1. #5. # 128.
    # Vmax_PYRtrcyt2mito_nH = 158005. #158010.  #128.
    Vmax_PYRtrcyt2mito_nH: float = 7257.23890975437  # 7700.0

    KmPyrCytTr_na: float = 0.15  # 0.15  # Berndt2015 #0.015 # 0.63 BerndtHepatokin
    KmPyrMitoTr_na: float = 0.15  # 0.15

    # Vmax_PYRtrcyt2mito_a = 3.0 #6. #3. #6.4 #12.8 #128. # 1.1 #1. #5. # 128.
    # Vmax_PYRtrcyt2mito_aH = 158005. #158010.  #128.
    Vmax_PYRtrcyt2mito_aH: float = 7961.37240852442  # 7700.0

    KmPyrCytTr_n: float = 0.15  # 0.15  # Berndt2015
    KmPyrMitoTr_n: float = 0.15  # 0.15
    KmPyrCytTr_a: float = 0.15  # 0.15  # Berndt2015
    KmPyrMitoTr_a: float = 0.15  # 0.15


@dataclass
class TCA:
    # PDH

    # r01 PDH

    # “lower pyruvate dehydrogenase activity in astrocytes” (Glucose utilization: still in the synapse Stoessl)

    # Berndt2012, Zhang2018
    # VmaxPDHCmito_n = 0.719 #0.85 #1. #10000.
    # # AmaxCaMitoPDH_n = 1.7
    # # Km_a_CaMito_PDH_n = 0.001
    # KmPyrMitoPDH_n = 0.045 #0.09     # 0.002 - 0.25 Brenda relevant species
    # KmNADmitoPDH_na = 0.046 #0.036           # 0.022 - 0.07 Brenda relevant species
    # KmCoAmitoPDH_n = 0.008 #0.0047   # 0.004-0.0761 Brenda relevant species

    VmaxPDHCmito_n: float = 2.67222326259307  # 2.8 # 2.9164794313209406 # 2.9164794313209406 # 2.916873266724163 # 2.798321254695664 # 2.15 #2.17 #2.18good #2.1 - slightly lower #2.2 - almost, slightly higher #2.0 -a bit too low #0.9999567804941919*2.4 -a bit too high # 2.4 almost #3.0 #3.112889016753674 #4.705913926611023 # 3.0 #2.0 #1.0 #0.1 #
    # 4.705913926611023 # 3.112889016753674  # 4.575 #4.57 slightly down #4.56 down # 4.58 slightly up #4.6 # 4.7 #3.04 #4.25 #4.22 #0.825 #0.719 #0.85 #1. #10000.

    # AmaxCaMitoPDH_n = 1.7
    # Km_a_CaMito_PDH_n = 0.001

    KmPyrMitoPDH_n: float = (
        0.068  # 0.045 #0.09 #0.045 #0.09    # 0.002 - 0.25 Brenda relevant species
    )
    KmNADmitoPDH_na: float = 0.036  # 0.046 #0.036           # 0.022 - 0.07 Brenda relevant species

    KmCoAmitoPDH_n: float = (
        0.007684422893475319  # 0.0047 #0.008 #0.0047   # 0.004-0.0761 Brenda relevant species
    )

    VmaxPDHCmito_a: float = 2.79810789599674  # 2.8 # 3.06 # 3.06  # from opt: 2.6496686498982145 # 3.06 #3.0575 #3.065 #3.1 #3.1987080122030234 #3.112889016753674 #2.6496686498982145  # before opt: 4.0  #0.677 #0.8 #0.5 #1. #10000. #4.0  #0.677 #0.8 #0.5 #1. #10000.
    # AmaxCaMitoPDH_a = 1.7
    # Km_a_CaMito_PDH_a = 0.001
    KmPyrMitoPDH_a: float = 0.068  # 0.02 # from opt: 0.012933056341060813 0.02 # 0.0189 #0.03 #0.012933056341060813 # before opt: 0.04 #0.0252         # 0.002 - 0.25 Brenda relevant species
    # KmNADmitoPDH_na = 0.046 #0.036 #0.035          # 0.022 - 0.07 Brenda relevant species
    KmCoAmitoPDH_a: float = 0.0047  # 0.0149         # 0.004-0.0761 Brenda relevant species

    # # psiPDH_n1 = VmaxPDHCmito_n*(1.0+AmaxCaMitoPDH_n*CaMito_n0/(CaMito_n0 + Km_a_CaMito_PDH_n)) * (PYRmito_n0/(PYRmito_n0+KmPyrMitoPDH_n)) * (NADmito_n0/(NADmito_n0 + KmNADmitoPDH_na)) * (CoAmito_n0/(CoAmito_n0 + KmCoAmitoPDH_n))
    # # psiPDH_a1 = VmaxPDHCmito_a*(1.0+AmaxCaMitoPDH_a*CaMito_a0/(CaMito_a0 + Km_a_CaMito_PDH_a)) * (PYRmito_a0/(PYRmito_a0+KmPyrMitoPDH_a)) * (NADmito_a0/(NADmito_a0 + KmNADmitoPDH_na)) * (CoAmito_a0/(CoAmito_a0 + KmCoAmitoPDH_a))

    # psiPDH_n1 = VmaxPDHCmito_n* (PYRmito_n0/(PYRmito_n0+KmPyrMitoPDH_n)) * (NADmito_n0/(NADmito_n0 + KmNADmitoPDH_na)) * (CoAmito_n0/(CoAmito_n0 + KmCoAmitoPDH_n))
    # psiPDH_a1 = VmaxPDHCmito_a* (PYRmito_a0/(PYRmito_a0+KmPyrMitoPDH_a)) * (NADmito_a0/(NADmito_a0 + KmNADmitoPDH_na)) * (CoAmito_a0/(CoAmito_a0 + KmCoAmitoPDH_a))

    # println(psiPDH_n1)
    # println(psiPDH_a1)

    ##############################################

    # r02: Citrate synthase: Oxa + AcCoA -> Cit # Berndt 2015

    # VmaxCSmito_n =  0.2 #0.4833  # 0.17 #0.165 #0.2 #0.4833 #0.2 #adj #1280.0 #0.116 # doi:10.1046/j.1471-4159.2003.01871.x 0.116 umol/min/mg
    # KmOxaMito_n = 0.005   # 0.005 mM brain https://pubmed.ncbi.nlm.nih.gov/4201777/
    # KiCitMito_n = 1.0 #3.7 #1.6 # 3.7  # 0.037
    # KmAcCoAmito_n = 0.0048   # 0.0048 mM brain https://pubmed.ncbi.nlm.nih.gov/4201777/
    # KiCoA_n = 0.02 # 0.025 # Berndt 2012,2015 #0.067 #0.00025

    VmaxCSmito_n = 0.4689427553439143  # 0.4645 # 0.4722162450277844 # 0.4724918447819282 # 0.5112293698278352 # 0.4645 # 0.57 #0.55 #0.65 #0.8 #0.4968890850459*1.0 #0.2 #0.4833 # 1.0 #0.2 #0.4833   # 0.17 #0.165 #0.2 #0.4833 #0.2 #adj #1280.0 #0.116 # doi:10.1046/j.1471-4159.2003.01871.x 0.116 umol/min/mg

    KmOxaMito_n: float = 0.005  # 0.005 mM brain https://pubmed.ncbi.nlm.nih.gov/4201777/
    KiCitMito_n: float = 1.0  # 3.7 #1.6 # 3.7  # 0.037
    KmAcCoAmito_n: float = 0.0048  # 0.0048 mM brain https://pubmed.ncbi.nlm.nih.gov/4201777/
    KiCoA_n: float = 0.02  # 0.025 # Berndt 2012,2015 #0.067 #0.00025

    VmaxCSmito_a: float = 0.7181459358580017  # 0.27867260457961346*1.9413118399434741 # 1.9413118399434741 # < from opt a 2.0 #0.2 #0.4833  # 0.17 #0.165 # 0.2 # 0.4833 #0.116 umol/min/mg   # doi:10.1046/j.1471-4159.2003.01871.x  #0.2 #adj  #1280.0

    KmOxaMito_a: float = 0.004  # 0.005   # 0.005 mM brain https://pubmed.ncbi.nlm.nih.gov/4201777/
    KiCitMito_a: float = 1.0  # 3.7 #1.6 # Berndt2018 #3.7
    KmAcCoAmito_a: float = 0.0048  # 0.0048 mM brain https://pubmed.ncbi.nlm.nih.gov/4201777/
    KiCoA_a: float = 0.02  # 0.025 # Berndt 2012,2015

    # psiCS_n1 = VmaxCSmito_n*(OXAmito_n0/(OXAmito_n0 + KmOxaMito_n*(1.0 + CITmito_n0/KiCitMito_n))) * (AcCoAmito_n0/(AcCoAmito_n0 + KmAcCoAmito_n*(1.0+CoAmito_n0/KiCoA_n)))
    # psiCS_a1 = VmaxCSmito_a*(OXAmito_a0/(OXAmito_a0 + KmOxaMito_a*(1.0 + CITmito_a0/KiCitMito_a))) * (AcCoAmito_a0/(AcCoAmito_a0 + KmAcCoAmito_a*(1.0+CoAmito_a0/KiCoA_a)))

    # println(psiCS_n1)
    # println(psiCS_a1)

    ##############################################

    # r03: aconitase, CITmito_a  ⇒ ISOCITmito_a

    # VmaxAco_n = 2. #5. #10. #5. #100. #200. #16000.0
    # KeqAco_na = 0.11 #0.067 #Berndt2015 #0.1 #Berndt2018
    # KmCitAco_n = 0.48 # GUARRIERO-BOBYLEVA 1973
    # KmIsoCitAco_n = 0.12 # GUARRIERO-BOBYLEVA 1973

    VmaxAco_n: float = 25.611147830094392  # 25.782707422203963 # 25.797754993950043 # 29. # 23.433 #29. #28.0 #2.35 # 2.3 #2. #5. #10. #5. #100. #200. #16000.0 #29. #28.0 #2.35 # 2.3 #2. #5. #10. #5. #100. #200. #16000.0
    KeqAco_na: float = 0.11  # 0.067 #Berndt2015 #0.1 #Berndt2018
    KmCitAco_n: float = 0.48  # GUARRIERO-BOBYLEVA 1973
    KmIsoCitAco_n: float = 0.12  # GUARRIERO-BOBYLEVA 1973

    # Cit <-> IsoCit # Berndt 2015
    VmaxAco_a: float = 9.438075110105698  # 26.99 # 29. #2. #5. # 10. #5. # 100. #200. #16000.0
    # KeqAco_na = 0.11 #0.067 #0.1 #Berndt2018
    KmCitAco_a: float = 0.48  # GUARRIERO-BOBYLEVA 1973
    KmIsoCitAco_a: float = 0.12  # GUARRIERO-BOBYLEVA 1973

    # VmaxAco_n = 2. #16000.0
    # KeqAco_na = 0.067 # par[511]
    # KmCitAco_n = 0.48 # GUARRIERO-BOBYLEVA 1973
    # KmIsoCitAco_n = 0.12 # GUARRIERO-BOBYLEVA 1973

    # # Cit <-> IsoCit # Berndt 2015
    # VmaxAco_a = 2. #16000.0
    # KeqAco_na = 0.067
    # KmCitAco_a = 0.48 # GUARRIERO-BOBYLEVA 1973
    # KmIsoCitAco_a = 0.12 # GUARRIERO-BOBYLEVA 1973

    # #psiACO_n1 = VmaxAco_n*(CITmito_n0-ISOCITmito_n0/KeqAco_na) / (KmCitAco_n + CITmito_n0 + KmCitAco_n*ISOCITmito_n/KmIsoCitAco_n)
    # psiACO_n1 = VmaxAco_n*(CITmito_n0-ISOCITmito_n0/KeqAco_na) / (1.0+CITmito_n0/KmCitAco_n + ISOCITmito_n0/KmIsoCitAco_n)
    # psiACO_a1 = VmaxAco_a*(CITmito_a0-ISOCITmito_a0/KeqAco_na) / (1.0+CITmito_a0/KmCitAco_a + ISOCITmito_a0/KmIsoCitAco_a)

    # println(psiACO_n1)
    # println(psiACO_a1)

    ##############################################

    # r04: IDH: ISOCITmito_a + NADmito_a  ⇒ AKGmito_a + NADHmito_a #  ISOCITmito_a  ⇒ AKGmito_a #

    # key rate-limiting enzyme in TCA !!!

    # a
    # CO2_mito_a = 1.2 # par[349]

    # NAD-dependent isocitrate dehydrogenase (IDH); ISOCITmito + NADmito  ⇒ AKGmito + NADHmito
    # VmaxIDH_a = 64.0 #### CHECK IT!!!! UNITS!!!!
    # nIsoCitmitoIDH_a = 1.9
    # KmIsoCitmito1IDH_a = 0.11
    # KmIsoCitmito2IDH_a = 0.06
    # KaCaidhIDH_a = 0.0074
    # nCaIdhIDH_a = 2.0
    # KmNADmitoIDH_a = 0.091
    # KiNADHmitoIDH_a = 0.041

    ######### IDH_a
    # Wu2007
    # VmaxfIDH_a = 425.0 #mM/s
    # Km_a_NAD_IDH_a = 0.074
    # Km_b_ISOCIT_IDH_a = 0.183 # 0.059, 0.055, 0.183
    # nH_IDH_a = 2.5 # 2.67 #3.0
    # KibIDH_a = 0.0238 # 0.00766, 0.0238
    # KiqIDH_a = 0.029
    # Ki_atp_IDH_a = 0.091
    # Ka_adp_IDH_a = 0.05
    # Keq0_IDH_a = 3.5e-16 #3.5*(10^(-16))
    # Pakg_IDH_a = 1.0
    # Keq_IDH_a = 30.5 #-Mulukutla2015  #Keq0_IDH_a*(Pakg_IDH_a*Pnadh_IDH_a*Pco2tot_IDH_a)/(C_H_mitomatr*Pnad_IDH_a*Picit_IDH_a)

    # Berndt + doi:10.1016/j.bbapap.2008.07.001 + Mulukutla

    # # NAD-dependent isocitrate dehydrogenase (IDH); ISOCITmito + NADmito  ⇒ AKGmito + NADHmito
    # VmaxIDH_n = 0.1249913793 # VmaxCSmito_n/3.8666666667   #3.8666666667 is calc from rates ratio of doi:10.1046/j.1471-4159.2003.01871.x  Table 2 #4.25 #64.0
    # nIsoCitmito_n = 1.9   # 3
    # KmIsoCitmito1_n = 0.2 #0.11
    # KmIsoCitmito2_n = 0.06
    # Km_a_Ca_idh_n = 0.074 #0.0074
    # nCaIdh_n = 2.0
    # KmNADmito_n = 0.091
    # KiNADHmito_n = 0.0041 # 4.1 uM PMID: 7359132 #0.05 #0.041
    # #KmIsoCitmito = KmIsoCitmito1/(1+(CaMito/KaCaidh)^nIsoCitmito) + KmIsoCitmito2

    # VmaxIDH_a = 0.2708146552 # VmaxCSmito_a/1.7846153846 # 1.7846153846 is calc from rates ratio of doi:10.1046/j.1471-4159.2003.01871.x  Table 2 Specific activities of LDH, CS, and ICDH in total lysates of neural cell cultures
    # nIsoCitmito_a = 1.9  # 3
    # KmIsoCitmito1_a = 0.2 #0.11
    # KmIsoCitmito2_a = 0.06
    # Km_a_Ca_idh_a = 0.074 #0.0074
    # nCaIdh_a = 2.0
    # KmNADmito_a = 0.091
    # KiNADHmito_a = 0.05 #0.041

    # psiIDH_n1 = VmaxIDH_n*((ISOCITmito_n0^nIsoCitmito_n) / (ISOCITmito_n0^nIsoCitmito_n + (KmIsoCitmito1_n/(1+(CaMito_n0/Km_a_Ca_idh_n)^nCaIdh_n) + KmIsoCitmito2_n)^nIsoCitmito_n) ) * (NADmito_n0/(NADmito_n0 + KmNADmito_n*(1+NADHmito_n0/KiNADHmito_n)))
    # psiIDH_a1 = VmaxIDH_a*((ISOCITmito_a0^nIsoCitmito_a) / (ISOCITmito_a0^nIsoCitmito_a + (KmIsoCitmito1_a/(1+(CaMito_a0/Km_a_Ca_idh_a)^nCaIdh_a) + KmIsoCitmito2_a)^nIsoCitmito_a) ) * (NADmito_a0/(NADmito_a0 + KmNADmito_a*(1+NADHmito_a0/KiNADHmito_a)))

    ######  with eq from doi:10.1016/j.bbapap.2008.07.001

    VmaxIDH_n: float = 1194.49868869589  # 1109.856835123883 # 1117.155367232157 # 1117.8073730616716 # 1033.507542656321 # 1090. #1080. #1078.5 #1076. #950. #910. #905.055  #1076.0 # 891.34 #500. #80.0 #5.2 #2.5 #0.1249913793 # n/a = 0.030/0.065 = 0.4615384615384615 ratio of doi:10.1046/j.1471-4159.2003.01871.x  #1076.0 # 891.34 #500. #80.0 #5.2 #2.5 #0.1249913793 # n/a = 0.030/0.065 = 0.4615384615384615 ratio of doi:10.1046/j.1471-4159.2003.01871.x  Table 2 #4.25 #64.0  #  1000*69.2*0.25/60 = 288.33 where 69.2 from doi:10.1016/j.bbapap.2008.07.001  #
    KiNADmito_na: float = 0.14  # 0.0776 # Kia
    KmIsoCitIDHm_n: float = 0.15  # 0.35 #0.45 #0.1489 # Kmb
    KmNADmito_na: float = 0.5033  # Kma
    KiNADHmito_na: float = 0.00475  ## Kiq
    nIDH: float = 3  # 1.9 #3

    VmaxIDH_a: float = 332.052098136637  # 344.93939819582073 # 1087.7 # 1076.0 # 891.34 #500. #80.0 #5.42 #0.2708146552 # n/a = 0.030/0.065 = 0.4615384615384615 ratio of doi:10.1046/j.1471-4159.2003.01871.x Table 2 Specific activities of LDH, CS, and ICDH in total lysates of neural cell cultures
    # KiNADmito_na = 0.14 #0.0776 # Kia
    KmIsoCitIDHm_a: float = 0.15  # 0.35 #0.45 # 0.1489 # Kmb
    # KmNADmito_na = 0.5033 # Kma
    # KiNADHmito_na = 0.00475 ## Kiq
    nIDH: float = 3  # 1.9 #3

    # psiIDH_a(ISOCITmito_a,NADmito_a,NADHmito_a) = VmaxIDH_a*(NADmito_a/KiNADmito_a)*((ISOCITmito_a/KmIsoCitIDHm_a)^nIDH ) /  (1.0 + NADmito_a/KiNADmito_a + (KmNADmito_a/KiNADmito_a)*((ISOCITmito_a/KmIsoCitIDHm_a)^nIDH) + NADHmito_a/KiNADHmito_a + (NADmito_a/KiNADmito_a)*((ISOCITmito_a/KmIsoCitIDHm_a)^nIDH) +   ((KmNADmito_a*NADHmito_a)/(KiNADmito_a*KiNADHmito_a))*((ISOCITmito_a/KmIsoCitIDHm_a)^nIDH) )

    # psiIDH_n(ISOCITmito_n,NADmito_n,NADHmito_n) = VmaxIDH_n*((NADmito_n*ISOCITmito_n)/(KiNADmito_n*KmIsoCitIDHm_n)) /
    # (1.0 + NADmito_n/KiNADmito_n + (KmNADmito_n*ISOCITmito_n)/(KiNADmito_n*KmIsoCitIDHm_n) + NADHmito_n/KiNADHmito_n + (NADmito_n*ISOCITmito_n)/(KiNADmito_n*KmIsoCitIDHm_n) +
    #     (KmNADmito_n*ISOCITmito_n*NADHmito_n)/(KiNADmito_n*KmIsoCitIDHm_n*KiNADHmito_n) )

    # psiIDH_n(ISOCITmito_n,NADmito_n,NADHmito_n) = VmaxIDH_n*(NADmito_n/KiNADmito_n)*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH ) /  (1.0 + NADmito_n/KiNADmito_n + (KmNADmito_n/KiNADmito_n)*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH) + NADHmito_n/KiNADHmito_n + (NADmito_n/KiNADmito_n)*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH) +   ((KmNADmito_n*NADHmito_n)/(KiNADmito_n*KiNADHmito_n))*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH) )

    # add ADP-activation
    # psiIDH_n(ISOCITmito_n,NADmito_n,NADHmito_n) = VmaxIDH_n*(NADmito_n/KiNADmito_n)*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH ) /
    # (1.0 + NADmito_n/KiNADmito_n + (KmNADmito_n/KiNADmito_n)*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH) + NADHmito_n/KiNADHmito_n + (NADmito_n/KiNADmito_n)*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH) +
    #    ((KmNADmito_n*NADHmito_n)/(KiNADmito_n*KiNADHmito_n))*((ISOCITmito_n/KmIsoCitIDHm_n)^nIDH) )

    #
    # psiIDH_n(ISOCITmito_n,CaMito_n,NADmito_n,NADHmito_n) = VmaxIDH_n*((ISOCITmito_n^nIsoCitmito_n) / (ISOCITmito_n^nIsoCitmito_n + (KmIsoCitmito1_n/(1+(CaMito_n/Km_a_Ca_idh_n)^nCaIdh_n) + KmIsoCitmito2_n)^nIsoCitmito_n) ) * (NADmito_n/(NADmito_n + KmNADmito_n*(1+NADHmito_n/KiNADHmito_n)))
    # psiIDH_a(ISOCITmito_a,CaMito_a,NADmito_a,NADHmito_a) = VmaxIDH_a*((ISOCITmito_a^nIsoCitmito_a) / (ISOCITmito_a^nIsoCitmito_a + (KmIsoCitmito1_a/(1+(CaMito_a/Km_a_Ca_idh_a)^nCaIdh_a) + KmIsoCitmito2_a)^nIsoCitmito_a) ) * (NADmito_a/(NADmito_a + KmNADmito_a*(1+NADHmito_a/KiNADHmito_a)))

    # psiIDH_n1 = VmaxIDH_n*(NADmito_n0/KiNADmito_n)*((ISOCITmito_n0/KmIsoCitIDHm_n)^nIDH ) /  (1.0 + NADmito_n0/KiNADmito_n + (KmNADmito_n/KiNADmito_n)*((ISOCITmito_n0/KmIsoCitIDHm_n)^nIDH) + NADHmito_n0/KiNADHmito_n + (NADmito_n0/KiNADmito_n)*((ISOCITmito_n0/KmIsoCitIDHm_n)^nIDH) +   ((KmNADmito_n*NADHmito_n0)/(KiNADmito_n*KiNADHmito_n))*((ISOCITmito_n0/KmIsoCitIDHm_n)^nIDH) )
    # psiIDH_a1 = VmaxIDH_a*(NADmito_a0/KiNADmito_a)*((ISOCITmito_a0/KmIsoCitIDHm_a)^nIDH ) /  (1.0 + NADmito_a0/KiNADmito_a + (KmNADmito_a/KiNADmito_a)*((ISOCITmito_a0/KmIsoCitIDHm_a)^nIDH) + NADHmito_a0/KiNADHmito_a + (NADmito_a0/KiNADmito_a)*((ISOCITmito_a0/KmIsoCitIDHm_a)^nIDH) +   ((KmNADmito_a*NADHmito_a0)/(KiNADmito_a*KiNADHmito_a))*((ISOCITmito_a0/KmIsoCitIDHm_a)^nIDH) )

    # println(psiIDH_n1)
    # println(psiIDH_a1)

    ###################################################

    # r05: aKGDH: AKGmito_a + NADmito_a + CoAmito_a ⇒ SUCCOAmito_a + NADHmito_a # AKGmito_a + CoAmito_a ⇒ SUCCOAmito_a

    # VmaxKGDH_n = 10. #1.344
    # #KiCa2KGDH_n = 0.0012 #1.2e-05
    # Km1KGDHKGDH_n = 0.67 #0.025  # 0.67 # doi:10.1098/rstb.2005.1764
    # Km2KGDHKGDH_n = 0.16 #0.0016
    # #Ki_KG_Ca_KGDH_n = 1.33e-7 #1.33e-09
    # KiNADHKGDHKGDH_n = 0.0045 #4.5e-05  # 0.0045 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    # KmNADkgdhKGDH_n = 0.021  #0.00021 # 0.021  # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    # Km_CoA_kgdhKGDH_n = 0.0027 #1.3e-05  # 0.0027 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    # Ki_SucCoA_kgdhKGDH_n = 0.0039 # in brain! Luder 1990 # 0.0069 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase

    # aKG dehydrogenase (KGDH); AKGmito + NADmito + CoAmito ⇒ SUCCOAmito + NADHmito      ### Berndt2012
    ### but in future for more details and regulation can consider Detailed kinetics and regulation of mammalian 2- oxoglutarate dehydrogenase
    # 2011 Feng Qi1,2, Ranjan K Pradhan1, Ranjan K Dash1 and Daniel A Beard

    # VmaxKGDH_a = 10. #1.344
    # #KiCa2KGDH_a = 0.0012 # McCormack 1979, Mogilevskaya 2006
    # Km1KGDHKGDH_a = 0.67 #2.5 # Berndt 2012 # 0.67 # doi:10.1098/rstb.2005.1764
    # Km2KGDHKGDH_a = 0.16 # McCormack 1979
    # #Ki_KG_Ca_KGDH_a = 1.33e-7 # calculated from McCormack 1979
    # KiNADHKGDHKGDH_a = 0.0045 # Smith 1974 # 0.0045 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    # KmNADkgdhKGDH_a = 0.021 # Smith 1974 # 0.021  # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    # Km_CoA_kgdhKGDH_a = 0.0027 #0.0013 # Smith 1974 # 0.0027 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    # KiSucCoAkgdhKGDH_a = 0.0039 # in brain! Luder 1990  # # 0.0069 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase

    # # psiKGDH_n(CaMito_n,AKGmito_n,NADHmito_n,NADmito_n,CoAmito_n,SUCCOAmito_n) = VmaxKGDH_n*(1-CaMito_n/(CaMito_n+KiCa2KGDH_n))*(AKGmito_n/(AKGmito_n+(Km1KGDHKGDH_n/(1+CaMito_n/Ki_KG_Ca_KGDH_n)+Km2KGDHKGDH_n)*(1+NADHmito_n/KiNADHKGDHKGDH_n))) *   (NADmito_n/(NADmito_n+KmNADkgdhKGDH_n*(1+NADHmito_n/KiNADHKGDHKGDH_n))) * (CoAmito_n/(CoAmito_n + Km_CoA_kgdhKGDH_n*(1+SUCCOAmito_n/Ki_SucCoA_kgdhKGDH_n)))
    # # psiKGDH_a(CaMito_a,AKGmito_a,NADHmito_a,NADmito_a,CoAmito_a,SUCCOAmito_a) = VmaxKGDH_a*(1-CaMito_a/(CaMito_a+KiCa2KGDH_a))*(AKGmito_a/(AKGmito_a+(Km1KGDHKGDH_a/(1+CaMito_a/Ki_KG_Ca_KGDH_a)+Km2KGDHKGDH_a)*(1+NADHmito_a/KiNADHKGDHKGDH_a))) *  (NADmito_a/(NADmito_a+KmNADkgdhKGDH_a*(1+NADHmito_a/KiNADHKGDHKGDH_a))) * (CoAmito_a/(CoAmito_a + Km_CoA_kgdhKGDH_a*(1+SUCCOAmito_a/KiSucCoAkgdhKGDH_a)))

    # psiKGDH_n(CaMito_n,AKGmito_n,NADHmito_n,NADmito_n,CoAmito_n,SUCCOAmito_n) = VmaxKGDH_n*(1-CaMito_n/(CaMito_n+KiCa2KGDH_n))*(AKGmito_n/(AKGmito_n+(Km1KGDHKGDH_n/(1+CaMito_n/Ki_KG_Ca_KGDH_n)+Km2KGDHKGDH_n)*(1+NADHmito_n/KiNADHKGDHKGDH_n))) *   (NADmito_n/(NADmito_n+KmNADkgdhKGDH_n*(1+NADHmito_n/KiNADHKGDHKGDH_n))) * (CoAmito_n/(CoAmito_n + Km_CoA_kgdhKGDH_n*(1+SUCCOAmito_n/Ki_SucCoA_kgdhKGDH_n)))
    # psiKGDH_a(CaMito_a,AKGmito_a,NADHmito_a,NADmito_a,CoAmito_a,SUCCOAmito_a) = VmaxKGDH_a*(1-CaMito_a/(CaMito_a+KiCa2KGDH_a))*(AKGmito_a/(AKGmito_a+(Km1KGDHKGDH_a/(1+CaMito_a/Ki_KG_Ca_KGDH_a)+Km2KGDHKGDH_a)*(1+NADHmito_a/KiNADHKGDHKGDH_a))) *  (NADmito_a/(NADmito_a+KmNADkgdhKGDH_a*(1+NADHmito_a/KiNADHKGDHKGDH_a))) * (CoAmito_a/(CoAmito_a + Km_CoA_kgdhKGDH_a*(1+SUCCOAmito_a/KiSucCoAkgdhKGDH_a)))

    # psiKGDH_n1 = VmaxKGDH_n*(AKGmito_n0/(AKGmito_n0+(Km1KGDHKGDH_n+Km2KGDHKGDH_n)*(1+NADHmito_n0/KiNADHKGDHKGDH_n))) *  (NADmito_n0/(NADmito_n0+KmNADkgdhKGDH_n*(1+NADHmito_n0/KiNADHKGDHKGDH_n))) * (CoAmito_n0/(CoAmito_n0 + Km_CoA_kgdhKGDH_n*(1+SUCCOAmito_n0/Ki_SucCoA_kgdhKGDH_n)))
    # psiKGDH_a1 = VmaxKGDH_a*(AKGmito_a0/(AKGmito_a0+(Km1KGDHKGDH_a+Km2KGDHKGDH_a)*(1+NADHmito_a0/KiNADHKGDHKGDH_a))) *  (NADmito_a0/(NADmito_a0+KmNADkgdhKGDH_a*(1+NADHmito_a0/KiNADHKGDHKGDH_a))) * (CoAmito_a0/(CoAmito_a0 + Km_CoA_kgdhKGDH_a*(1+SUCCOAmito_a0/KiSucCoAkgdhKGDH_a)))

    # Mogilevskaya

    VmaxKGDH_n: float = 28.6907036435173  # 28.91517141816992 # 28.932047191118823 # 29.791351583908167 #28.496668132945448 # 30.41167501394481 #30. #28. #27. #26. #25.524 #23.4 #30.0 #35.0 # 40.0 #50.415 #166.22 #10. #1.344   23.4 #30.0 #35.0 # 40.0 #50.415 #166.22 #10. #1.344
    KiADPmito_KGDH_n: float = (
        0.6  # 0.56 # 0.1 # both values are in Mogilevskaya, 0.56 is fitted, 0.1 is lit
    )
    KiATPmito_KGDH_n: float = 0.0108261270854904  # 0.01 # 0.1 # both values are in Mogilevskaya, 0.01 is fitted, 0.1 is lit
    Km1KGDHKGDH_n: float = 0.8  # 0.67 #0.025  # 0.67 # doi:10.1098/rstb.2005.1764
    Km_CoA_kgdhKGDH_n: float = 0.005  # 0.0027 #1.3e-05  # 0.0027 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    KmNADkgdhKGDH_na: float = 0.021  # 0.00021 # 0.021  # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    KiCa2KGDH_n: float = 1.2e-05  # 0.0012 #1.2e-05
    KiNADHKGDHKGDH_na: float = 0.0045  # 4.5e-05  # 0.0045 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    Ki_SucCoA_kgdhKGDH_n: float = 0.0039  # in brain! Luder 1990 # 0.0069 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase

    VmaxKGDH_a: float = 7.74815022676304  # 7.4236647140402 #18.792728253785338  # 23.86 #23.93  #24.0 #up #23.8 down  #24.256852208624576 up #23.4 #47.681 #166.22 #10. #1.344
    KiADPmito_KGDH_a: float = 0.5046016363070087  # KiADPmito_KGDH_a = 0.6 #0.57 #0.56 # 0.1 # both values are in Mogilevskaya, 0.56 is fitted, 0.1 is lit
    KiATPmito_KGDH_a: float = 0.054580855381112  # 0.053818392618842754 # 0.01 # 0.1 # both values are in Mogilevskaya, 0.01 is fitted, 0.1 is lit
    Km1KGDHKGDH_a: float = (
        0.6287013099563603  # 0.8 #0.67 #0.025  # 0.67 # doi:10.1098/rstb.2005.1764
    )
    Km_CoA_kgdhKGDH_a: float = 0.005  # 0.0027 #1.3e-05  # 0.0027 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase
    KiCa2KGDH_a: float = 1.2e-05  # 0.0012 #1.2e-05
    Ki_SucCoA_kgdhKGDH_a: float = 0.0039  # in brain! Luder 1990 # 0.0069 # SMITH1973 Regulation of Mitochondrial a=Ketoglutarate Metabolism by Product Inhibition at a-Ketoglutarate Dehydrogenase

    # psiKGDH_n1 =
    # (VmaxKGDH_n*(1 + ADPmito_n0/KiADPmito_KGDH_n)*(AKGmito_n0/Km1KGDHKGDH_n)*(CoAmito_n0/Km_CoA_kgdhKGDH_n)*(NADmito_n0/KmNADkgdhKGDH_n) ) /
    # ( ( (CoAmito_n0/Km_CoA_kgdhKGDH_n)*(NADmito_n0/KmNADkgdhKGDH_n)*(AKGmito_n0/Km1KGDHKGDH_n + (1 + ATPmito_n0/KiATPmito_KGDH_n)/(1 + CaMito_n0/KiCa2KGDH_n)) ) +
    #     ( (AKGmito_n0/Km1KGDHKGDH_n)*(CoAmito_n0/Km_CoA_kgdhKGDH_n + NADmito_n0/KmNADkgdhKGDH_n)*(1 + NADHmito_n0/KiNADHKGDHKGDH_n + SUCCOAmito_n0/Ki_SucCoA_kgdhKGDH_n) )  )

    # psiKGDH_a1 =
    # (VmaxKGDH_a*(1 + ADPmito_a0/KiADPmito_KGDH_a)*(AKGmito_a0/Km1KGDHKGDH_a)*(CoAmito_a0/Km_CoA_kgdhKGDH_a)*(NADmito_a0/KmNADkgdhKGDH_a) ) /
    # ( ( (CoAmito_a0/Km_CoA_kgdhKGDH_a)*(NADmito_a0/KmNADkgdhKGDH_a)*(AKGmito_a0/Km1KGDHKGDH_a + (1 + ATPmito_a0/KiATPmito_KGDH_a)/(1 + CaMito_a0/KiCa2KGDH_a)) ) +
    #     ( (AKGmito_a0/Km1KGDHKGDH_a)*(CoAmito_a0/Km_CoA_kgdhKGDH_a + NADmito_a0/KmNADkgdhKGDH_a)*(1 + NADHmito_a0/KiNADHKGDHKGDH_a + SUCCOAmito_a0/Ki_SucCoA_kgdhKGDH_a) )  )

    # println(psiKGDH_n1)
    # println(psiKGDH_a1)

    ###################################################

    # r06: SCS: SUCCOAmito_n + ADPmito_n ⇒ SUCmito_n + ATPmito_n + CoAmito_n

    VmaxSuccoaATPscs_n: float = 410.83664327655714  # 409.916218893484 #433.58091004733 # 433.8339610456146 # 437.42815951086135 # 458.29727009401 # 476.615 # 400. #396. #395. #394.5 #394.21 #395. #400.0 #1.0067 #192.0 #400.0 #1.0067 #192.0
    AmaxPscs_n: float = 1.2  #  Berndt 2015
    npscs_n: float = 3.0  # Berndt 2015 #2.5 #
    Keqsuccoascs_na: float = 3.8  # Berndt 2015
    Km_succoa_scs_n: float = (
        0.02852096394334664  # 0.041 # Berndt2012,2015 #0.086 #  0.024 # Mogilevskaya
    )
    Km_succ_scs_n: float = 0.836589467070621  # 1.6 #PMID: 1869044 #0.49 #
    Km_pi_scs_na: float = 2.5  # 0.72,2.5 # Berndt 2012,2015
    Km_coa_scs_n: float = 0.056  # PMID: 1869044
    Km_atpmito_scs_n: float = 0.0156620432157514  # 0.017 # PMID: 1869044 # 0.72 #
    Km_ADPmito_scs_n: float = 0.25  #  Berndt 2012,2015

    VmaxSuccoaATPscs_a: float = 182.496590618396  # 171.24090767446916 # 360.0 #490.78642491794716 #400.0 #429.06807326391527 #367.77263422621314 #490.36351230161745 #576.4491390247175 #490.7864249179471 #370.0 #360.0 #415.0 # 410 down # 420 up #360.0 #400.0 #0.9236 #192.0  #360.0 #370.0 # 360.0 # 400.0 #0.9236 #192.0
    AmaxPscs_a: float = 1.2  #  Berndt 2015
    npscs_a: float = 3.0  # Berndt 2015 #2.5 #
    # Keqsuccoascs_na :float= 3.8 # Berndt 2015
    Km_succoa_scs_a: float = 0.041  # Berndt2012,2015 #0.086 #  0.024 # Mogilevskaya
    Km_succ_scs_a: float = 1.6  # PMID: 1869044 #0.49 #
    # Km_pi_scs_na :float= 2.5 # 0.72,2.5 # Berndt 2012,2015
    Km_coa_scs_a: float = 0.056  # PMID: 1869044
    Km_atpmito_scs_a: float = 0.0164177843454365  # 0.017 # PMID: 1869044 # 0.72 #
    Km_ADPmito_scs_a: float = 0.25  #  Berndt 2012,2015

    ###################################################

    # !!! J_DH from ETC instead

    # # r07: SDH: SUCmito_n + Qmito_n  ⇒ FUMmito_n + QH2mito_n

    # # kcat_SDH_n :float= 79274.6 #Vf_SDH_n 16.1389 # par[547]

    # # #Mulukutla2015
    # # KiOXA_SDH_n :float= 0.0015 # par[544]
    # # KaSUC_SDH_n :float= 0.45 # par[545]
    # # KaFUM_SDH_n :float= 0.375 # par[546]
    # # Keq_SDH_n :float= 1.21 # par[548]
    # # KiSUC_SDH_n :float= 0.12 # par[549]
    # # KmQ_SDH_n :float= 0.48 # par[550]
    # # KmSuc_SDH_n :float= 0.467 # par[551]
    # # KiFUM_SDH_n :float= 1.275 # par[552]
    # # KmQH2_SDH_n :float= 0.00245 # par[553]
    # # KmFUM_SDH_n :float= 1.2 # par[554]

    # # psiSDH_n(SUCmito_n,Qmito_n,QH2mito_n,FUMmito_n,OXAmito_n) :float= kcat_SDH_n*concentration_enzyme_transporter_TCA_r07_SDH_n*( SUCmito_n*Qmito_n - QH2mito_n*FUMmito_n/Keq_SDH_n  ) / ( KiSUC_SDH_n*KmQ_SDH_n*((1.0 + OXAmito_n/KiOXA_SDH_n + SUCmito_n/KaSUC_SDH_n + FUMmito_n/KaFUM_SDH_n ) / (1.0 + SUCmito_n/KaSUC_SDH_n + FUMmito_n/KaFUM_SDH_n  ) )   +    KmQ_SDH_n*SUCmito_n + KmSuc_SDH_n*((1.0 + OXAmito_n/KiOXA_SDH_n + SUCmito_n/KaSUC_SDH_n + FUMmito_n/KaFUM_SDH_n ) / (1.0 + SUCmito_n/KaSUC_SDH_n + FUMmito_n/KaFUM_SDH_n  ) ) *Qmito_n + SUCmito_n*Qmito_n + KmSuc_SDH_n*Qmito_n*FUMmito_n/KiFUM_SDH_n  +    (KiSUC_SDH_n*KmQ_SDH_n/(KiFUM_SDH_n*KmQH2_SDH_n) )*( KmFUM_SDH_n*((1.0 + OXAmito_n/KiOXA_SDH_n + SUCmito_n/KaSUC_SDH_n + FUMmito_n/KaFUM_SDH_n ) / (1.0 + SUCmito_n/KaSUC_SDH_n + FUMmito_n/KaFUM_SDH_n  ) ) *QH2mito_n + KmQH2_SDH_n*FUMmito_n + KmFUM_SDH_n*SUCmito_n*QH2mito_n/KiSUC_SDH_n + QH2mito_n*FUMmito_n ) )        # eto_mito_n_scaled*

    # # # Succinate dehydrogenase (SDH); SUCmito + Qmito  ⇒ FUMmito + QH2mito  # Mogilevskaya 2006  ## try eq from IvanChang for this reaction
    # # #kfSDH_a :float= 10000.0
    # # #Kesucsucmito_a :float= 0.01
    # # #Kmqmito_a :float= 0.0003
    # # #krSDH_a :float= 102.0
    # # #Kefumfummito_a :float= 0.29
    # # #Kmqh2mito_a :float= 0.0015
    # # #Kmsucsdh_a :float= 0.13
    # # #Kmfumsdh_a :float= 0.025
    # # #@reaction_func VSDH(SDHmito,SUCmito,Qmito,FUMmito,QH2mito) :float= SDHmito*(kfSDH*(SUCmito/Kesucsucmito)*(Qmito/Kmqmito) - krSDH*(FUMmito/Kefumfummito)*(QH2mito/Kmqh2mito)) / (1+(SUCmito/Kesucsucmito)+(Qmito/Kmqmito)*(Kmsucsdh/Kesucsucmito)+(SUCmito/Kesucsucmito)*(Qmito/Kmqmito)+(FUMmito/Kefumfummito)+(QH2mito/Kmqh2mito)*(Kmfumsdh/Kefumfummito) + (FUMmito/Kefumfummito)*(QH2mito/Kmqh2mito))
    # # ####################################################################################

    # # # Succinate dehydrogenase (SDH); SUCmito + Qmito  ⇒ FUMmito + QH2mito  # IvanChang
    # # #VmaxDHchang_a :float= 0.28
    # # #KrDHchang_a :float= 0.100
    # # #pDchang_a :float=0.8

    # # #Mulukutla2015
    # # kcat_SDH_a :float= 82609.7 #Vf_SDH_a 16.14 #58100.0/3600.0
    # # Keq_SDH_a :float= 1.21
    # # KmSuc_SDH_a :float= 0.467
    # # KmQ_SDH_a :float= 0.48
    # # KmQH2_SDH_a :float= 0.00245
    # # KmFUM_SDH_a :float= 1.2
    # # KiSUC_SDH_a :float= 0.12
    # # KiFUM_SDH_a :float= 1.275
    # # KiOXA_SDH_a :float= 0.0015
    # # KaSUC_SDH_a :float= 0.45
    # # KaFUM_SDH_a :float= 0.375

    # # #psiSDH_a  VmaxDHchang_a*((NADmito_a/NADHmito_a)/(NADmito_a/NADHmito_a+KrDHchang_a))

    # # #Mulukutla2015
    # # #alpha_SDH_a ((1.0 + OXAmito_a/KiOXA_SDH_a + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a ) / (1.0 + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a  ))
    # # psiSDH_a(SUCmito_a,Qmito_a,QH2mito_a,FUMmito_a,OXAmito_a) :float= kcat_SDH_a*concentration_enzyme_transporter_TCA_r07_SDH_a*( SUCmito_a*Qmito_a - QH2mito_a*FUMmito_a/Keq_SDH_a  ) /     ( KiSUC_SDH_a*KmQ_SDH_a*((1.0 + OXAmito_a/KiOXA_SDH_a + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a ) / (1.0 + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a  ))  + KmQ_SDH_a*SUCmito_a + KmSuc_SDH_a*((1.0 + OXAmito_a/KiOXA_SDH_a + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a ) / (1.0 + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a  ))*Qmito_a + SUCmito_a*Qmito_a + KmSuc_SDH_a*Qmito_a*FUMmito_a/KiFUM_SDH_a  +    (KiSUC_SDH_a*KmQ_SDH_a/(KiFUM_SDH_a*KmQH2_SDH_a) )*( KmFUM_SDH_a*((1.0 + OXAmito_a/KiOXA_SDH_a + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a ) / (1.0 + SUCmito_a/KaSUC_SDH_a + FUMmito_a/KaFUM_SDH_a  ))*QH2mito_a + KmQH2_SDH_a*FUMmito_a + KmFUM_SDH_a*SUCmito_a*QH2mito_a/KiSUC_SDH_a + QH2mito_a*FUMmito_a   )   )

    # # Berndt2012
    # # ZEYLEMAKER1969 for OXA inh 1-s2.0-0005274469902423-main.pdf KiOXA :float= 4 uM
    # # http://dx.doi.org/10.1016/j.bbabio.2016.06.002 for BRAIN OXA inhibition of SDH KdOXA ~ 1e-8 M

    # VmaxSDH_n :float= 12.1 # 5000. # approx Mogilevskaya #2.9167 #brain approx 1000*0.7*0.25/60 from Shaw1981 #2000. # approx from LW fig in MISHRA1993 # 0.33056 # approx by 1000*4.76*0.25/3600 from RAMESH REDDY 1989 # #20.0 # approx
    # Keq_SDH_n :float= 0.06 #2.547923498331544 # calc Berndt2012# 1.21 #0.06 # calc as in Berndt2015 fad #1.21 #0.0102 # approx 102/10000
    # KmSuc_SDH_n :float= 1.6 #0.00769 #1.0 # approx Nakae1995 KmSDH solub and membrane bound are diff #0.00769  #1.6 # Berndt2012 # 2.5 # RAMESH REDDY 1989 # 0.26 #doi:10.1016/j.bbabio.2010.10.009  # 0.00769 approx from LW fig in MISHRA1993  # 0.048 from https://doi.org/10.1186/s13765-021-00626-1
    # #KiMAL_SDH_n :float= 2.2 # Berndt2012
    # KiOXASDH_n :float= 0.004 # ZEYLEMAKER1969

    # VmaxSDH_a :float= 11.7 #5000. # approx Mogilevskaya  2.9167 #brain approx 1000*0.7*0.25/60 from Shaw1981  # 2000. # approx from LW fig in MISHRA1993 #0.33056 # approx by 1000*4.76*0.25/3600 from RAMESH REDDY 1989 #  #20.0 # approx
    # Keq_SDH_a :float= 0.06 #2.547923498331544 #1.21 #0.06 # calc as in Berndt2015 fad  #1.21 #0.0102 # approx 102/10000
    # KmSuc_SDH_a :float= 1.6 #0.00769 #1.0 # approx Nakae1995 KmSDH solub and membrane bound are diff # 0.00769  #1.6 # Berndt2012 # 2.5 # RAMESH REDDY 1989  # 0.26 #doi:10.1016/j.bbabio.2010.10.009  # 0.00769 approx from LW fig in MISHRA1993  # 0.048 from https://doi.org/10.1186/s13765-021-00626-1
    # #KiMAL_SDH_a :float= 2.2 # Berndt2012
    # KiOXASDH_a :float= 0.004 # ZEYLEMAKER1969

    # # #psiSDH_n1 :float= VmaxSDH_n*( SUCmito_n0*Qmito_n0 - (QH2mito_n0*FUMmito_n0)/Keq_SDH_n  ) / (SUCmito_n0 + KmSuc_SDH_n*(1 + MALmito_n0/KiMAL_SDH_n) )
    # # #psiSDH_a1 :float= VmaxSDH_a*( SUCmito_a0*Qmito_a0 - (QH2mito_a0*FUMmito_a0)/Keq_SDH_a  ) / (SUCmito_a0 + KmSuc_SDH_a*(1 + MALmito_a0/KiMAL_SDH_a) )

    # # psiSDH_n1 :float= VmaxSDH_n*( SUCmito_n0*Qmito_n0 - (QH2mito_n0*FUMmito_n0)/Keq_SDH_n  ) / (SUCmito_n0 + KmSuc_SDH_n*(1 + OXAmito_n0/KiOXASDH_n) )
    # # psiSDH_a1 :float= VmaxSDH_a*( SUCmito_a0*Qmito_a0 - (QH2mito_a0*FUMmito_a0)/Keq_SDH_a  ) / (SUCmito_a0 + KmSuc_SDH_a*(1 + OXAmito_a0/KiOXASDH_a) )

    # # println(psiSDH_n1)
    # # println(psiSDH_a1)

    ###################################################

    # r08: FUM: FUMmito_a  ⇒ MALmito_a

    # kr :float= 1.4*kf # doi:10.1111/febs.14782 The FEBS Journal - 2019 - Ajalla Aleixo - Structural  biochemical and biophysical characterization of recombinant human.pdf

    # Vmaxfum_n :float= 20. #0.8109 # 90721*2.27*1e-4:float=20.59 Mogilevskaya
    # Keqfummito_na :float= 5.5 #4.4 #4.3 #doi:10.1111/febs.14782 #4.4  Berndt 2015
    # Km_fummito_n :float= 0.14 #0.2 # doi:10.1111/febs.14782 #0.14  Berndt 2015
    # Km_malmito_n :float= 0.3 #1.4 #doi:10.1111/febs.14782 #0.3  Berndt 2015

    Vmaxfum_n: float = 129.92082588239924  # 129.9966516254743 # 131.89863784638874 # 132.91320856708984 # 133. #130. #139. #132. #140. #155. #180. #130. #260. #0.8109 # 90721*2.27*1e-4:float=20.59 Mogilevskaya

    Keqfummito_na: float = 6.0  # 5.6 #5.5 #4.4 #4.3 #doi:10.1111/febs.14782 #4.4  Berndt 2015
    Km_fummito_n: float = (
        0.15102517071248805  # 0.14 #0.2 # doi:10.1111/febs.14782 #0.14  Berndt 2015
    )
    Km_malmito_n: float = 0.3  # 1.4 #doi:10.1111/febs.14782 #0.3  Berndt 2015

    # Fumarase (FUM); FUMmito  ⇒  MALmito  based on Berndt 2015
    Vmaxfum_a: float = 42.24027032956515  # 231.87304452250146 #260. # 20. #1.496  # 90721*2.27*1e-4:float=20.59 Mogilevskaya
    Km_fummito_a: float = 0.14  # 0.2 # doi:10.1111/febs.14782 #0.14  Berndt 2015
    Km_malmito_a: float = 0.3  # 1.4 #doi:10.1111/febs.14782 #0.3  Berndt 2015

    # psiFUM_n1 :float= Vmaxfum_n*(FUMmito_n0 - MALmito_n0/Keqfummito_n)/(1.0+FUMmito_n0/Km_fummito_n+MALmito_n0/Km_malmito_n)
    # psiFUM_a1 :float= Vmaxfum_a*(FUMmito_a0 - MALmito_a0/Keqfummito_a)/(1.0+FUMmito_a0/Km_fummito_a+MALmito_a0/Km_malmito_a)

    # println(psiFUM_n1)
    # println(psiFUM_a1)

    ###################################################

    # r09: MDH: MALmito_a + NADmito_a ⇒ OXAmito_a + NADHmito_a # MALmito_a  ⇒ OXAmito_a #

    # VmaxMDHmito_n :float= 3261.5989 #20. #10.  # approx #32000.0 #Berndt #0.53
    # Keqmdhmito_na :float= 0.022 #0.02 #0.02 #0.01 #4e-5 #1e-3 #1.2e-3 #Berndt2012 or 1e-4 Berndt2015  #0.000402 #
    # Km_mal_mdh_n :float= 0.4 #0.33 #0.145 #Berndt #0.167 #0.0145  # 0.33 Berndt2018
    # Km_nad_mdh_na :float= 0.06 #Berndt #0.056 #0.006
    # Km_oxa_mdh_n :float= 0.1 #0.08 #0.017 #0.04 #Bernstein1978 #0.017 #Berndt #0.055 #0.0017
    # Km_nadh_mdh_na :float= 0.044 #Berndt #0.026 #0.0044

    VmaxMDHmito_n: float = 390.370655175952  # 417.5043146364773 # 417.7479828450139 # 418.7013772682505 # 450.58427655768554 #450. # 445. #390. #475. #800.0 #70.07614130634326 #3261.5989 #20. #10.  # approx #32000.0 #Berndt #0.53

    Keqmdhmito_na: float = 0.025  # 0.022 #0.02 #0.02 #0.01 #4e-5 #1e-3 #1.2e-3 #Berndt2012 or 1e-4 Berndt2015  #0.000402 #
    Km_mal_mdh_n: float = 0.4  # 0.33 #0.145 #Berndt #0.167 #0.0145  # 0.33 Berndt2018
    Km_nad_mdh_na: float = 0.06  # Berndt #0.056 #0.006
    Km_oxa_mdh_n: float = 0.1  # 0.08 #0.017 #0.04 #Bernstein1978 #0.017 #Berndt #0.055 #0.0017
    Km_nadh_mdh_na: float = 0.044  # Berndt #0.026 #0.0044

    # Malate dehydrogenase; MALmito + NADmito ⇒ OXAmito + NADHmito  based on Berndt 2015
    VmaxMDHmito_a: float = 107.964870005644  # 118.4814599996424 # 343.03071799750387 #300.0 #343.03071799750387 #800.0 #53.57 #20. # approx #32000.0 #Berndt
    # Keqmdhmito_na :float= 0.022 #0.02 #0.01  #4e-5 #1e-3 #1.2e-3 #Berndt  0.0001
    Km_mal_mdh_a: float = 0.4  # 0.33 #0.145 #Berndt #0.0145 #0.145  # 0.33 Berndt2018
    # Km_nad_mdh_na :float= 0.06 #Berndt #0.006 #0.06
    Km_oxa_mdh_a: float = 0.1  # 0.08 #0.017 #0.04 #Bernstein1978 0.017 #Berndt #0.0017 #0.017
    # Km_nadh_mdh_na :float= 0.044 #Berndt #0.0044 #0.044

    # psiMDH_n1 :float= VmaxMDHmito_n*(MALmito_n0*NADmito_n0-OXAmito_n0*NADHmito_n0/Keqmdhmito_n) / ((1.0+MALmito_n0/Km_mal_mdh_n)*(1.0+NADmito_n0/Km_nad_mdh_n)+(1.0+OXAmito_n0/Km_oxa_mdh_n)*(1.0+NADHmito_n0/Km_nadh_mdh_n))   # eto_mito_n_scaled*
    # psiMDH_a1 :float= VmaxMDHmito_a*(MALmito_a0*NADmito_a0-OXAmito_a0*NADHmito_a0/Keqmdhmito_a) / ((1.0+MALmito_a0/Km_mal_mdh_a)*(1+NADmito_a0/Km_nad_mdh_a)+(1+OXAmito_a0/Km_oxa_mdh_a)*(1+NADHmito_a0/Km_nadh_mdh_a))


### count constants
if __name__ == "__main__":
    total_constants = 0

    def count_constants(cls):
        total = len(fields(cls))
        instance = cls()
        for attr in dir(instance):
            if not attr.startswith("_") and not any(f.name == attr for f in fields(cls)):
                total += 1
        return total

    current_module = inspect.getmodule(inspect.currentframe())
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj) and is_dataclass(obj):
            n = count_constants(obj)
            print(f"{name}: {n} constants")
            total_constants += n

    print(f"Total: {total_constants}")
