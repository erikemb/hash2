from hashlib import sha256
import numpy as np
import numpy

maior = 0

tables = []

table_tmp = {}
table_tmp[1024] = 233
table_tmp[1616] = 397
table_tmp[592] = 261
table_tmp[576] = 279
table_tmp[64] = 285
table_tmp[528] = 137
table_tmp[512] = 348
table_tmp[1600] = 153
table_tmp[1088] = 667
table_tmp[80] = 23
table_tmp[1104] = 448
table_tmp[4672] = 74
table_tmp[580] = 755
table_tmp[624] = 435
table_tmp[112] = 401
table_tmp[16] = 728
table_tmp[4160] = 295
table_tmp[1552] = 448
table_tmp[560] = 609
table_tmp[0] = 439
table_tmp[96] = 80
table_tmp[48] = 186
table_tmp[4096] = 71
table_tmp[2] = 973
table_tmp[4162] = 133
table_tmp[4608] = 178
table_tmp[832] = 103
table_tmp[320] = 351
table_tmp[578] = 510
table_tmp[4928] = 875
table_tmp[4674] = 761
table_tmp[768] = 192
table_tmp[66] = 566
table_tmp[1040] = 40
table_tmp[1536] = 640
table_tmp[33792] = 424
table_tmp[1664] = 179
table_tmp[32768] = 985
table_tmp[128] = 848
table_tmp[32] = 174
table_tmp[32896] = 673
table_tmp[608] = 594
table_tmp[516] = 667
table_tmp[192] = 622
table_tmp[4] = 906
table_tmp[544] = 886
table_tmp[514] = 325
table_tmp[32772] = 1023
table_tmp[33280] = 642
table_tmp[1028] = 583
table_tmp[32900] = 474
table_tmp[32832] = 674
table_tmp[34816] = 863
table_tmp[2048] = 846
table_tmp[3072] = 693
table_tmp[32960] = 609
tables.append(table_tmp)








table_tmp = {}
table_tmp[576] = 7
table_tmp[64] = 181
table_tmp[33536] = 911
table_tmp[33280] = 923
table_tmp[580] = 59
table_tmp[512] = 60
table_tmp[32768] = 17
table_tmp[33344] = 263
table_tmp[65] = 693
table_tmp[33600] = 399
table_tmp[68] = 476
table_tmp[32832] = 384
table_tmp[581] = 227
table_tmp[33024] = 990
table_tmp[577] = 599
table_tmp[0] = 104
table_tmp[33408] = 803
table_tmp[33472] = 49
table_tmp[33088] = 987
table_tmp[33345] = 691
table_tmp[585] = 982
table_tmp[4621] = 138
table_tmp[4109] = 539
table_tmp[4105] = 412
table_tmp[9] = 456
table_tmp[1] = 551
table_tmp[521] = 76
table_tmp[4101] = 377
table_tmp[4108] = 149
table_tmp[4617] = 623
table_tmp[4104] = 969
table_tmp[4097] = 883
table_tmp[8] = 907
table_tmp[4620] = 403
table_tmp[4677] = 197
table_tmp[4100] = 206
table_tmp[4612] = 196
table_tmp[644] = 482
table_tmp[4165] = 188
table_tmp[137] = 605
table_tmp[4164] = 788
table_tmp[4685] = 174
table_tmp[516] = 708
table_tmp[4740] = 531
table_tmp[4] = 404
table_tmp[4676] = 968
table_tmp[4684] = 689
table_tmp[4228] = 536
table_tmp[73] = 620
table_tmp[640] = 150
table_tmp[4173] = 139
table_tmp[4748] = 1009
table_tmp[4613] = 817
table_tmp[4236] = 165
table_tmp[4749] = 267
table_tmp[649] = 715
table_tmp[4293] = 491
table_tmp[525] = 170
table_tmp[141] = 985
table_tmp[13] = 832
table_tmp[77] = 866
table_tmp[4229] = 267
table_tmp[4237] = 1011
table_tmp[4301] = 27
table_tmp[589] = 500
table_tmp[12] = 681
table_tmp[5] = 585
table_tmp[520] = 313
table_tmp[201] = 810
table_tmp[4172] = 307
table_tmp[4421] = 241
table_tmp[4420] = 819
table_tmp[36941] = 20
table_tmp[36932] = 794
table_tmp[4292] = 682
table_tmp[36940] = 690
table_tmp[69] = 181
table_tmp[4180] = 971
table_tmp[36933] = 470
table_tmp[768] = 287
table_tmp[4933] = 752
table_tmp[4869] = 726
table_tmp[4877] = 887
table_tmp[4357] = 735
table_tmp[513] = 166
table_tmp[320] = 610
table_tmp[832] = 731
table_tmp[4932] = 315
table_tmp[517] = 59
table_tmp[256] = 50
table_tmp[4708] = 912
table_tmp[4709] = 919
table_tmp[37444] = 604
table_tmp[37476] = 245
table_tmp[36868] = 620
table_tmp[4196] = 687
table_tmp[4132] = 475
table_tmp[37445] = 626
table_tmp[32841] = 238
table_tmp[4197] = 395
table_tmp[4133] = 947
table_tmp[37380] = 486
table_tmp[33353] = 762
table_tmp[37453] = 694
table_tmp[100] = 878
table_tmp[128] = 180
table_tmp[132] = 527
table_tmp[4356] = 935
table_tmp[4609] = 675
table_tmp[4365] = 469
table_tmp[4429] = 458
table_tmp[4868] = 968
table_tmp[4941] = 618
tables.append(table_tmp)

