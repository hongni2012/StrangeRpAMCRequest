import FWCore.ParameterSet.Config as cms
from GeneratorInterface.ReggeGribovPartonMCInterface.ReggeGribovPartonMC_AdvancedParameters_cfi import *

generator = cms.EDFilter("ReggeGribovPartonMCGeneratorFilter",
                     ReggeGribovPartonMCAdvancedParameters,
                     beammomentum = cms.double(4000),
                     targetmomentum = cms.double(-1577),
                     beamid = cms.int32(1),
                     targetid = cms.int32(208),
                     model = cms.int32(0),
                     )

configurationMetadata = cms.untracked.PSet(
     version = cms.untracked.string('$Revision: 1.4 $'),
     name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/GeneratorInterface/ReggeGribovPartonMCInterface/python/ReggeGribovPartonMC_EposLHC_5TeV_pPb_cfi.py,v $'),
     annotation = cms.untracked.string('ReggeGribovMC generator')
     )

particlefilter = cms.EDFilter("MCSingleParticleFilter",
    Status = cms.untracked.vint32(1),
    MaxEta = cms.untracked.vdouble(2.4),
    MinEta = cms.untracked.vdouble(-2.4),
    MinPt = cms.untracked.vdouble(5.9),
    ParticleID = cms.untracked.vint32(310)
)

ProductionFilterSequence = cms.Sequence(generator+particlefilter)
