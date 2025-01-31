import flashgg.Taggers.globalVariables_cff as globalVars

#import FWCore.ParameterSet.Config as cms

#from globalVariables_cff import globalVariables

from flashgg.MicroAOD.flashggJets_cfi import flashggBTag
from flashgg.MicroAOD.flashggJets_cfi import flashggDeepCSVb
from flashgg.MicroAOD.flashggJets_cfi import flashggDeepCSVbb

vtx_variables=[
    "vtxprob                := diPhotonMVA.vtxprob",
    "ptbal                  := diPhoton.ptBal",
    "ptasym                 := diPhoton.ptAsym",
    "logspt2                := diPhoton.logSumPt2",
    "p2conv                 := diPhoton.pullConv",
    "nconv                  := diPhoton.nConv",
    "vtxmva                 := diPhoton.vtxProbMVA",
    "vtxdz                  := diPhoton.dZ1",
    "vtx_x                  := diPhoton.vtx.x", 
    "vtx_y                  := diPhoton.vtx.y", 
    "vtx_z                  := diPhoton.vtx.z"
    
]

vtx_truth_variables = [
    "gv_x                   := diPhoton.genPV.x", 
    "gv_y                   := diPhoton.genPV.y", 
    "gv_z                   := diPhoton.genPV.z"

]

dipho_variables=[
    "dipho_sumpt            := diPhoton.sumPt",
    "dipho_cosphi           := abs(cos(diPhoton.leadingPhoton.phi - diPhoton.subLeadingPhoton.phi))",
    "dipho_mass             := diPhoton.mass",
    "dipho_pt               := diPhoton.pt",
    "dipho_phi              := diPhoton.phi",
    "dipho_eta              := diPhoton.eta",
    "dipho_e                := diPhoton.energy",
    "dipho_PtoM             := diPhoton.pt/diPhoton.mass",
    "cosphi                 := diPhotonMVA.CosPhi",
    "sigmaMrvoM             := diPhotonMVA.sigmarv",
    "sigmaMwvoM             := diPhotonMVA.sigmawv",
]

photon_variables=[
    "dipho_leadPt           := diPhoton.leadingPhoton.pt",
    "dipho_leadEt           := diPhoton.leadingPhoton.et",
    "dipho_leadEta          := diPhoton.leadingPhoton.eta",
    "dipho_leadPhi          := diPhoton.leadingPhoton.phi",
    "dipho_lead_sieie       := diPhoton.leadingPhoton.sigmaIetaIeta",
    "dipho_lead_hoe         := diPhoton.leadingPhoton.hadronicOverEm",
    "dipho_lead_sigmaEoE    := diPhoton.leadingPhoton.sigEOverE",
    "dipho_lead_ptoM        := diPhoton.leadingPhoton.pt/diPhoton.mass",
    "dipho_leadR9           := diPhoton.leadingPhoton.full5x5_r9",
    "dipho_leadIDMVA        := diPhoton.leadingView.phoIdMvaWrtChosenVtx",
    "dipho_lead_elveto      := diPhoton.leadingPhoton.passElectronVeto",
    "dipho_lead_prompt      := diPhoton.leadingPhoton.genMatchType",
    "dipho_lead_chiso       := diPhoton.leadingView.pfChIso03WrtChosenVtx",
    "dipho_lead_chisow      := diPhoton.leadingPhoton.pfChgIsoWrtWorstVtx04",
    "dipho_lead_phoiso      := diPhoton.leadingPhoton.pfPhoIso03",
    "dipho_lead_phoiso04    := diPhoton.leadingPhoton.pfPhoIso04",
    "dipho_lead_neutiso      := diPhoton.leadingPhoton.pfNeutIso03",
    "dipho_lead_ecaliso03   := diPhoton.leadingPhoton.ecalRecHitSumEtConeDR03",
    "dipho_lead_hcaliso03   := diPhoton.leadingPhoton.hcalTowerSumEtConeDR03",
    "dipho_lead_pfcluecal03 := diPhoton.leadingPhoton.ecalPFClusterIso",
    "dipho_lead_pfcluhcal03 := diPhoton.leadingPhoton.hcalPFClusterIso",
    "dipho_lead_trkiso03    := diPhoton.leadingPhoton.trkSumPtHollowConeDR03",
    "dipho_lead_pfchiso2    := diPhoton.leadingView.pfChIso02WrtChosenVtx",
    "dipho_lead_haspixelseed:= diPhoton.leadingPhoton.hasPixelSeed",
    "dipho_lead_sieip       := diPhoton.leadingPhoton.sieip",
    "dipho_lead_etawidth    := diPhoton.leadingPhoton.superCluster.etaWidth",
    "dipho_lead_phiwidth    := diPhoton.leadingPhoton.superCluster.phiWidth",
    "dipho_lead_regrerr     := diPhoton.leadingPhoton.sigEOverE * diPhoton.leadingPhoton.energy",
    "dipho_lead_s4ratio     :=  diPhoton.leadingPhoton.s4",
    "dipho_lead_effSigma    :=  diPhoton.leadingPhoton.esEffSigmaRR",
    "dipho_lead_scraw       :=  diPhoton.leadingPhoton.superCluster.rawEnergy",
    "dipho_lead_ese         :=  diPhoton.leadingPhoton.superCluster.preshowerEnergy",

    "dipho_subleadPt        := diPhoton.subLeadingPhoton.pt",
    "dipho_subleadEt        := diPhoton.subLeadingPhoton.et",
    "dipho_subleadEta       := diPhoton.subLeadingPhoton.eta",
    "dipho_subleadPhi       := diPhoton.subLeadingPhoton.phi",
    "dipho_sublead_sieie    := diPhoton.subLeadingPhoton.sigmaIetaIeta",
    "dipho_sublead_hoe      := diPhoton.subLeadingPhoton.hadronicOverEm",
    "dipho_sublead_sigmaEoE := diPhoton.subLeadingPhoton.sigEOverE",
    "dipho_sublead_ptoM     := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
    "dipho_subleadR9        := diPhoton.subLeadingPhoton.full5x5_r9",
    "dipho_subleadIDMVA     := diPhoton.subLeadingView.phoIdMvaWrtChosenVtx",
    "dipho_sublead_elveto   := diPhoton.subLeadingPhoton.passElectronVeto",
    "dipho_sulead_prompt    := diPhoton.subLeadingPhoton.genMatchType",
    "dipho_sublead_chiso    := diPhoton.leadingView.pfChIso03WrtChosenVtx",
    "dipho_sublead_chisow   := diPhoton.subLeadingPhoton.pfChgIsoWrtWorstVtx04",
    "dipho_sublead_phoiso   := diPhoton.subLeadingPhoton.pfPhoIso03",
    "dipho_sublead_phoiso04 := diPhoton.subLeadingPhoton.pfPhoIso04",
    "dipho_sublead_neutiso   := diPhoton.subLeadingPhoton.pfNeutIso03",
    "dipho_sublead_ecaliso03:= diPhoton.subLeadingPhoton.ecalRecHitSumEtConeDR03",
    "dipho_sublead_hcaliso03:= diPhoton.subLeadingPhoton.hcalTowerSumEtConeDR03",
    "dipho_sublead_pfcluecal03 := diPhoton.subLeadingPhoton.ecalPFClusterIso",
    "dipho_sublead_pfcluhcal03 := diPhoton.subLeadingPhoton.hcalPFClusterIso",
    "dipho_sublead_trkiso03    := diPhoton.subLeadingPhoton.trkSumPtHollowConeDR03",
    "dipho_sublead_pfchiso2    := diPhoton.subLeadingView.pfChIso02WrtChosenVtx",
    "dipho_sublead_haspixelseed:= diPhoton.subLeadingPhoton.hasPixelSeed",
    "dipho_sublead_sieip       := diPhoton.subLeadingPhoton.sieip",
    "dipho_sublead_etawidth    := diPhoton.subLeadingPhoton.superCluster.etaWidth",
    "dipho_sublead_phiwidth    := diPhoton.subLeadingPhoton.superCluster.phiWidth",
    "dipho_sublead_regrerr     := diPhoton.subLeadingPhoton.sigEOverE * diPhoton.subLeadingPhoton.energy",
    "dipho_sublead_s4ratio     :=  diPhoton.subLeadingPhoton.s4",
    "dipho_sublead_effSigma    :=  diPhoton.subLeadingPhoton.esEffSigmaRR",
    "dipho_sublead_scraw       :=  diPhoton.subLeadingPhoton.superCluster.rawEnergy",
    "dipho_sublead_ese         :=  diPhoton.subLeadingPhoton.superCluster.preshowerEnergy",
        
]