table_tmp = {}
table_tmp[5140] = 51
table_tmp[34320] = 929
table_tmp[54804] = 9
table_tmp[50196] = 1003
table_tmp[33812] = 856
table_tmp[21572] = 799
table_tmp[54276] = 450
table_tmp[17408] = 305
table_tmp[4] = 99
table_tmp[37892] = 788
table_tmp[54292] = 97
table_tmp[38548] = 329
table_tmp[33808] = 999
table_tmp[1044] = 817
table_tmp[1040] = 1011
table_tmp[33796] = 571
table_tmp[37908] = 788
table_tmp[21524] = 449
table_tmp[17428] = 219
table_tmp[34324] = 606
table_tmp[21508] = 479
table_tmp[4116] = 141
table_tmp[17412] = 989
table_tmp[18500] = 615
table_tmp[38420] = 395
table_tmp[16384] = 310
table_tmp[1552] = 286
table_tmp[34308] = 855
table_tmp[38404] = 801
table_tmp[20] = 231
table_tmp[50192] = 152
table_tmp[18496] = 723
table_tmp[34452] = 245
table_tmp[23620] = 23
table_tmp[17424] = 219
table_tmp[1028] = 875
table_tmp[16400] = 219
table_tmp[38532] = 217
table_tmp[53268] = 857
table_tmp[16404] = 877
table_tmp[17476] = 143
table_tmp[50708] = 956
table_tmp[54932] = 107
table_tmp[16] = 743
table_tmp[16388] = 846
table_tmp[4740] = 530
table_tmp[640] = 804
table_tmp[1664] = 778
table_tmp[4096] = 604
table_tmp[34432] = 61
table_tmp[4736] = 818
table_tmp[4228] = 519
table_tmp[0] = 179
table_tmp[37508] = 611
table_tmp[4100] = 459
table_tmp[512] = 664
table_tmp[37504] = 306
table_tmp[4224] = 457
table_tmp[33408] = 353
table_tmp[34304] = 166
table_tmp[38528] = 209
table_tmp[128] = 724
table_tmp[5124] = 598
table_tmp[40580] = 37
table_tmp[36868] = 695
table_tmp[36996] = 780
table_tmp[7812] = 638
table_tmp[39940] = 771
table_tmp[38916] = 92
table_tmp[5764] = 902
table_tmp[36884] = 768
table_tmp[36948] = 893
table_tmp[32768] = 185
table_tmp[5252] = 597
table_tmp[38596] = 405
table_tmp[7172] = 964
table_tmp[32772] = 172
table_tmp[37956] = 627
table_tmp[40068] = 499
table_tmp[33792] = 472
table_tmp[36864] = 564
table_tmp[38020] = 433
table_tmp[40644] = 709
table_tmp[7300] = 766
table_tmp[39956] = 14
table_tmp[36932] = 282
table_tmp[1680] = 433
table_tmp[34436] = 760
table_tmp[5780] = 570
table_tmp[34448] = 540
table_tmp[656] = 271
table_tmp[1668] = 475
table_tmp[2708] = 251
table_tmp[644] = 449
table_tmp[33924] = 777
table_tmp[660] = 350
table_tmp[4756] = 538
table_tmp[33920] = 61
table_tmp[1684] = 576
table_tmp[2704] = 991
table_tmp[1536] = 542
table_tmp[37888] = 746
table_tmp[49152] = 691
table_tmp[50208] = 963
table_tmp[20484] = 970
table_tmp[50176] = 94
table_tmp[50320] = 599
table_tmp[50832] = 910
table_tmp[32896] = 843
table_tmp[50304] = 59
table_tmp[32784] = 152
table_tmp[33952] = 375
table_tmp[4612] = 403
table_tmp[33824] = 471
table_tmp[20500] = 656
table_tmp[50816] = 102
table_tmp[34464] = 836
table_tmp[54288] = 541
table_tmp[53264] = 275
table_tmp[49168] = 782
table_tmp[33280] = 591
table_tmp[33412] = 832
table_tmp[37380] = 461
table_tmp[1152] = 741
table_tmp[1024] = 316
table_tmp[5652] = 872
table_tmp[5136] = 95
table_tmp[38036] = 551
table_tmp[37904] = 110
table_tmp[54340] = 474
table_tmp[5760] = 965
table_tmp[5636] = 164
table_tmp[37396] = 610
table_tmp[38422] = 490
table_tmp[5120] = 316
table_tmp[5776] = 91
table_tmp[38534] = 127
table_tmp[54356] = 901
table_tmp[5268] = 426
table_tmp[34336] = 610
table_tmp[33840] = 500
table_tmp[34352] = 143
table_tmp[33825] = 922
table_tmp[50224] = 414
table_tmp[50688] = 397
table_tmp[37920] = 618
table_tmp[16408] = 716
table_tmp[50336] = 852
tables.append(table_tmp)

