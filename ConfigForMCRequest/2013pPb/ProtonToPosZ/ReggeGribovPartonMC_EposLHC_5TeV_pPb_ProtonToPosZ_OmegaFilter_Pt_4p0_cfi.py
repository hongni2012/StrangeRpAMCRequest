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

particlefilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(1),
    MaxRapidity = cms.untracked.double(2.4),
    MinRapidity = cms.untracked.double(-2.4),
    MinPt = cms.untracked.double(4.0),
    MaxPt = cms.untracked.double(999.),
    ParticleID = cms.untracked.int32(3334),
)

ProductionFilterSequence = cms.Sequence(generator+particlefilter)