lepton_variables=[
    "LeptonType             := getLeptonType()",
    "n_ele                  := electrons.size",
    "n_loose_ele            := n_Ele_Loose",
    "n_veto_ele             := n_Ele_Veto",
    "n_medium_ele           := n_Ele_Medium",
    "n_tight_ele            := n_Ele_Tight",
    "ele1_pt                := ?(electrons.size>0)? electrons.at(0).pt : -999",
    "ele2_pt                := ?(electrons.size>1)? electrons.at(1).pt : -999",
    "ele1_eta               := ?(electrons.size>0)? electrons.at(0).superCluster().eta : -999",
    "ele2_eta               := ?(electrons.size>1)? electrons.at(1).superCluster().eta : -999",
    "ele1_phi               := ?(electrons.size>0)? electrons.at(0).superCluster().phi : -999",
    "ele2_phi               := ?(electrons.size>1)? electrons.at(1).superCluster().phi : -999",
    "ele1_e                 := ?(electrons.size>0)? electrons.at(0).energy : -999",
    "ele2_e                 := ?(electrons.size>1)? electrons.at(1).energy : -999",
    "ele1_ch                := ?(electrons.size>0)? electrons.at(0).charge : -999",
    "ele2_ch                := ?(electrons.size>1)? electrons.at(1).charge : -999",
    "ele1_sigmaIetaIeta     := ?(electrons.size>0)? electrons.at(0).full5x5_sigmaIetaIeta : -999",
    "ele2_sigmaIetaIeta     := ?(electrons.size>1)? electrons.at(1).full5x5_sigmaIetaIeta : -999",
    "ele1_dEtaInSeed        := ?(electrons.size>0)? electrons.at(0).deltaEtaSuperClusterTrackAtVtx() - electrons.at(0).superCluster().eta() + electrons.at(0).superCluster().seed().eta  : -999",
    "ele2_dEtaInSeed        := ?(electrons.size>1)? electrons.at(1).deltaEtaSuperClusterTrackAtVtx() - electrons.at(1).superCluster().eta() + electrons.at(1).superCluster().seed().eta  : -999",
    "ele1_dPhiIn            := ?(electrons.size>0)? electrons.at(0).deltaPhiSuperClusterTrackAtVtx : -999",
    "ele2_dPhiIn            := ?(electrons.size>1)? electrons.at(1).deltaPhiSuperClusterTrackAtVtx : -999",
    "ele1_hOverE            := ?(electrons.size>0)? electrons.at(0).hadronicOverEm : -999",
    "ele2_hOverE            := ?(electrons.size>1)? electrons.at(1).hadronicOverEm : -999",
    "ele1_RelIsoEA          := ?(electrons.size>0)? ( electrons.at(0).pfIsolationVariables().sumChargedHadronPt + max(0.0, electrons.at(0).pfIsolationVariables().sumNeutralHadronEt + electrons.at(0).pfIsolationVariables().sumPhotonEt - getElecAlpha(0)*getrho) ) / electrons.at(0).pt : -999",
    "ele2_RelIsoEA          := ?(electrons.size>1)? ( electrons.at(1).pfIsolationVariables().sumChargedHadronPt + max(0.0, electrons.at(1).pfIsolationVariables().sumNeutralHadronEt + electrons.at(1).pfIsolationVariables().sumPhotonEt - getElecAlpha(1)*getrho) ) / electrons.at(1).pt : -999",
    "ele1_ooEmooP           := ?(electrons.size>0)? abs(1.0 - electrons.at(0).eSuperClusterOverP)*(1./electrons.at(0).ecalEnergy) : -999",
    "ele2_ooEmooP           := ?(electrons.size>1)? abs(1.0 - electrons.at(1).eSuperClusterOverP)*(1./electrons.at(1).ecalEnergy) : -999",
    "ele1_dxy               := ?(electrons.size>0)? getLeadingLeptonVertexDxy(\"electron\"): -999",
    "ele2_dxy               := ?(electrons.size>0)? getSubLeadingLeptonVertexDxy(\"electron\"):  -999",
    "ele1_diphodxy          := ?(electrons.size>0)? getLeadingLeptonDiphoVertexDxy(\"electron\"):  -999",
    "ele2_diphodxy          := ?(electrons.size>1)? getSubLeadingLeptonDiphoVertexDxy(\"electron\"):  -999",
    "ele1_dz                := ?(electrons.size>0)? getLeadingLeptonVertexDz(\"electron\") : -999",
    "ele2_dz                := ?(electrons.size>1)? getSubLeadingLeptonVertexDz(\"electron\"):  -999",
    "ele1_diphodz           := ?(electrons.size>0)? getLeadingLeptonDiphoVertexDz(\"electron\"):  -999",
    "ele2_diphodz           := ?(electrons.size>1)? getSubLeadingLeptonDiphoVertexDz(\"electron\"):  -999",
    "ele1_misHits           := ?(electrons.size>0)? getLeadingElectronMisHits: -999",
    "ele2_misHits           := ?(electrons.size>0)? getSubLeadingElectronMisHits: -999",
    "ele1_ConversionVeto    := ?(electrons.size>0)? electrons.at(0).passConversionVeto : -999",
    "ele2_ConversionVeto    := ?(electrons.size>1)? electrons.at(1).passConversionVeto : -999",
    "ele1_ChargedHadronPt   := ?(electrons.size>0)? electrons.at(0).pfIsolationVariables().sumChargedHadronPt: -999",
    "ele2_ChargedHadronPt   := ?(electrons.size>1)? electrons.at(1).pfIsolationVariables().sumChargedHadronPt: -999",
    "ele2_NeutralHadronEt   := ?(electrons.size>1)? electrons.at(1).pfIsolationVariables().sumNeutralHadronEt: -999",
    "ele1_NeutralHadronEt   := ?(electrons.size>0)? electrons.at(0).pfIsolationVariables().sumNeutralHadronEt: -999",
    "ele1_PhotonEt          := ?(electrons.size>0)? electrons.at(0).pfIsolationVariables().sumPhotonEt: -999",
    "ele2_PhotonEt          := ?(electrons.size>1)? electrons.at(1).pfIsolationVariables().sumPhotonEt: -999",
    "ele1_PassTight         := ?(electrons.size>0)? ElePassTight.at(0) : -999",
    "ele2_PassTight         := ?(electrons.size>1)? ElePassTight.at(1) : -999",
    "ele1_PassVeto          := ?(electrons.size>0)? ElePassVeto.at(0) : -999",
    "ele2_PassVeto          := ?(electrons.size>1)? ElePassVeto.at(1) : -999",
    "ele1_dPhiMET           := ?(electrons.size>0)? dPhi_Electron1_MET() : -999",
    'ele2_dPhiMET           := ?(electrons.size>1)? dPhi_Electron2_MET() : -999',
    "n_muons                := muons.size",
    "n_LooseMu25            := NLooseMu25",
    "n_LooseMu15            := NLooseMu15",
    "n_TightMu25            := NTightMuo25",
    "n_TightMu15            := NTightMuo15",
    "n_MediumMu25           := NMediumMu25",
    "n_MediumMu15           := NMediumMu15",
    "muon1_pt               := ?(muons.size>0)? muons.at(0).pt : -999",
    "muon2_pt               := ?(muons.size>1)? muons.at(1).pt : -999",
    "muon1_eta              := ?(muons.size>0)? muons.at(0).eta : -999",
    "muon2_eta              := ?(muons.size>1)? muons.at(1).eta : -999",
    "muon1_phi              := ?(muons.size>0)? muons.at(0).phi : -999",
    "muon2_phi              := ?(muons.size>1)? muons.at(1).phi : -999",
    "muon1_e                := ?(muons.size>0)? muons.at(0).energy : -999",
    "muon2_e                := ?(muons.size>1)? muons.at(1).energy : -999",
    "muon1_ch               := ?(muons.size>0)? muons.at(0).charge : -999",
    "muon2_ch               := ?(muons.size>1)? muons.at(1).charge : -999",
    "muon1_iso              := ?(muons.size>0)? (muons.at(0).pfIsolationR04().sumChargedHadronPt+ max( 0.,muons.at(0).pfIsolationR04().sumNeutralHadronEt + muons.at(0).pfIsolationR04().sumPhotonEt - 0.5 * muons.at(0).pfIsolationR04().sumPUPt)) / ( muons.at(0).pt ) : -999.",
    "muon2_iso              := ?(muons.size>1)? (muons.at(1).pfIsolationR04().sumChargedHadronPt+ max( 0.,muons.at(1).pfIsolationR04().sumNeutralHadronEt + muons.at(1).pfIsolationR04().sumPhotonEt - 0.5 * muons.at(1).pfIsolationR04().sumPUPt)) / ( muons.at(1).pt ) : -999.",
    "muon1_chi2             := ?(muons.size>0)? muons.at(0).innerTrack().normalizedChi2 : -999",
    "muon2_chi2             := ?(muons.size>1)? muons.at(1).innerTrack().normalizedChi2 : -999",
    "muon1_mHits            := ?(muons.size>0)? muons.at(0).innerTrack().hitPattern().numberOfValidMuonHits : -999",
    "muon2_mHits            := ?(muons.size>1)? muons.at(1).innerTrack().hitPattern().numberOfValidMuonHits : -999",
    "muon1_mStations        := ?(muons.size>0)? muons.at(0).numberOfMatchedStations : -999",
    "muon2_mStations        := ?(muons.size>1)? muons.at(1).numberOfMatchedStations : -999",
    "muon1_dxy              := ?(muons.size>0)? getLeadingLeptonVertexDxy(\"muon\"): -999",
    "muon2_dxy              := ?(muons.size>0)? getSubLeadingLeptonVertexDxy(\"muon\"):  -999",
    "muon1_diphodxy         := ?(muons.size>0)? getLeadingLeptonDiphoVertexDxy(\"muon\"):  -999",
    "muon2_diphodxy         := ?(muons.size>1)? getSubLeadingLeptonDiphoVertexDxy(\"muon\"):  -999",
    "muon1_dz               := ?(muons.size>0)? getLeadingLeptonVertexDz(\"muon\") : -999",
    "muon2_dz               := ?(muons.size>1)? getSubLeadingLeptonVertexDz(\"muon\"):  -999",
    "muon1_diphodz          := ?(muons.size>0)? getLeadingLeptonDiphoVertexDz(\"muon\"):  -999",
    "muon2_diphodz          := ?(muons.size>1)? getSubLeadingLeptonDiphoVertexDz(\"muon\"):  -999",
    "muon1_pxHits           := ?(muons.size>0)? muons.at(0).innerTrack().hitPattern().numberOfValidPixelHits : -999",
    "muon2_pxHits           := ?(muons.size>1)? muons.at(1).innerTrack().hitPattern().numberOfValidPixelHits : -999",
    "muon1_tkLayers         := ?(muons.size>0)? muons.at(0).innerTrack().hitPattern().trackerLayersWithMeasurement : -999",
    "muon2_tkLayers         := ?(muons.size>1)? muons.at(1).innerTrack().hitPattern().trackerLayersWithMeasurement : -999",
    "muon1_PassTight        := ?(muons.size>0)? MuPassTight.at(0) : -999",
    "muon2_PassTight        := ?(muons.size>1)? MuPassTight.at(1) : -999",
    "muon1_dPhiMET          := ?(muons.size>0)? dPhi_Muon1_MET() : -999",
    "muon2_dPhiMET          := ?(muons.size>1)? dPhi_Muon2_MET() : -999",
    

]