table_tmp = {}
table_tmp[1152] = 183
table_tmp[17555] = 974
table_tmp[18065] = 127
table_tmp[1664] = 627
table_tmp[1681] = 275
table_tmp[19603] = 234
table_tmp[16401] = 699
table_tmp[16913] = 159
table_tmp[16] = 499
table_tmp[19601] = 494
table_tmp[18064] = 638
table_tmp[1168] = 819
table_tmp[17619] = 954
table_tmp[17553] = 239
table_tmp[34449] = 529
table_tmp[18067] = 438
table_tmp[50833] = 594
table_tmp[1680] = 886
table_tmp[33425] = 158
table_tmp[49809] = 239
table_tmp[17554] = 719
table_tmp[20113] = 830
table_tmp[17041] = 619
table_tmp[34432] = 197
table_tmp[17539] = 345
table_tmp[49681] = 660
table_tmp[1169] = 711
table_tmp[1232] = 442
table_tmp[16897] = 667
table_tmp[17937] = 974
table_tmp[17425] = 895
table_tmp[18131] = 855
table_tmp[34448] = 182
table_tmp[17617] = 950
table_tmp[1745] = 439
table_tmp[0] = 159
table_tmp[17552] = 874
table_tmp[17603] = 635
table_tmp[1235] = 942
table_tmp[25747] = 699
table_tmp[1233] = 307
table_tmp[25745] = 737
table_tmp[8218] = 288
table_tmp[8200] = 851
table_tmp[8] = 840
table_tmp[72] = 680
table_tmp[8264] = 868
table_tmp[8192] = 663
table_tmp[8202] = 425
table_tmp[24] = 434
table_tmp[26] = 835
table_tmp[8216] = 1018
table_tmp[8280] = 54
table_tmp[10] = 715
table_tmp[40984] = 747
table_tmp[8704] = 151
table_tmp[41496] = 750
table_tmp[12376] = 907
table_tmp[41480] = 266
table_tmp[32792] = 226
table_tmp[8712] = 733
table_tmp[8217] = 721
table_tmp[8728] = 630
table_tmp[9369] = 542
table_tmp[9368] = 903
table_tmp[8729] = 346
table_tmp[41472] = 550
table_tmp[520] = 806
table_tmp[8201] = 191
table_tmp[9872] = 852
table_tmp[8856] = 619
table_tmp[41488] = 301
table_tmp[8208] = 636
table_tmp[536] = 52
table_tmp[33304] = 759
table_tmp[32776] = 649
table_tmp[40968] = 165
table_tmp[8720] = 78
table_tmp[33288] = 288
table_tmp[9880] = 775
table_tmp[9881] = 559
table_tmp[9240] = 565
table_tmp[41624] = 767
table_tmp[8344] = 488
table_tmp[9360] = 42
table_tmp[1536] = 474
table_tmp[32768] = 54
table_tmp[1560] = 217
table_tmp[1544] = 364
table_tmp[528] = 760
table_tmp[1024] = 395
table_tmp[512] = 164
table_tmp[34320] = 904
table_tmp[1552] = 588
table_tmp[34312] = 114
table_tmp[33936] = 988
table_tmp[1040] = 617
table_tmp[64] = 708
table_tmp[1672] = 553
table_tmp[33792] = 187
table_tmp[1032] = 63
table_tmp[33808] = 383
table_tmp[34304] = 230
table_tmp[34328] = 310
table_tmp[1048] = 844
table_tmp[1688] = 724
table_tmp[80] = 751
table_tmp[8840] = 379
table_tmp[9864] = 1015
table_tmp[8713] = 462
table_tmp[8328] = 762
table_tmp[1160] = 850
table_tmp[9352] = 686
table_tmp[25736] = 563
table_tmp[9224] = 497
table_tmp[9] = 867
table_tmp[8331] = 735
table_tmp[26248] = 539
table_tmp[9867] = 1023
table_tmp[9353] = 47
table_tmp[9226] = 767
table_tmp[8329] = 602
table_tmp[25737] = 594
table_tmp[1161] = 804
table_tmp[17545] = 799
table_tmp[9736] = 386
table_tmp[1545] = 975
table_tmp[9225] = 432
table_tmp[1673] = 571
table_tmp[136] = 307
table_tmp[648] = 346
table_tmp[26249] = 979
table_tmp[1033] = 476
table_tmp[8193] = 410
table_tmp[8203] = 943
table_tmp[8194] = 124
table_tmp[9355] = 1005
table_tmp[9865] = 827
table_tmp[9227] = 870
table_tmp[1675] = 510
table_tmp[9737] = 987
table_tmp[521] = 999
table_tmp[24600] = 244
table_tmp[16408] = 950
table_tmp[2] = 688
table_tmp[18] = 182
table_tmp[522] = 341
table_tmp[24584] = 551
table_tmp[530] = 531
table_tmp[514] = 354
table_tmp[8714] = 983
table_tmp[33280] = 964
table_tmp[538] = 765
table_tmp[13448] = 963
table_tmp[12352] = 975
table_tmp[13384] = 495
table_tmp[12364] = 989
table_tmp[9344] = 878
table_tmp[9216] = 338
table_tmp[5192] = 997
table_tmp[12288] = 189
table_tmp[76] = 46
table_tmp[12296] = 655
table_tmp[8268] = 562
table_tmp[4168] = 465
table_tmp[5256] = 1003
table_tmp[9856] = 929
table_tmp[4104] = 837
table_tmp[13320] = 267
table_tmp[13312] = 419
table_tmp[12360] = 423
table_tmp[4172] = 86
table_tmp[5128] = 927
table_tmp[9728] = 603
table_tmp[26240] = 251
table_tmp[8320] = 706
table_tmp[8832] = 461
table_tmp[640] = 282
table_tmp[24704] = 415
table_tmp[1665] = 462
table_tmp[18048] = 454
table_tmp[25728] = 216
table_tmp[128] = 418
table_tmp[25216] = 498
table_tmp[18049] = 462
table_tmp[17536] = 715
table_tmp[1696] = 1023
table_tmp[25224] = 286
table_tmp[16536] = 345
table_tmp[25752] = 390
table_tmp[24730] = 428
table_tmp[25240] = 865
table_tmp[24728] = 190
table_tmp[8282] = 954
table_tmp[8346] = 287
table_tmp[25242] = 491
table_tmp[17048] = 402
table_tmp[26264] = 486
table_tmp[24712] = 453
table_tmp[8730] = 817
table_tmp[664] = 371
table_tmp[9857] = 610
table_tmp[42633] = 239
table_tmp[34441] = 871
table_tmp[137] = 867
tables.append(table_tmp)

