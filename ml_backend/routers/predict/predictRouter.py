import json, pickle
import pandas as pd
from typing import List, Dict
from pathlib import Path

from routers.predict.router import router
from models.allModels.CRUD.schema import MLInputX, MLOutputY, MLInputXFiltered, MLOutputYFull
from fastapi.encoders import jsonable_encoder

from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse



examl = {
   "adb019dcde61d092941e0fec4e89b405130df238877e2611c330ae95a7266487":{
      "14aa1250a60229a6f0fc62e973fe757d076f897e4bc93a4238497af4fe06a00d":[
         {
            "BRAT":0.9321553374541728,
            "DEGT":0.0,
            "DELFN":17.788759262399356,
            "DELN1":6.243883756000001,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0002732203969804678,
            "EGTC":0.17206797920096026,
            "EGTHDM":72.18695829999984,
            "EGTHDM_D":2.430152889999995,
            "GEGTMC":-0.22430922657627062,
            "GN2MC":0.002836200003827143,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":82.6244048999999,
            "PCN12I":83.31227305911611,
            "PCN1AR":85.54979605391772,
            "PCN1BR":85.99986806254506,
            "PCN1K":85.22966000000001,
            "PCN2C":0.010730835118973402,
            "SLOATL":66.69866180000007,
            "SLOATL_D":0.8117599490000008,
            "WBE":1.180699248839953,
            "WBI":-0.00022226926501157546,
            "WFMP":-0.001044587431154896,
            "ZPCN25_D":0.05000305180000006,
            "ZT49_D":-2.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"14aa1250a60229a6f0fc62e973fe757d076f897e4bc93a4238497af4fe06a00d",
            "id":191793,
            "flight_datetime":"2022-02-0803:50:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         },
         {
            "BRAT":0.8781616746154426,
            "DEGT":0.0,
            "DELFN":13.624891202421695,
            "DELN1":4.941905548,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":0.17206797920096026,
            "EGTHDM":67.3817673000001,
            "EGTHDM_D":1.2818069500000027,
            "GEGTMC":0.056895793878148665,
            "GN2MC":-0.003326027505432906,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":85.80401609999996,
            "PCN12I":86.61467067934359,
            "PCN1AR":86.52110654182991,
            "PCN1BR":87.35877397983481,
            "PCN1K":86.2385329999999,
            "PCN2C":0.012918704614302159,
            "SLOATL":65.09348299999992,
            "SLOATL_D":0.4252700810000005,
            "WBE":1.1560896457267478,
            "WBI":-0.0026830180701795494,
            "WFMP":0.7440126375285083,
            "ZPCN25_D":0.09999847410000004,
            "ZT49_D":-1.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"14aa1250a60229a6f0fc62e973fe757d076f897e4bc93a4238497af4fe06a00d",
            "id":191827,
            "flight_datetime":"2022-05-1504:10:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         },
         {
            "BRAT":0.0004550808683766159,
            "DEGT":0.0,
            "DELFN":12.492224432719375,
            "DELN1":5.060831882,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008324956238809829,
            "EGTC":0.1701121027650926,
            "EGTHDM":65.40029909999997,
            "EGTHDM_D":4.75512694999999,
            "GEGTMC":0.18205306208138852,
            "GN2MC":0.009221540947739111,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":91.89396670000014,
            "PCN12I":92.39923677032802,
            "PCN1AR":89.58136048505986,
            "PCN1BR":90.70813093177694,
            "PCN1K":89.62342069999983,
            "PCN2C":0.0074433406304661,
            "SLOATL":64.43571470000005,
            "SLOATL_D":1.561893459999996,
            "WBE":-0.09106384191115957,
            "WBI":-0.00037385984695742123,
            "WFMP":0.6025191423442969,
            "ZPCN25_D":0.04999542240000003,
            "ZT49_D":-4.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"14aa1250a60229a6f0fc62e973fe757d076f897e4bc93a4238497af4fe06a00d",
            "id":191918,
            "flight_datetime":"2022-07-1604:38:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "47ea147feec375157fdc4ef94bce6803be3f847399e52aab06d2414ce2ea6b92":{
      "dda2a4e5f8b7c39356d9da1279e61b44bf4362c6cf46a0421d1265e6e9b176ed":[
         {
            "BRAT":8.773130086626878e-05,
            "DEGT":0.0,
            "DELFN":22.390930699531417,
            "DELN1":7.409583570000001,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0002732203969804678,
            "EGTC":0.17206797920096026,
            "EGTHDM":84.84693909999993,
            "EGTHDM_D":9.959304810000022,
            "GEGTMC":0.7397262309647641,
            "GN2MC":0.0020474089068944507,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":84.09664150000009,
            "PCN12I":84.89726582729898,
            "PCN1AR":83.50572382823069,
            "PCN1BR":83.59753781642011,
            "PCN1K":83.74441529999986,
            "PCN2C":0.002177082510981357,
            "SLOATL":70.99703979999984,
            "SLOATL_D":3.358810419999998,
            "WBE":-0.06957572153136335,
            "WBI":0.00038479935544405913,
            "WFMP":1.1004956485472888,
            "ZPCN25_D":-0.05000305180000006,
            "ZT49_D":-9.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"dda2a4e5f8b7c39356d9da1279e61b44bf4362c6cf46a0421d1265e6e9b176ed",
            "id":191795,
            "flight_datetime":"2022-05-3122:40:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ],
      "9e7ff478861887972d5f37170fb9a980d273e527a774ee5a7cbcc5473415d53e":[
         {
            "BRAT":0.921144186164474,
            "DEGT":0.0,
            "DELFN":12.608605222395672,
            "DELN1":4.744900084000001,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":0.01598003430948763,
            "EGTHDM":65.73619080000005,
            "EGTHDM_D":-12.753410300000024,
            "GEGTMC":0.014527733570143163,
            "GN2MC":0.0025334632181989135,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":87.43790439999992,
            "PCN12I":87.64248733352082,
            "PCN1AR":87.0217807967074,
            "PCN1BR":87.5984083844095,
            "PCN1K":86.93097690000005,
            "PCN2C":0.01494990973262384,
            "SLOATL":64.54705809999997,
            "SLOATL_D":-4.330368039999997,
            "WBE":1.1991885526348516,
            "WBI":-0.001214766167383741,
            "WFMP":0.6510193635589256,
            "ZPCN25_D":0.0,
            "ZT49_D":11.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"9e7ff478861887972d5f37170fb9a980d273e527a774ee5a7cbcc5473415d53e",
            "id":191880,
            "flight_datetime":"2022-07-2311:16:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "fd69b53f644e0e39b94d3e536daab93467b82d061cc31ca29755bf83f21cc98b":{
      "967dbe8a86e92e1b19788c361a4f4766caf15d97ad6bf77a6587c33d46b179bf":[
         {
            "BRAT":0.0005802887496126098,
            "DEGT":0.0,
            "DELFN":13.273547286966675,
            "DELN1":5.036321255,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0014400072816702471,
            "EGTC":0.039805694526459795,
            "EGTHDM":38.46931839999991,
            "EGTHDM_D":-10.226287800000016,
            "GEGTMC":0.15047225304660725,
            "GN2MC":0.0019487296367150231,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":89.85014340000006,
            "PCN12I":90.80934387608589,
            "PCN1AR":88.165302759373,
            "PCN1BR":86.90441322367529,
            "PCN1K":88.25019069999989,
            "PCN2C":0.0074433406304661,
            "SLOATL":55.72859570000006,
            "SLOATL_D":-3.2866401699999988,
            "WBE":-0.04887611666469982,
            "WBI":0.00026555574799353365,
            "WFMP":0.5146461922483516,
            "ZPCN25_D":0.09999847410000004,
            "ZT49_D":9.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.31967040999999996,
            "engine_id":"967dbe8a86e92e1b19788c361a4f4766caf15d97ad6bf77a6587c33d46b179bf",
            "id":191845,
            "flight_datetime":"2022-06-2221:52:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "a01939fb3fb61c0277349d8fa8d6a683ef13e127ebb6f95c2f43fed85cfc4a3b":{
      "f648cc7c0eca92a230aab5023ca2321f29be8ae4dfea5571d0fb53db16892e69":[
         {
            "BRAT":0.8816308499714405,
            "DEGT":0.0,
            "DELFN":14.629224437506856,
            "DELN1":4.863893174,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":0.010448423724599535,
            "EGTHDM":54.87248989999992,
            "EGTHDM_D":-2.2754135099999946,
            "GEGTMC":-0.06482305677503085,
            "GN2MC":0.0009099951076754445,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":86.30192569999983,
            "PCN12I":86.80853885194477,
            "PCN1AR":86.9676043094162,
            "PCN1BR":87.4695802573648,
            "PCN1K":86.63594819999992,
            "PCN2C":0.01494990973262384,
            "SLOATL":60.980888400000076,
            "SLOATL_D":-0.7426071169999999,
            "WBE":1.136274481681716,
            "WBI":-0.0002602298894359197,
            "WFMP":0.2402576349154901,
            "ZPCN25_D":0.10000610400000015,
            "ZT49_D":2.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"f648cc7c0eca92a230aab5023ca2321f29be8ae4dfea5571d0fb53db16892e69",
            "id":191863,
            "flight_datetime":"2022-05-2403:37:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "fc952bb014fc5706d37a69df457c83637959ff94fac3a822d96a8af0b3a3c597":{
      "d74ae6e72e9c56afba1190e583521073f567ea4e6739e7f4ca60c55a50bf1c2a":[
         {
            "BRAT":0.18418676991403182,
            "DEGT":0.0,
            "DELFN":13.25351975665358,
            "DELN1":4.113895754,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.004236056191617332,
            "EGTC":0.039805694526459795,
            "EGTHDM":67.8793640000001,
            "EGTHDM_D":-9.273262019999978,
            "GEGTMC":0.03351080719397988,
            "GN2MC":0.0027790441333300077,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":88.06542210000022,
            "PCN12I":88.80241153380622,
            "PCN1AR":88.13970434870409,
            "PCN1BR":88.14522612036694,
            "PCN1K":88.10942839999998,
            "PCN2C":0.0074433406304661,
            "SLOATL":65.25904079999991,
            "SLOATL_D":-3.1406326300000047,
            "WBE":0.19014777243428183,
            "WBI":0.0006664317568038202,
            "WFMP":0.0005713759496071627,
            "ZPCN25_D":0.0,
            "ZT49_D":9.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"d74ae6e72e9c56afba1190e583521073f567ea4e6739e7f4ca60c55a50bf1c2a",
            "id":191848,
            "flight_datetime":"2022-06-0913:24:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "8b013b1be61b0047e5a6ea6771810d71f987831f5c93293fb7a2b6f458a41f35":{
      "9c8cd934ffbca8d075e1c2b0e70015dff7ee31e54ead92a33a972c9aa2aedfa3":[
         {
            "BRAT":-0.00042067145041761717,
            "DEGT":0.0,
            "DELFN":23.127648593288363,
            "DELN1":8.21535797,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.004020204882556675,
            "EGTC":-0.08270974086607032,
            "EGTHDM":52.17237850000004,
            "EGTHDM_D":-5.252136230000008,
            "GEGTMC":-0.13165751965749056,
            "GN2MC":0.004350604162211234,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":84.93537139999995,
            "PCN12I":85.26468981269797,
            "PCN1AR":83.84051628674666,
            "PCN1BR":84.09758506202614,
            "PCN1K":83.85457609999982,
            "PCN2C":-0.003978896449137,
            "SLOATL":60.10553739999986,
            "SLOATL_D":-1.7149925200000014,
            "WBE":-0.015045306078049409,
            "WBI":0.000781043605625657,
            "WFMP":0.5606737997524328,
            "ZPCN25_D":0.0,
            "ZT49_D":4.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"9c8cd934ffbca8d075e1c2b0e70015dff7ee31e54ead92a33a972c9aa2aedfa3",
            "id":191856,
            "flight_datetime":"2022-06-0315:07:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         },
         {
            "BRAT":-9.479990015895036e-05,
            "DEGT":0.0,
            "DELFN":12.538945287405651,
            "DELN1":4.676720141999999,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":-0.08466561730193799,
            "EGTHDM":59.90275959999992,
            "EGTHDM_D":-4.877223969999992,
            "GEGTMC":0.08775108518305852,
            "GN2MC":0.002269888301378671,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":90.69604489999989,
            "PCN12I":91.11127667912017,
            "PCN1AR":90.01471108495043,
            "PCN1BR":90.62114719879442,
            "PCN1K":90.072319,
            "PCN2C":-0.0007726693192344407,
            "SLOATL":62.62331009999987,
            "SLOATL_D":-1.6142539999999992,
            "WBE":-0.010066689539187462,
            "WBI":-0.000328807771894354,
            "WFMP":0.2402576349154901,
            "ZPCN25_D":0.0,
            "ZT49_D":4.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"9c8cd934ffbca8d075e1c2b0e70015dff7ee31e54ead92a33a972c9aa2aedfa3",
            "id":191996,
            "flight_datetime":"2022-05-1715:07:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ],
      "9d02dfc19ca7dfb65a752a0b6af2169a07222471639c4ea9a6595f035e556894":[
         {
            "BRAT":-0.0012342792766258336,
            "DEGT":0.0,
            "DELFN":15.378665045007057,
            "DELN1":5.77397237,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0054779193603415825,
            "EGTC":0.10879500187773072,
            "EGTHDM":67.55532839999985,
            "EGTHDM_D":1.9454345700000026,
            "GEGTMC":-0.11799273979827563,
            "GN2MC":0.004350604162211234,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":88.40000150000009,
            "PCN12I":88.40593042812223,
            "PCN1AR":86.58015777483858,
            "PCN1BR":86.53376950401011,
            "PCN1K":86.58100129999997,
            "PCN2C":0.002928504729473156,
            "SLOATL":65.15125270000016,
            "SLOATL_D":0.6448745730000011,
            "WBE":0.005948136636554774,
            "WBI":0.00036060658729371645,
            "WFMP":0.5606737997524328,
            "ZPCN25_D":-0.09999847410000004,
            "ZT49_D":-2.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"9d02dfc19ca7dfb65a752a0b6af2169a07222471639c4ea9a6595f035e556894",
            "id":192048,
            "flight_datetime":"2022-06-2218:34:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "30c6570a99d5554ca6975f2ca386e7d3af1b3b92dc063e0d34d90223f5d2e7dd":{
      "f5a5af90e581be9a4b812c1000c5a9fa938741889bab629817a4f48b5aaca69c":[
         {
            "BRAT":0.8695535997112938,
            "DEGT":0.0,
            "DELFN":17.721094251119442,
            "DELN1":6.677229976,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.004800053968373333,
            "EGTC":0.04176157096232748,
            "EGTHDM":66.80974580000013,
            "EGTHDM_D":-1.5081558200000011,
            "GEGTMC":0.06696402616618251,
            "GN2MC":0.007079787406326765,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":85.47481539999995,
            "PCN12I":86.02636526378318,
            "PCN1AR":84.70544277669207,
            "PCN1BR":83.99496598834654,
            "PCN1K":84.7653045999998,
            "PCN2C":0.012918704614302159,
            "SLOATL":64.90338900000005,
            "SLOATL_D":-0.5024185179999994,
            "WBE":1.1272409579064802,
            "WBI":-0.0011039547797431824,
            "WFMP":-0.27768329385286655,
            "ZPCN25_D":-0.10000610400000015,
            "ZT49_D":2.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":-0.39683105500000004,
            "engine_id":"f5a5af90e581be9a4b812c1000c5a9fa938741889bab629817a4f48b5aaca69c",
            "id":191904,
            "flight_datetime":"2022-05-2615:05:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "c896242ec59470fd98fe0e3b28c6badc98c5f0c20038f44c583248c0fed2ca0f":{
      "87dc3095fc06e4007876868455aa719043cbce519a7939cf1598fad1cbcea42b":[
         {
            "BRAT":0.9240525051338867,
            "DEGT":0.0,
            "DELFN":24.777590457850135,
            "DELN1":8.402278229999999,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":0.09331913358722126,
            "EGTHDM":82.96527100000002,
            "EGTHDM_D":3.309356689999999,
            "GEGTMC":1.1080535022202094,
            "GN2MC":0.00016126310749793474,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":82.6815720000002,
            "PCN12I":83.21284710607696,
            "PCN1AR":82.92764045268963,
            "PCN1BR":83.73214125125133,
            "PCN1K":82.8919830000002,
            "PCN2C":0.010730835118973402,
            "SLOATL":70.35171509999988,
            "SLOATL_D":1.125976559999999,
            "WBE":1.1954457706970576,
            "WBI":-0.00028846199438978514,
            "WFMP":2.65571711135921,
            "ZPCN25_D":-0.10000610400000015,
            "ZT49_D":-3.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"87dc3095fc06e4007876868455aa719043cbce519a7939cf1598fad1cbcea42b",
            "id":191914,
            "flight_datetime":"2022-05-2718:30:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "62a728b0b2cb8efb20f13941e7fe44058122f9869ab0a9d970fcd5080d0eae86":{
      "b8b60d46930b3e30ccb9153507c4252b36234f4d8e3f8d7d3b015308affef486":[
         {
            "BRAT":0.0007149019375883537,
            "DEGT":0.0,
            "DELFN":19.11579468451205,
            "DELN1":6.537097216000001,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":-0.13550672004802508,
            "EGTHDM":54.30543519999994,
            "EGTHDM_D":-8.351356509999988,
            "GEGTMC":0.0342273099754281,
            "GN2MC":-0.001590574916102057,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":88.37127690000007,
            "PCN12I":89.01976980440986,
            "PCN1AR":87.14758431204301,
            "PCN1BR":88.3823648773635,
            "PCN1K":87.14354710000022,
            "PCN2C":0.0074433406304661,
            "SLOATL":60.796691900000035,
            "SLOATL_D":-2.7534256000000075,
            "WBE":0.01663708588019666,
            "WBI":-0.0005516048052543646,
            "WFMP":-1.2204684159053605,
            "ZPCN25_D":0.25,
            "ZT49_D":7.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"b8b60d46930b3e30ccb9153507c4252b36234f4d8e3f8d7d3b015308affef486",
            "id":192024,
            "flight_datetime":"2022-07-0713:53:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "84bdcd156603935b711cccd5a7c44b59a475e44429ab0f8a27ec18e175817436":{
      "424ecc7768f1e2b55e18ef655bfad0464ee28370a47ebbd597fda40518263463":[
         {
            "BRAT":0.0004972354856472181,
            "DEGT":0.0,
            "DELFN":11.263445277986449,
            "DELN1":3.755426573,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.006415595610268628,
            "EGTC":0.1701121027650926,
            "EGTHDM":71.7580643000001,
            "EGTHDM_D":-7.0271377599999925,
            "GEGTMC":0.14286349259933903,
            "GN2MC":-0.001054187915385651,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":89.78076169999991,
            "PCN12I":90.81668359272315,
            "PCN1AR":88.50505868704268,
            "PCN1BR":89.8657441188836,
            "PCN1K":88.58191679999987,
            "PCN2C":0.0074433406304661,
            "SLOATL":66.55480960000016,
            "SLOATL_D":-2.387107850000005,
            "WBE":-0.02388591930340983,
            "WBI":-0.0007916195552023189,
            "WFMP":-0.6912941892587101,
            "ZPCN25_D":0.09999847410000004,
            "ZT49_D":7.0,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"424ecc7768f1e2b55e18ef655bfad0464ee28370a47ebbd597fda40518263463",
            "id":192051,
            "flight_datetime":"2022-07-0415:05:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   },
   "beb81e71a33a62f368c0971987d5b5214214cd70acfd06d934c02b9f51958aa4":{
      "b8f7e4972c4313a7a80e45d04532a7e549461bc38e137f9987d537bc10373935":[
         {
            "BRAT":0.12512713779619364,
            "DEGT":0.0,
            "DELFN":24.491687342634908,
            "DELN1":8.623665617,
            "DELVSV":1.7614456514412082e-05,
            "DPOIL":-0.0008807320547697322,
            "EGTC":0.04176157096232748,
            "EGTHDM":52.936080899999986,
            "EGTHDM_D":3.8057632399999943,
            "GEGTMC":0.09636851642790753,
            "GN2MC":0.002583662360931695,
            "GPCN25":0.0,
            "GWFM":0.0,
            "PCN12":84.17148590000012,
            "PCN12I":84.8607988039207,
            "PCN1AR":82.92467158989872,
            "PCN1BR":83.85767056108033,
            "PCN1K":83.02988430000003,
            "PCN2C":0.002702564887844093,
            "SLOATL":60.35268400000011,
            "SLOATL_D":1.224006650000003,
            "WBE":0.11965019273801997,
            "WBI":-0.0007476938125508996,
            "WFMP":0.8276107111332738,
            "ZPCN25_D":0.04999542240000003,
            "ZT49_D":-3.5,
            "ZTLA_D":0.0,
            "ZTNAC_D":0.0,
            "ZWF36_D":0.0,
            "engine_id":"b8f7e4972c4313a7a80e45d04532a7e549461bc38e137f9987d537bc10373935",
            "id":192083,
            "flight_datetime":"2022-06-2609:02:00",
            "flight_phase":"FlightPhase.TAKEOFF"
         }
      ]
   }
}

@router.post("/predict", response_model=Dict[str, Dict[str, List[MLOutputY]]])
async def create_category(
    input_full: List[MLInputX]
):
    
    final_output = {}

    
    base_models_path = '../splitted_models/'
    end_phase_n1_path = 'by_eng_phase_n1/'
    phase_path = 'by_phase/'
    

    for input in input_full:
        if not input.aircraft_id in final_output:
            final_output[input.aircraft_id] = {}

        if not input.engine_id in final_output[input.aircraft_id]:
            final_output[input.aircraft_id][input.engine_id] = []


        input_for_ml = MLInputXFiltered(**input.dict())

        temp_output = {}


        for predicted_param in MLOutputY().__fields__:

            filename_eng_n1_phase = input.engine_type + '_' + str(input.n1_modifier) + '_' + input.flight_phase + '_' + predicted_param + '.pickle'
            filename_phase =  input.flight_phase + '_' + predicted_param + '.pickle'
            filename_general = 'general_' + predicted_param + '.pickle'

            eng_n1_phase_filters_model_path = base_models_path + end_phase_n1_path + filename_eng_n1_phase
            phase_filters_path = base_models_path + phase_path + filename_phase
            general_model_path = base_models_path + 'general/' + filename_general

            print('general_model_path',general_model_path)


            check_is_exists_eng_n1_phase_filters_model_path = Path(eng_n1_phase_filters_model_path)
            check_is_exists_phase_filters_path = Path(phase_filters_path)
            check_is_exists_general_path = Path(general_model_path)


            parsed = pd.DataFrame(input_for_ml.__dict__, index=[1])
            parsed = parsed.fillna(0)

            # if check_is_exists_eng_n1_phase_filters_model_path.is_file():
                

            #     print('full filters model 4', predicted_param)

                
            #     model = pickle.load(open(eng_n1_phase_filters_model_path, "rb"))
            #     res = model.predict(parsed)
            #     temp_output[predicted_param] = res

            # elif check_is_exists_phase_filters_path.is_file():
            #     print('flight phase model 4', predicted_param)


            #     if input.flight_phase == "TAKEOFF":
            #         pass

            #     elif input.flight_phase == "CRUISE":
            #         pass    


            #     model = pickle.load(open(phase_filters_path, "rb"))
            #     res = model.predict(parsed)
            #     temp_output[predicted_param] = res

            if check_is_exists_general_path.is_file():
                print('general model 4', predicted_param)
                
                
                model = pickle.load(open(general_model_path, "rb"))
                res = model.predict(parsed)
                temp_output[predicted_param] = res



            else:
                
                return JSONResponse(status_code=400, content={'error': 'dataset not found'})

    
        temp_output = MLOutputYFull(**temp_output)

        temp_output.engine_id = input.engine_id
        temp_output.id = input.id
        temp_output.flight_datetime = input.flight_datetime
        temp_output.flight_phase = input.flight_phase

        temp_output = json.loads(temp_output.json())

        final_output[input.aircraft_id][input.engine_id].append(temp_output)

    

    return JSONResponse(status_code=201, content=json.loads(json.dumps(final_output)))
    
    # return JSONResponse(status_code=201, content=json.loads(json.dumps(examl)))
    

    # except:
    #     raise HTTPException(
    #         status_code=400, detail={"Message": "Error"}
    #     )