#print lepton_variables["ele1_pt"]
jet_variables=[
    
    "n_fwdjets              := Jets_EtaSorted.size",
    "fwdjet1_pt             := ?Jets_EtaSorted.size>0? Jets_EtaSorted.at(0).pt : -999",
    "fwdjet2_pt             := ?Jets_EtaSorted.size>1? Jets_EtaSorted.at(1).pt : -999",
    "fwdjet3_pt             := ?Jets_EtaSorted.size>2? Jets_EtaSorted.at(2).pt : -999",
    "fwdjet1_eta            := ?Jets_EtaSorted.size>0? Jets_EtaSorted.at(0).eta: -999.",
    "fwdjet2_eta            := ?Jets_EtaSorted.size>1? Jets_EtaSorted.at(1).eta:-999.",
    "fwdjet3_eta            := ?Jets_EtaSorted.size>2? Jets_EtaSorted.at(2).eta:-999.",
    "fwdjet4_eta            := ?Jets_EtaSorted.size>3? Jets_EtaSorted.at(3).eta: -999.",
    "fwdjet5_eta            := ?Jets_EtaSorted.size>4? Jets_EtaSorted.at(4).eta:-999.",
    "fwdjet6_eta            := ?Jets_EtaSorted.size>5? Jets_EtaSorted.at(5).eta:-999.",
    "fwdjet7_eta            := ?Jets_EtaSorted.size>6? Jets_EtaSorted.at(6).eta: -999.",
    "fwdjet8_eta            := ?Jets_EtaSorted.size>7? Jets_EtaSorted.at(7).eta:-999.",
    "fwdjet9_eta            := ?Jets_EtaSorted.size>8? Jets_EtaSorted.at(8).eta:-999.",
    "fwdjet1_phi            := ?Jets_EtaSorted.size>0? Jets_EtaSorted.at(0).phi: -999.",
    "fwdjet2_phi            := ?Jets_EtaSorted.size>1? Jets_EtaSorted.at(1).phi: -999.",
    "fwdjet3_phi            := ?Jets_EtaSorted.size>2? Jets_EtaSorted.at(2).phi: -999.",
    "fwdjet1_e              := ?Jets_EtaSorted.size>0? Jets_EtaSorted.at(0).energy: -999.",
    "fwdjet2_e              := ?Jets_EtaSorted.size>1? Jets_EtaSorted.at(1).energy: -999.",
    "fwdjet3_e              := ?Jets_EtaSorted.size>2? Jets_EtaSorted.at(2).energy: -999.",
    
    "n_M_bjets                := nMedium_bJets",
    "n_L_bjets                := nLoose_bJets",
    "n_T_bjets                := nTight_bJets",

#    "n_centraljets	    := nCentralJets",
#    "n_forwardjets	    := nForwardJets",

    "n_bjets                := bJets.size",
    "bjet1_pt               := ?bJets.size>0? bJets.at(0).pt : -999",
    "bjet2_pt               := ?bJets.size>1? bJets.at(1).pt : -999",
    "bjet3_pt               := ?bJets.size>2? bJets.at(2).pt : -999",
    "bjet1_eta              := ?bJets.size>0? bJets.at(0).eta: -999.",
    "bjet2_eta              := ?bJets.size>1? bJets.at(1).eta:-999.",
    "bjet3_eta              := ?bJets.size>2? bJets.at(2).eta:-999.",
    "bjet1_phi              := ?bJets.size>0? bJets.at(0).phi: -999.",
    "bjet2_phi              := ?bJets.size>1? bJets.at(1).phi: -999.",
    "bjet3_phi              := ?bJets.size>2? bJets.at(2).phi: -999.",
    "bjet1_e                := ?bJets.size>0? bJets.at(0).energy: -999.",
    "bjet2_e                := ?bJets.size>1? bJets.at(1).energy: -999.",
    "bjet3_e                := ?bJets.size>2? bJets.at(2).energy: -999.",
#    'bjet1_discr            := ?bJets.size>0? bJets.at(0).bDiscriminator( "'+ flashggBTag +'" ) : -999',
#    'bjet2_discr            := ?bJets.size>1? bJets.at(1).bDiscriminator( "'+ flashggBTag +'" ) : -999',
#    'bjet3_discr            := ?bJets.size>2? bJets.at(2).bDiscriminator( "'+ flashggBTag +'" ) : -999',
    'bjet1_discr  := ?bJets.size>0? (bJets.at(0).bDiscriminator( "'+ flashggDeepCSVb +'" ) + bJets.at(0).bDiscriminator( "'+ flashggDeepCSVbb +'" )) : -999',
    'bjet2_discr  := ?bJets.size>1? (bJets.at(1).bDiscriminator( "'+ flashggDeepCSVb +'" ) + bJets.at(1).bDiscriminator( "'+ flashggDeepCSVbb +'" )) : -999',
    'bjet3_discr  := ?bJets.size>2? (bJets.at(2).bDiscriminator( "'+ flashggDeepCSVb +'" ) + bJets.at(2).bDiscriminator( "'+ flashggDeepCSVbb +'" )) : -999',
#    'bjet1_discr_1 := ?bJets.size>0? bDiscriminatorValue.at(0) : -999',
#    'bjet2_discr_2 := ?bJets.size>1? bDiscriminatorValue.at(1) : -999',
#    'bjet3_discr_3 := ?bJets.size>2? bDiscriminatorValue.at(2) : -999',


    # new variables
    "n_jets                 := jets.size",
    "jet1_pt                := ?jets.size>0? jets.at(0).pt : -999",
    "jet2_pt                := ?jets.size>1? jets.at(1).pt : -999",
    "jet3_pt                := ?jets.size>2? jets.at(2).pt : -999",
    "jet1_eta               := ?jets.size>0? jets.at(0).eta : -999",
    "jet2_eta               := ?jets.size>1? jets.at(1).eta : -999",
    "jet3_eta               := ?jets.size>2? jets.at(2).eta : -999",
    "jet1_phi               := ?jets.size>0? jets.at(0).phi : -999",
    "jet2_phi               := ?jets.size>1? jets.at(1).phi : -999",
    "jet3_phi               := ?jets.size>2? jets.at(2).phi : -999",
    "jet1_e                 := ?jets.size>0? jets.at(0).energy : -999",
    "jet2_e                 := ?jets.size>1? jets.at(1).energy : -999",
    "jet3_e                 := ?jets.size>2? jets.at(2).energy : -999",

    "recoMET_pt             :=getRECOMET().getCorPt()",
    "recoMET_eta            :=getRECOMET().eta()",
    "recoMET_phi            :=getRECOMET().getCorPhi()",
    "recoMET_e              :=getRECOMET().energy()",
    "solvedMET_pt           :=getMET_Pt(\"SolvedMET\")",
    "solvedMET_eta          :=getMET_Eta(\"SolvedMET\")",
    "solvedMET_phi          :=getMET_Phi(\"SolvedMET\")",
    "solvedMET_e            :=getMET_E(\"SolvedMET\")",
    "dr_leadphobjet          :=getmyfunction()",
    "dr_leptonfwdjet         :=getdRleptonfwdjet",
    "top_mt                 :=gettop_mt()",
    "top_mass               :=gettop_mass()",
    "HT                     :=getHT()"    
]