for d in tables:
    addr = []
    outs = []
    sha=[]  #sha256 da entrada
    shain=[] #parte inicial da sha
    shaout=[] #parte final da sha 

    arm1=[]  #união shain bo shaout

    hash1 = [] 
    hash11 = [] #testador de repetição do hash1
    hash2 = []
    hash22 = [] #testador de repetição do hash2
    hash3 = [] 
    hash33 = [] #testador de repetição do hash3
    hash4= []
    hash44 = [] #testador de repetição do hash4
    n = len(d)
    m = n / 4
    for k in d.keys():
        #print(str(k) + '-> '+ str(d[k]))     
       
        if maior < k :
            maior = k

        addr.append(str(k))        
        outs.append(str(d[k])) 

    n_bits = np.ceil(np.log2(maior))   #calcula numero de bits a serem pegos da hash
    ax = int(np.ceil(n_bits/4))

    sha = [sha256(addr[i].encode()).hexdigest() for i in range(len(addr))]  #armazenando os sha256

    for i in range(len(addr)):
        temp = sha[i]
        shain.append(temp[:ax])    #pega parte inicial da hash
        shaout.append(temp[-ax:])   #pega parte final da hash   

    
    for i in range(0,n,1): #transforma em decimal
        hex_string = str(shain[i])
        shain[i] = int(hex_string, 16)
        hex_string = str(shaout[i])
        shaout[i] = int(hex_string, 16)   
        

    for i in range(0,n,1):
            temp = [shain[i]],[np.int(outs[i])],[shaout[i]]
            arm1.append(temp)

    #parte teste

    for i in range(0,n,1) :
        if (shain[i] not in hash11) and (len(hash1))<m:
            hash11.append(shain[i])  
            hash1.append(arm1[i])
        
    for i in range(0,n,1) :  
        if (arm1[i] not in hash1) and (shain[i] not in hash22) and (len(hash2))<m:
            hash22.append(shain[i])  
            hash2.append(arm1[i])

    for i in range(0,n,1) :  
        if (arm1[i] not in hash1) and (arm1[i] not in hash2) and (shain[i] not in hash33) and (len(hash3))<m:
            hash33.append(shain[i])  
            hash3.append(arm1[i])

    for i in range(0,n,1) :  
        if (arm1[i] not in hash1) and (arm1[i] not in hash2) and (arm1[i] not in hash3) and (shain[i] not in hash44) and (len(hash4))<m:
            hash44.append(shain[i])  
            hash4.append(arm1[i])

    tax = 100 * (len(hash1)+len(hash2)+len(hash3)+len(hash4)) / len(arm1)
    #print(tax,"%")
    print("")
    for i in range(len(arm1)):
        print(arm1[i])
    print("")