dr_variable=[
    "dr_tHchainfwdjet        :=getdRtHchainfwdjet()",
    "dr_bjetfwdjet           :=getdRbjetfwdjet()",
#    "dr_leadphobjet	     :=getmyfunction()",
    "dr_subleadphobjet       :=getdRsubleadphobjet()",
    "dr_leadphofwdjet        :=getdRleadphofwdjet()",
    "dr_subleadphofwdjet     :=getdRsubleadphofwdjet()",
    "dr_leptonbjet           :=getdRleptonbjet",
#    "dr_leptonfwdjet	     :=getdRleptonfwdjet",
    "dEta_leptonfwdjet       :=getdEtaleptonfwdjet()",
#    "top_mt		     :=gettop_mt()",
    "lepton_charge           :=getlepton_ch()",
    "n_centraljets           := nCentralJets",
    "n_forwardjets           := nForwardJets",
    "forwardjet1_eta         := ?forwardJet.size>0? forwardJet.at(0).eta : -999 ",
    "forwardjet1_pt          := ?forwardJet.size>0? forwardJet.at(0).pt : -999 ",
    "likelihood_value        :=getlikelihood()",
#    "MVAresult_thq	     :=getthq_mvaresult"
]

thqmva_variables=[
    "bTagWeight             := bTagWeight",
    "bTagWeightUp           := bTagWeightUp",
    "bTagWeightDown         := bTagWeightDown",
    "photonWeights          := photonWeights",
    "FoxWolf                :=getFoxWolframMoment_ONE",
    "Aplanarity             :=getAplanarity()",
    "MET_pt                 :=getRECOMET().getCorPt()",
    "MET_phi                :=getRECOMET().getCorPhi()",
    "MVAresult              :=getmvaresult",
#   "likelihood_value	    :=getlikelihood()"
    "MVAresult_thq          :=getthq_mvaresult"
]

for label in ["HighestBTagVal", "Medium" , "Loose" , "Tight"]:
    thqmva_variables.append('fwdJetEta_{0}             := ?thqleptonicMvaRes("{0}")>-10.? getFwdJet("{0}").eta : -999'.format(label) )
    thqmva_variables.append('MVA_{0}                   := thqleptonicMvaRes("{0}")'.format(label) )
    thqmva_variables.append('bJetPt_{0}                := ?thqleptonicMvaRes("{0}")>-10.? getbJet("{0}").pt : -999'.format(label) )


truth_variables=[
    
    "Photon1_J1_dR       := tagTruth().dR_Ph1_1_FggJet()",
    "Photon1_J2_dR       := tagTruth().dR_Ph1_2_FggJet()",
    "Photon1_J3_dR       := tagTruth().dR_Ph1_3_FggJet()",
    "Photon2_J1_dR        := tagTruth().dR_Ph2_1_FggJet()",
    "Photon2_J2_dR        := tagTruth().dR_Ph2_2_FggJet()",
    "Photon2_J3_dR        := tagTruth().dR_Ph2_3_FggJet()",
    "dRToNearestPartonJ1 := tagTruth().dR_partonMatchingToJ1()",
    "dRToNearestPartonJ2 := tagTruth().dR_partonMatchingToJ2()",
    "dRToNearestPartonJ3 := tagTruth().dR_partonMatchingToJ3()",
    "numberOfLSSMatches  := tagTruth().numberOfMatchesAfterDRCut(0.5)",
    "numberOfLSMatches   := tagTruth().numberOfLeadingAndSubLeadingMatchesAfterDRCut(0.5)",
    "numberOfLMatches    := tagTruth().numberOfLeadingMatchesAfterDRCut(0.5)",
    
    # tag truth information
    "genJetMatchingToJ1_pt                := ?tagTruth().hasClosestGenJetToLeadingJet? tagTruth().closestGenJetToLeadingJet().pt : -999.",
    "genJetMatchingToJ2_pt                := ?tagTruth().hasClosestGenJetToSubLeadingJet? tagTruth().closestGenJetToSubLeadingJet().pt : -999.",
    "genJetMatchingToJ3_pt                := ?tagTruth().hasClosestGenJetToSubSubLeadingJet? tagTruth().closestGenJetToSubSubLeadingJet().pt : -999.",
    "genJetMatchingToJ1_eta               := ?tagTruth().hasClosestGenJetToLeadingJet? tagTruth().closestGenJetToLeadingJet().eta : -999.",
    "genJetMatchingToJ2_eta               := ?tagTruth().hasClosestGenJetToSubLeadingJet? tagTruth().closestGenJetToSubLeadingJet().eta : -999.",
    "genJetMatchingToJ3_eta               := ?tagTruth().hasClosestGenJetToSubSubLeadingJet? tagTruth().closestGenJetToSubSubLeadingJet().eta : -999.",
    "genJetMatchingToJ1_phi               := ?tagTruth().hasClosestGenJetToLeadingJet? tagTruth().closestGenJetToLeadingJet().phi : -999.",
    "genJetMatchingToJ2_phi               := ?tagTruth().hasClosestGenJetToSubLeadingJet? tagTruth().closestGenJetToSubLeadingJet().phi : -999.",
    "genJetMatchingToJ3_phi               := ?tagTruth().hasClosestGenJetToSubSubLeadingJet? tagTruth().closestGenJetToSubSubLeadingJet().phi : -999.",
    "genJetMatchingToJ1_e                 := ?tagTruth().hasClosestGenJetToLeadingJet? tagTruth().closestGenJetToLeadingJet().energy : -999.",
    "genJetMatchingToJ2_e                 := ?tagTruth().hasClosestGenJetToSubLeadingJet? tagTruth().closestGenJetToSubLeadingJet().energy : -999.",
    "genJetMatchingToJ3_e                 := ?tagTruth().hasClosestGenJetToSubSubLeadingJet? tagTruth().closestGenJetToSubSubLeadingJet().energy : -999.",
    "partonMatchingToJ1_pt                := ?tagTruth().hasClosestPartonToLeadingJet? tagTruth().closestPartonToLeadingJet().pt : -999.",
    "partonMatchingToJ2_pt                := ?tagTruth().hasClosestPartonToSubLeadingJet? tagTruth().closestPartonToSubLeadingJet().pt : -999.",
    "partonMatchingToJ3_pt                := ?tagTruth().hasClosestPartonToSubSubLeadingJet? tagTruth().closestPartonToSubSubLeadingJet().pt : -999.",
    "partonMatchingToJ1_eta               := ?tagTruth().hasClosestPartonToLeadingJet? tagTruth().closestPartonToLeadingJet().eta : -999.",
    "partonMatchingToJ2_eta               := ?tagTruth().hasClosestPartonToSubLeadingJet? tagTruth().closestPartonToSubLeadingJet().eta : -999.",
    "partonMatchingToJ3_eta               := ?tagTruth().hasClosestPartonToSubSubLeadingJet? tagTruth().closestPartonToSubSubLeadingJet().eta : -999.",
    "partonMatchingToJ1_phi               := ?tagTruth().hasClosestPartonToLeadingJet? tagTruth().closestPartonToLeadingJet().phi : -999.",
    "partonMatchingToJ2_phi               := ?tagTruth().hasClosestPartonToSubLeadingJet? tagTruth().closestPartonToSubLeadingJet().phi : -999.",
    "partonMatchingToJ3_phi               := ?tagTruth().hasClosestPartonToSubSubLeadingJet? tagTruth().closestPartonToSubSubLeadingJet().phi : -999.",
    "partonMatchingToJ1_e                 := ?tagTruth().hasClosestPartonToLeadingJet? tagTruth().closestPartonToLeadingJet().energy : -999.",
    "partonMatchingToJ2_e                 := ?tagTruth().hasClosestPartonToSubLeadingJet? tagTruth().closestPartonToSubLeadingJet().energy : -999.",
    "partonMatchingToJ3_e                 := ?tagTruth().hasClosestPartonToSubSubLeadingJet? tagTruth().closestPartonToSubSubLeadingJet().energy : -999.",
    
#    "genParticleMatchingToLeadingMuon_pt          := ?tagTruth().hasClosestParticleToLeadingMuon? tagTruth().closestParticleToLeadingMuon().pt : -999.",
   "genParticleMatchingToLeadingMuon_pt          :=tagTruth().pt_genParticleMatchingToLeadingMuon() ",

   "genParticleMatchingToSubLeadingMuon_pt       := ?tagTruth().hasClosestParticleToSubLeadingMuon? tagTruth().closestParticleToSubLeadingMuon().pt : -999.",
    "genParticleMatchingToLeadingMuon_eta         := ?tagTruth().hasClosestParticleToLeadingMuon? tagTruth().closestParticleToLeadingMuon().eta : -999.",
    "genParticleMatchingToSubLeadingMuon_eta      := ?tagTruth().hasClosestParticleToSubLeadingMuon? tagTruth().closestParticleToSubLeadingMuon().eta : -999.",
    "genParticleMatchingToLeadingMuon_phi         := ?tagTruth().hasClosestParticleToLeadingMuon? tagTruth().closestParticleToLeadingMuon().phi : -999.",
    "genParticleMatchingToSubLeadingMuon_phi      := ?tagTruth().hasClosestParticleToSubLeadingMuon? tagTruth().closestParticleToSubLeadingMuon().phi : -999.",
    "genParticleMatchingToLeadingMuon_e           := ?tagTruth().hasClosestParticleToLeadingMuon? tagTruth().closestParticleToLeadingMuon().energy : -999.",
    "genParticleMatchingToSubLeadingMuon_e        := ?tagTruth().hasClosestParticleToSubLeadingMuon? tagTruth().closestParticleToSubLeadingMuon().energy : -999.",
    "genParticleMatchingToLeadingElectron_pt      := ?tagTruth().hasClosestParticleToLeadingElectron? tagTruth().closestParticleToLeadingElectron().pt : -999.", 
    "genParticleMatchingToSubLeadingElectron_pt   := ?tagTruth().hasClosestParticleToSubLeadingElectron? tagTruth().closestParticleToSubLeadingElectron().pt : -999.",
    "genParticleMatchingToLeadingElectron_eta     := ?tagTruth().hasClosestParticleToLeadingElectron? tagTruth().closestParticleToLeadingElectron().eta : -999.",
    "genParticleMatchingToSubLeadingElectron_eta  := ?tagTruth().hasClosestParticleToSubLeadingElectron? tagTruth().closestParticleToSubLeadingElectron().eta : -999.",
    "genParticleMatchingToLeadingElectron_phi     := ?tagTruth().hasClosestParticleToLeadingElectron? tagTruth().closestParticleToLeadingElectron().phi : -999.",
    "genParticleMatchingToSubLeadingElectron_phi  := ?tagTruth().hasClosestParticleToSubLeadingElectron? tagTruth().closestParticleToSubLeadingElectron().phi : -999.",
    "genParticleMatchingToLeadingElectron_e       := ?tagTruth().hasClosestParticleToLeadingElectron? tagTruth().closestParticleToLeadingElectron().energy : -999.",
    "genParticleMatchingToSubLeadingElectron_e    := ?tagTruth().hasClosestParticleToSubLeadingElectron? tagTruth().closestParticleToSubLeadingElectron().energy : -999.",
    
    "genPromptParticleMatchingToLeadingMuon_pt          := ?tagTruth().hasClosestPromptParticleToLeadingMuon? tagTruth().closestPromptParticleToLeadingMuon().pt : -999.",
    "genPromptParticleMatchingToSubLeadingMuon_pt       := ?tagTruth().hasClosestPromptParticleToSubLeadingMuon? tagTruth().closestPromptParticleToSubLeadingMuon().pt : -999.",
    "genPromptParticleMatchingToLeadingMuon_eta         := ?tagTruth().hasClosestPromptParticleToLeadingMuon? tagTruth().closestPromptParticleToLeadingMuon().eta : -999.",
    "genPromptParticleMatchingToSubLeadingMuon_eta      := ?tagTruth().hasClosestPromptParticleToSubLeadingMuon? tagTruth().closestPromptParticleToSubLeadingMuon().eta : -999.",
    "genPromptParticleMatchingToLeadingMuon_phi         := ?tagTruth().hasClosestPromptParticleToLeadingMuon? tagTruth().closestPromptParticleToLeadingMuon().phi : -999.",
    "genPromptParticleMatchingToSubLeadingMuon_phi      := ?tagTruth().hasClosestPromptParticleToSubLeadingMuon? tagTruth().closestPromptParticleToSubLeadingMuon().phi : -999.",
    "genPromptParticleMatchingToLeadingMuon_e           := ?tagTruth().hasClosestPromptParticleToLeadingMuon? tagTruth().closestPromptParticleToLeadingMuon().energy : -999.",
    "genPromptParticleMatchingToSubLeadingMuon_e        := ?tagTruth().hasClosestPromptParticleToSubLeadingMuon? tagTruth().closestPromptParticleToSubLeadingMuon().energy : -999.",
#    "genPromptParticleMatchingToLeadingElectron_pt      := ?tagTruth().hasClosestPromptParticleToLeadingElectron? tagTruth().closestPromptParticleToLeadingElectron().pt : -999.",
     "genPromptParticleMatchingToLeadingElectron_pt      := tagTruth().pt_genPromptParticleMatchingToLeadingElectron()",
    "genPromptParticleMatchingToSubLeadingElectron_pt   := ?tagTruth().hasClosestPromptParticleToSubLeadingElectron? tagTruth().closestPromptParticleToSubLeadingElectron().pt : -999.",
#    "genPromptParticleMatchingToLeadingElectron_eta     := ?tagTruth().hasClosestPromptParticleToLeadingElectron? tagTruth().closestPromptParticleToLeadingElectron().eta : -999.",
    "genPromptParticleMatchingToSubLeadingElectron_eta  := ?tagTruth().hasClosestPromptParticleToSubLeadingElectron? tagTruth().closestPromptParticleToSubLeadingElectron().eta : -999.",
#    "genPromptParticleMatchingToLeadingElectron_phi     := ?tagTruth().hasClosestPromptParticleToLeadingElectron? tagTruth().closestPromptParticleToLeadingElectron().phi : -999.",
    "genPromptParticleMatchingToSubLeadingElectron_phi  := ?tagTruth().hasClosestPromptParticleToSubLeadingElectron? tagTruth().closestPromptParticleToSubLeadingElectron().phi : -999.",
#    "genPromptParticleMatchingToLeadingElectron_e       := ?tagTruth().hasClosestPromptParticleToLeadingElectron? tagTruth().closestPromptParticleToLeadingElectron().energy : -999.",
    "genPromptParticleMatchingToSubLeadingElectron_e    := ?tagTruth().hasClosestPromptParticleToSubLeadingElectron? tagTruth().closestPromptParticleToSubLeadingElectron().energy : -999.",
#    "genPartMatchingToPho1_pt := ?tagTruth().hasClosestParticleToLeadingPhoton()? tagTruth().closestParticleToLeadingPhoton()->pt() : -999.",

    "genMET_pt                            := getMET_Pt(\"allNus\")",
    "genMET_eta                           := getMET_Eta(\"allNus\")",
    "genMET_phi                           := getMET_Phi(\"allNus\")",
    "genMET_e                             := getMET_E(\"allNus\")",
    "promptGenMET_pt                      := getMET_Pt(\"allPromptNus\")",
    "promptGenMET_eta                     := getMET_Eta(\"allPromptNus\")",
    "promptGenMET_phi                     := getMET_Phi(\"allPromptNus\")",
    "promptGenMET_e                       := getMET_E(\"allPromptNus\")",
    "genMETTrue_pt                        := getMET_Pt(\"genMetTrue\")",
    "genMETTrue_eta                       := getMET_Eta(\"genMetTrue\")",
    "genMETTrue_phi                       := getMET_Phi(\"genMetTrue\")",
    "genMETTrue_e                         := getMET_E(\"genMetTrue\")"    
    ]


# thqSystematicVariables = [
#     "diphoMVA[20,-1,1] := diPhotonMVA().result",
#     "n_jets[5,0,5] := jets.size",
#     "n_M_bjets[3,0,3] := nMedium_bJets",
#     "LeptonType[3,0,3]:=getLeptonType()",
#     "MET[10,0,300]    :=getMET()",
# ]
thqSystematicVariables = [
    "fwdjet1_eta := ?Jets_EtaSorted.size>0? Jets_EtaSorted.at(0).eta: -999.",
    "diphoMVA    := diPhotonMVA().result",
    "n_jets      := jets.size",
    "n_L_bjets   := nLoose_bJets",
    "n_T_bjets   := nTight_bJets",
    "n_M_bjets   := nMedium_bJets",
    "LeptonType  := getLeptonType()",
    "MET_pt      := getRECOMET().getCorPt()",
    "HT          := getHT()"
]
for label in ["Medium" ]: #"HighestBTagVal", "Loose" , "Tight"]:
    thqSystematicVariables.append('fwdJetEta_{0}             := ?thqleptonicMvaRes("{0}")>-10.? getFwdJet("{0}").eta : -999'.format(label) )
    thqSystematicVariables.append('MVA_{0}                   := thqleptonicMvaRes("{0}")'.format(label) )
    thqSystematicVariables.append('bJetPt_{0}              := ?thqleptonicMvaRes("{0}")>-10.? getbJet("{0}").pt : -999'.format(label) )


theoweight_variables=[
    "weight_electronVetoSF:=weight(\"electronVetoSFCentral\")",
    "weight_PreselSF:=weight(\"PreselSFCentral\")",
    "weight_TriggerWeight:=weight(\"TriggerWeightCentral\")",
    "weight_LooseMvaSF:=weight(\"LooseMvaSFCentral\")",
    "weight_FracRVWeight:=weight(\"FracRVWeightCentral\")",
    "weight_FracRVNvtxWeight:=weight(\"FracRVNvtxWeightCentral\")",
    "weight_SigmaEOverESmearing:=weight(\"SigmaEOverESmearingCentral\")",
    "weight_MuonMediumIDWeight:=weight(\"MuonMediumIDWeightCentral\")",
    "weight_MuonLooseRelISOWeight:=weight(\"MuonLooseRelISOWeightCentral\")",
    "weight_ElectronWeight:=weight(\"ElectronWeightCentral\")",
    "weight_JEC:=weight(\"JECCentral\")",
    "weight_JER:=weight(\"JERCentral\")",
    "weight_JetBTagCutWeight:=weight(\"JetBTagCutWeightCentral\")",
    "weight_JetBTagReshapeWeight:=weight(\"JetBTagReshapeWeightCentral\")",
    "alphaUp   := getAlphaUp()",
    "alphaDown := getAlphaDown()",
    "pdfnlo    := getPdfNLO()"
]

theoweight_variables +=[
    "scaleMuFUp          := getScale(0)",
    "scaleMuFDown        := getScale(1)",
    "scaleMuRUp          := getScale(2)",
    "scaleMuFUpMuRUp     := getScale(3)",
    "scaleMuFDownMuRUp   := getScale(4)",
    "scaleMuRDown        := getScale(5)",
    "scaleMuFUpMuRDown   := getScale(6)",
    "scaleMuFDownMuRDown := getScale(7)"
    ]

for i in range(1):
    theoweight_variables +=["pdf_%i := getPdf(%i)" % (i,i)]

theoctcvweight_variables = []
for i in range(1):
    theoctcvweight_variables +=["ctcv_%i := getCtCv(%i)" % (i,i)]


