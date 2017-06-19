#!/usr/bin/env python


from __future__ import unicode_literals

import monoseq

from extractor import describe


#ref = 'MAVLWRLSAVCGALGGRALLLRTPVVRPAHISAFLQDRPIPEWCGVQHIHLSPSHHSGSKAASLHWTSERVVSVLLLGLLPAAYLNPCSAMDYSLAAALTLHGHWGLGQVVTDYVHGDALQKAAKAGLLALSALTFAGLCYFNYHDVGICKAVAMLWKL*'
#alt = 'MAVLWRLSAVCGAPTARDRRPSSVASNSSGQTCSYLSISSGPTYPRMVWSAAHTLVTEPPFWLQGCISPLD*'
ref = 'ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA'
alt = 'ATGGCGGCGGTGGTCGCCCTCTCCTTGAGGCGCCGGTTGCCGCACTCTCCTTGAGGCGCCGGTTGCCGGCCACAACCCTTGGCGGA'

#ref = 'ATGATGATCAGATACAGTGTGATACAGGTAGTTAGACAA'
#alt = 'TCCTGGCATCAGTTACTGTGTTGACTCACTCAGTGTTGGGATCACTCACTTTCCCCCTACAGGACTCAGATCTGGGAGGCAATTACCTTCGGAGAAAAACGAATAGGAAAAACTGAAGTGTTACTTTTTTTAAAGCTGCTGAAGTTTGTTGGTTTCTCATTGTTTTTAAGCCTACTGGAGCAATAAAGTTTGAAGAACTTTTACCAGGTTTTTTTTATCGCTGCCTTGATATACACTTTTCAAAATGCTTTGGTGGGAAGAAGTAGAGGACTGTTATGAAAGAGAAGATGTTCAAAAGAAAACATTCACAAAATGGGTAAATGCACAATTTTCTAAGTTTGGGAAGCAGCATATTGAGAACCTCTTCAGTGACCTACAGGATGGGAGGCGCCTCCTAGACCTCCTCGAAGGCCTGACAGGGCAAAAACTGCCAAAAGAAAAAGGATCCACAAGAGTTCATGCCCTGAACAATGTCAACAAGGCACTGCGGGTTTTGCAGAACAATAATGTTGATTTAGTGAATATTGGAAGTACTGACATCGTAGATGGAAATCATAAACTGACTCTTGGTTTGATTTGGAATATAATCCTCCACTGGCAGGTCAAAAATGTAATGAAAAATATCATGGCTGGATTGCAACAAACCAACAGTGAAAAGATTCTCCTGAGCTGGGTCCGACAATCAACTCGTAATTATCCACAGGTTAATGTAATCAACTTCACCACCAGCTGGTCTGATGGCCTGGCTTTGAATGCTCTCATCCATAGTCATAGGCCAGACCTATTTGACTGGAATAGTGTGGTTTGCCAGCAGTCAGCCACACAACGACTGGAACATGCATTCAACATCGCCAGATATCAATTAGGCATAGAGAAACTACTCGATCCTGAAGATGTTGATACCACCTATCCAGATAAGAAGTCCATCTTAATGTACATCACATCACTCTTCCAAGTTTTGCCTCAACAAGTGAGCATTGAAGCCATCCAGGAAGTGGAAATGTTGCCAAGGCCACCTAAAGTGACTAAAGAAGAACATTTTCAGTTACATCATCAAATGCACTATTCTCAACAGATCACGGTCAGTCTAGCACAGGGATATGAGAGAACTTCTTCCCCTAAGCCTCGATTCAAGAGCTATGCCTACACACAGGCTGCTTATGTCACCACCTCTGACCCTACACGGAGCCCATTTCCTTCACAGCATTTGGAAGCTCCTGAAGACAAGTCATTTGGCAGTTCATTGATGGAGAGTGAAGTAAACCTGGACCGTTATCAAACAGCTTTAGAAGAAGTATTATCGTGGCTTCTTTCTGCTGAGGACACATTGCAAGCACAAGGAGAGATTTCTAATGATGTGGAAGTGGTGAAAGACCAGTTTCATACTCATGAGGGGTACATGATGGATTTGACAGCCCATCAGGGCCGGGTTGGTAATATTCTACAATTGGGAAGTAAGCTGATTGGAACAGGAAAATTATCAGAAGATGAAGAAACTGAAGTACAAGAGCAGATGAATCTCCTAAATTCAAGATGGGAATGCCTCAGGGTAGCTAGCATGGAAAAACAAAGCAATTTACATAGAGTTTTAATGGATCTCCAGAATCAGAAACTGAAAGAGTTGAATGACTGGCTAACAAAAACAGAAGAAAGAACAAGGAAAATGGAGGAAGAGCCTCTTGGACCTGATCTTGAAGACCTAAAACGCCAAGTACAACAACATAAGGTGCTTCAAGAAGATCTAGAACAAGAACAAGTCAGGGTCAATTCTCTCACTCACATGGTGGTGGTAGTTGATGAATCTAGTGGAGATCACGCAACTGCTGCTTTGGAAGAACAACTTAAGGTATTGGGAGATCGATGGGCAAACATCTGTAGATGGACAGAAGACCGCTGGGTTCTTTTACAAGACATCCTTCTCAAATGGCAACGTCTTACTGAAGAACAGTGCCTTTTTAGTGCATGGCTTTCAGAAAAAGAAGATGCAGTGAACAAGATTCACACAACTGGCTTTAAAGATCAAAATGAAATGTTATCAAGTCTTCAAAAACTGGCCGTTTTAAAAGCGGATCTAGAAAAGAAAAAGCAATCCATGGGCAAACTGTATTCACTCAAACAAGATCTTCTTTCAACACTGAAGAATAAGTCAGTGACCCAGAAGACGGAAGCATGGCTGGATAACTTTGCCCGGTGTTGGGATAATTTAGTCCAAAAACTTGAAAAGAGTACAGCACAGATTTCACAGGCTGTCACCACCACTCAGCCATCACTAACACAGACAACTGTAATGGAAACAGTAACTACGGTGACCACAAGGGAACAGATCCTGGTAAAGCATGCTCAAGAGGAACTTCCACCACCACCTCCCCAAAAGAAGAGGCAGATTACTGTGGATTCTGAAATTAGGAAAAGGTTGGATGTTGATATAACTGAACTTCACAGCTGGATTACTCGCTCAGAAGCTGTGTTGCAGAGTCCTGAATTTGCAATCTTTCGGAAGGAAGGCAACTTCTCAGACTTAAAAGAAAAAGTCAATGCCATAGAGCGAGAAAAAGCTGAGAAGTTCAGAAAACTGCAAGATGCCAGCAGATCAGCTCAGGCCCTGGTGGAACAGATGGTGAATGAGGGTGTTAATGCAGATAGCATCAAACAAGCCTCAGAACAACTGAACAGCCGGTGGATCGAATTCTGCCAGTTGCTAAGTGAGAGACTTAACTGGCTGGAGTATCAGAACAACATCATCGCTTTCTATAATCAGCTACAACAATTGGAGCAGATGACAACTACTGCTGAAAACTGGTTGAAAATCCAACCCACCACCCCATCAGAGCCAACAGCAATTAAAAGTCAGTTAAAAATTTGTAAGGATGAAGTCAACCGGCTATCAGGTCTTCAACCTCAAATTGAACGATTAAAAATTCAAAGCATAGCCCTGAAAGAGAAAGGACAAGGACCCATGTTCCTGGATGCAGACTTTGTGGCCTTTACAAATCATTTTAAGCAAGTCTTTTCTGATGTGCAGGCCAGAGAGAAAGAGCTACAGACAATTTTTGACACTTTGCCACCAATGCGCTATCAGGAGACCATGAGTGCCATCAGGACATGGGTCCAGCAGTCAGAAACCAAACTCTCCATACCTCAACTTAGTGTCACCGACTATGAAATCATGGAGCAGAGACTCGGGGAATTGCAGGCTTTACAAAGTTCTCTGCAAGAGCAACAAAGTGGCCTATACTATCTCAGCACCACTGTGAAAGAGATGTCGAAGAAAGCGCCCTCTGAAATTAGCCGGAAATATCAATCAGAATTTGAAGAAATTGAGGGACGCTGGAAGAAGCTCTCCTCCCAGCTGGTTGAGCATTGTCAAAAGCTAGAGGAGCAAATGAATAAACTCCGAAAAATTCAGAATCACATACAAACCCTGAAGAAATGGATGGCTGAAGTTGATGTTTTTCTGAAGGAGGAATGGCCTGCCCTTGGGGATTCAGAAATTCTAAAAAAGCAGCTGAAACAGTGCAGACTTTTAGTCAGTGATATTCAGACAATTCAGCCCAGTCTAAACAGTGTCAATGAAGGTGGGCAGAAGATAAAGAATGAAGCAGAGCCAGAGTTTGCTTCGAGACTTGAGACAGAACTCAAAGAACTTAACACTCAGTGGGATCACATGTGCCAACAGGTCTATGCCAGAAAGGAGGCCTTGAAGGGAGGTTTGGAGAAAACTGTAAGCCTCCAGAAAGATCTATCAGAGATGCACGAATGGATGACACAAGCTGAAGAAGAGTATCTTGAGAGAGATTTTGAATATAAAACTCCAGATGAATTACAGAAAGCAGTTGAAGAGATGAAGAGAGCTAAAGAAGAGGCCCAACAAAAAGAAGCGAAAGTGAAACTCCTTACTGAGTCTGTAAATAGTGTCATAGCTCAAGCTCCACCTGTAGCACAAGAGGCCTTAAAAAAGGAACTTGAAACTCTAACCACCAACTACCAGTGGCTCTGCACTAGGCTGAATGGGAAATGCAAGACTTTGGAAGAAGTTTGGGCATGTTGGCATGAGTTATTGTCATACTTGGAGAAAGCAAACAAGTGGCTAAATGAAGTAGAATTTAAACTTAAAACCACTGAAAACATTCCTGGCGGAGCTGAGGAAATCTCTGAGGTGCTAGATTCACTTGAAAATTTGATGCGACATTCAGAGGATAACCCAAATCAGATTCGCATATTGGCACAGACCCTAACAGATGGCGGAGTCATGGATGAGCTAATCAATGAGGAACTTGAGACATTTAATTCTCGTTGGAGGGAACTACATGAAGAGGCTGTAAGGAGGCAAAAGTTGCTTGAACAGAGCATCCAGTCTGCCCAGGAGACTGAAAAATCCTTACACTTAATCCAGGAGTCCCTCACATTCATTGACAAGCAGTTGGCAGCTTATATTGCAGACAAGGTGGACGCAGCTCAAATGCCTCAGGAAGCCCAGAAAATCCAATCTGATTTGACAAGTCATGAGATCAGTTTAGAAGAAATGAAGAAACATAATCAGGGGAAGGAGGCTGCCCAAAGAGTCCTGTCTCAGATTGATGTTGCACAGAAAAAATTACAAGATGTCTCCATGAAGTTTCGATTATTCCAGAAACCAGCCAATTTTGAGCAGCGTCTACAAGAAAGTAAGATGATTTTAGATGAAGTGAAGATGCACTTGCCTGCATTGGAAACAAAGAGTGTGGAACAGGAAGTAGTACAGTCACAGCTAAATCATTGTGTGAACTTGTATAAAAGTCTGAGTGAAGTGAAGTCTGAAGTGGAAATGGTGATAAAGACTGGACGTCAGATTGTACAGAAAAAGCAGACGGAAAATCCCAAAGAACTTGATGAAAGAGTAACAGCTTTGAAATTGCATTATAATGAGCTGGGAGCAAAGGTAACAGAAAGAAAGCAACAGTTGGAGAAATGCTTGAAATTGTCCCGTAAGATGCGAAAGGAAATGAATGTCTTGACAGAATGGCTGGCAGCTACAGATATGGAATTGACAAAGAGATCAGCAGTTGAAGGAATGCCTAGTAATTTGGATTCTGAAGTTGCCTGGGGAAAGGCTACTCAAAAAGAGATTGAGAAACAGAAGGTGCACCTGAAGAGTATCACAGAGGTAGGAGAGGCCTTGAAAACAGTTTTGGGCAAGAAGGAGACGTTGGTGGAAGATAAACTCAGTCTTCTGAATAGTAACTGGATAGCTGTCACCTCCCGAGCAGAAGAGTGGTTAAATCTTTTGTTGGAATACCAGAAACACATGGAAACTTTTGACCAGAATGTGGACCACATCACAAAGTGGATCATTCAGGCTGACACACTTTTGGATGAATCAGAGAAAAAGAAACCCCAGCAAAAAGAAGACGTGCTTAAGCGTTTAAAGGCAGAACTGAATGACATACGCCCAAAGGTGGACTCTACACGTGACCAAGCAGCAAACTTGATGGCAAACCGCGGTGACCACTGCAGGAAATTAGTAGAGCCCCAAATCTCAGAGCTCAACCATCGATTTGCAGCCATTTCACACAGAATTAAGACTGGAAAGGCCTCCATTCCTTTGAAGGAATTGGAGCAGTTTAACTCAGATATACAAAAATTGCTTGAACCACTGGAGGCTGAAATTCAGCAGGGGGTGAATCTGAAAGAGGAAGACTTCAATAAAGATATGAATGAAGACAATGAGGGTACTGTAAAAGAATTGTTGCAAAGAGGAGACAACTTACAACAAAGAATCACAGATGAGAGAAAGCGAGAGGAAATAAAGATAAAACAGCAGCTGTTACAGACAAAACATAATGCTCTCAAGGATTTGAGGTCTCAAAGAAGAAAAAAGGCTCTAGAAATTTCTCATCAGTGGTATCAGTACAAGAGGCAGGCTGATGATCTCCTGAAATGCTTGGATGACATTGAAAAAAAATTAGCCAGCCTACCTGAGCCCAGAGATGAAAGGAAAATAAAGGAAATTGATCGGGAATTGCAGAAGAAGAAAGAGGAGCTGAATGCAGTGCGTAGGCAAGCTGAGGGCTTGTCTGAGGATGGGGCCGCAATGGCAGTGGAGCCAACTCAGATCCAGCTCAGCAAGCGCTGGCGGGAAATTGAGAGCAAATTTGCTCAGTTTCGAAGACTCAACTTTGCACAAATTCACACTGTCCGTGAAGAAACGATGATGGTGATGACTGAAGACATGCCTTTGGAAATTTCTTATGTGCCTTCTACTTATTTGACTGAAATCACTCATGTCTCACAAGCCCTATTAGAAGTGGAACAACTTCTCAATGCTCCTGACCTCTGTGCTAAGGACTTTGAAGATCTCTTTAAGCAAGAGGAGTCTCTGAAGAATATAAAAGATAGTCTACAACAAAGCTCAGGTCGGATTGACATTATTCATAGCAAGAAGACAGCAGCATTGCAAAGTGCAACGCCTGTGGAAAGGGTGAAGCTACAGGAAGCTCTCTCCCAGCTTGATTTCCAATGGGAAAAAGTTAACAAAATGTACAAGGACCGACAAGGGCGATTTGACAGATCTGTTGAGAAATGGCGGCGTTTTCATTATGATATAAAGATATTTAATCAGTGGCTAACAGAAGCTGAACAGTTTCTCAGAAAGACACAAATTCCTGAGAATTGGGAACATGCTAAATACAAATGGTATCTTAAGGAACTCCAGGATGGCATTGGGCAGCGGCAAACTGTTGTCAGAACATTGAATGCAACTGGGGAAGAAATAATTCAGCAATCCTCAAAAACAGATGCCAGTATTCTACAGGAAAAATTGGGAAGCCTGAATCTGCGGTGGCAGGAGGTCTGCAAACAGCTGTCAGACAGAAAAAAGAGGCTAGAAGAACAAAAGAATATCTTGTCAGAATTTCAAAGAGATTTAAATGAATTTGTTTTATGGTTGGAGGAAGCAGATAACATTGCTAGTATCCCACTTGAACCTGGAAAAGAGCAGCAACTAAAAGAAAAGCTTGAGCAAGTCAAGTTACTGGTGGAAGAGTTGCCCCTGCGCCAGGGAATTCTCAAACAATTAAATGAAACTGGAGGACCCGTGCTTGTAAGTGCTCCCATAAGCCCAGAAGAGCAAGATAAACTTGAAAATAAGCTCAAGCAGACAAATCTCCAGTGGATAAAGGTTTCCAGAGCTTTACCTGAGAAACAAGGAGAAATTGAAGCTCAAATAAAAGACCTTGGGCAGCTTGAAAAAAAGCTTGAAGACCTTGAAGAGCAGTTAAATCATCTGCTGCTGTGGTTATCTCCTATTAGGAATCAGTTGGAAATTTATAACCAACCAAACCAAGAAGGACCATTTGACGTTCAGGAAACTGAAATAGCAGTTCAAGCTAAACAACCGGATGTGGAAGAGATTTTGTCTAAAGGGCAGCATTTGTACAAGGAAAAACCAGCCACTCAGCCAGTGAAGAGGAAGTTAGAAGATCTGAGCTCTGAGTGGAAGGCGGTAAACCGTTTACTTCAAGAGCTGAGGGCAAAGCAGCCTGACCTAGCTCCTGGACTGACCACTATTGGAGCCTCTCCTACTCAGACTGTTACTCTGGTGACACAACCTGTGGTTACTAAGGAAACTGCCATCTCCAAACTAGAAATGCCATCTTCCTTGATGTTGGAGGTACCTGCTCTGGCAGATTTCAACCGGGCTTGGACAGAACTTACCGACTGGCTTTCTCTGCTTGATCAAGTTATAAAATCACAGAGGGTGATGGTGGGTGACCTTGAGGATATCAACGAGATGATCATCAAGCAGAAGGCAACAATGCAGGATTTGGAACAGAGGCGTCCCCAGTTGGAAGAACTCATTACCGCTGCCCAAAATTTGAAAAACAAGACCAGCAATCAAGAGGCTAGAACAATCATTACGGATCGAATTGAAAGAATTCAGAATCAGTGGGATGAAGTACAAGAACACCTTCAGAACCGGAGGCAACAGTTGAATGAAATGTTAAAGGATTCAACACAATGGCTGGAAGCTAAGGAAGAAGCTGAGCAGGTCTTAGGACAGGCCAGAGCCAAGCTTGAGTCATGGAAGGAGGGTCCCTATACAGTAGATGCAATCCAAAAGAAAATCACAGAAACCAAGCAGTTGGCCAAAGACCTCCGCCAGTGGCAGACAAATGTAGATGTGGCAAATGACTTGGCCCTGAAACTTCTCCGGGATTATTCTGCAGATGATACCAGAAAAGTCCACATGATAACAGAGAATATCAATGCCTCTTGGAGAAGCATTCATAAAAGGGTGAGTGAGCGAGAGGCTGCTTTGGAAGAAACTCATAGATTACTGCAACAGTTCCCCCTGGACCTGGAAAAGTTTCTTGCCTGGCTTACAGAAGCTGAAACAACTGCCAATGTCCTACAGGATGCTACCCGTAAGGAAAGGCTCCTAGAAGACTCCAAGGGAGTAAAAGAGCTGATGAAACAATGGCAAGACCTCCAAGGTGAAATTGAAGCTCACACAGATGTTTATCACAACCTGGATGAAAACAGCCAAAAAATCCTGAGATCCCTGGAAGGTTCCGATGATGCAGTCCTGTTACAAAGACGTTTGGATAACATGAACTTCAAGTGGAGTGAACTTCGGAAAAAGTCTCTCAACATTAGGTCCCATTTGGAAGCCAGTTCTGACCAGTGGAAGCGTCTGCACCTTTCTCTGCAGGAACTTCTGGTGTGGCTACAGCTGAAAGATGATGAATTAAGCCGGCAGGCACCTATTGGAGGCGACTTTCCAGCAGTTCAGAAGCAGAACGATGTACATAGGGCCTTCAAGAGGGAATTGAAAACTAAAGAACCTGTAATCATGAGTACTCTTGAGACTGTACGAATATTTCTGACAGAGCAGCCTTTGGAAGGACTAGAGAAACTCTACCAGGAGCCCAGAGAGCTGCCTCCTGAGGAGAGAGCCCAGAATGTCACTCGGCTTCTACGAAAGCAGGCTGAGGAGGTCAATACTGAGTGGGAAAAATTGAACCTGCACTCCGCTGACTGGCAGAGAAAAATAGATGAGACCCTTGAAAGACTCCAGGAACTTCAAGAGGCCACGGATGAGCTGGACCTCAAGCTGCGCCAAGCTGAGGTGATCAAGGGATCCTGGCAGCCCGTGGGCGATCTCCTCATTGACTCTCTCCAAGATCACCTCGAGAAAGTCAAGGCACTTCGAGGAGAAATTGCGCCTCTGAAAGAGAACGTGAGCCACGTCAATGACCTTGCTCGCCAGCTTACCACTTTGGGCATTCAGCTCTCACCGTATAACCTCAGCACTCTGGAAGACCTGAACACCAGATGGAAGCTTCTGCAGGTGGCCGTCGAGGACCGAGTCAGGCAGCTGCATGAAGCCCACAGGGACTTTGGTCCAGCATCTCAGCACTTTCTTTCCACGTCTGTCCAGGGTCCCTGGGAGAGAGCCATCTCGCCAAACAAAGTGCCCTACTATATCAACCACGAGACTCAAACAACTTGCTGGGACCATCCCAAAATGACAGAGCTCTACCAGTCTTTAGCTGACCTGAATAATGTCAGATTCTCAGCTTATAGGACTGCCATGAAACTCCGAAGACTGCAGAAGGCCCTTTGCTTGGATCTCTTGAGCCTGTCAGCTGCATGTGATGCCTTGGACCAGCACAACCTCAAGCAAAATGACCAGCCCATGGATATCCTGCAGATTATTAATTGTTTGACCACTATTTATGACCGCCTGGAGCAAGAGCACAACAATTTGGTCAACGTCCCTCTCTGCGTGGATATGTGTCTGAACTGGCTGCTGAATGTTTATGATACGGGACGAACAGGGAGGATCCGTGTCCTGTCTTTTAAAACTGGCATCATTTCCCTGTGTAAAGCACATTTGGAAGACAAGTACAGATACCTTTTCAAGCAAGTGGCAAGTTCAACAGGATTTTGTGACCAGCGCAGGCTGGGCCTCCTTCTGCATGATTCTATCCAAATTCCAAGACAGTTGGGTGAAGTTGCATCCTTTGGGGGCAGTAACATTGAGCCAAGTGTCCGGAGCTGCTTCCAATTTGCTAATAATAAGCCAGAGATCGAAGCGGCCCTCTTCCTAGACTGGATGAGACTGGAACCCCAGTCCATGGTGTGGCTGCCCGTCCTGCACAGAGTGGCTGCTGCAGAAACTGCCAAGCATCAGGCCAAATGTAACATCTGCAAAGAGTGTCCAATCATTGGATTCAGGTACAGGAGTCTAAAGCACTTTAATTATGACATCTGCCAAAGCTGCTTTTTTTCTGGTCGAGTTGCAAAAGGCCATAAAATGCACTATCCCATGGTGGAATATTGCACTCCGACTACATCAGGAGAAGATGTTCGAGACTTTGCCAAGGTACTAAAAAACAAATTTCGAACCAAAAGGTATTTTGCGAAGCATCCCCGAATGGGCTACCTGCCAGTGCAGACTGTCTTAGAGGGGGACAACATGGAAACTCCCGTTACTCTGATCAACTTCTGGCCAGTAGATTCTGCGCCTGCCTCGTCCCCTCAGCTTTCACACGATGATACTCATTCACGCATTGAACATTATGCTAGCAGGCTAGCAGAAATGGAAAACAGCAATGGATCTTATCTAAATGATAGCATCTCTCCTAATGAGAGCATAGATGATGAACATTTGTTAATCCAGCATTACTGCCAAAGTTTGAACCAGGACTCCCCCCTGAGCCAGCCTCGTAGTCCTGCCCAGATCTTGATTTCCTTAGAGAGTGAGGAAAGAGGGGAGCTAGAGAGAATCCTAGCAGATCTTGAGGAAGAAAACAGGAATCTGCAAGCAGAATATGACCGTCTAAAGCAGCAGCACGAACATAAAGGCCTGTCCCCACTGCCGTCCCCTCCTGAAATGATGCCCACCTCTCCCCAGAGTCCCCGGGATGCTGAGCTCATTGCTGAGGCCAAGCTACTGCGTCAACACAAAGGCCGCCTGGAAGCCAGGATGCAAATCCTGGAAGACCACAATAAACAGCTGGAGTCACAGTTACACAGGCTAAGGCAGCTGCTGGAGCAACCCCAGGCAGAGGCCAAAGTGAATGGCACAACGGTGTCCTCTCCTTCTACCTCTCTACAGAGGTCCGACAGCAGTCAGCCTATGCTGCTCCGAGTGGTTGGCAGTCAAACTTCGGACTCCATGGGTGAGGAAGATCTTCTCAGTCCTCCCCAGGACACAAGCACAGGGTTAGAGGAGGTGATGGAGCAACTCAACAACTCCTTCCCTAGTTCAAGAGGAAGAAATACCCCTGGAAAGCCAATGAGAGAGGACACAATGTAGGAAGTCTTTTCCACATGGCAGATGATTTGGGCAGAGCGATGGAGTCCTTAGTATCAGTCATGACAGATGAAGAAGGAGCAGAATAAATGTTTTACAACTCCTGATTCCCGCATGGTTTTTATAATATTCATACAACAAAGAGGATTAGACAGTAAGAGTTTACAAGAAATAAATCTATATTTTTGTGAAGGGTAGTGGTATTATACTGTAGATTTCAGTAGTTTCTAAGTCTGTTATTGTTTTGTTAACAATGGCAGGTTTTACACGTCTATGCAATTGTACAAAAAAGTTATAAGAAAACTACATGTAAAATCTTGATAGCTAAATAACTTGCCATTTCTTTATATGGAACGCATTTTGGGTTGTTTAAAAATTTATAACAGTTATAAAGAAAGATTGTAAACTAAAGTGTGCTTTATAAAAAAAAGTTGTTTATAAAAACCCCTAAAAACAAAACAAACACACACACACACACATACACACACACACACAAAACTTTGAGGCAGCGCATTGTTTTGCATCCTTTTGGCGTGATATCCATATGAAATTCATGGCTTTTTCTTTTTTTGCATATTAAAGATAAGACTTCCTCTACCACCACACCAAATGACTACTACACACTGCTCATTTGAGAACTGTCAGCTGAGTGGGGCAGGCTTGAGTTTTCATTTCATATATCTATATGTCTATAAGTATATAAATACTATAGTTATATAGATAAAGAGATACGAATTTCTATAGACTGACTTTTTCCATTTTTTAAATGTTCATGTCACATCCTAATAGAAAGAAATTACTTCTAGTCAGTCATCCAGGCTTACCTGCTTGGTCTAGAATGGATTTTTCCCGGAGCCGGAAGCCAGGAGGAAACTACACCACACTAAAACATTGTCTACAGCTCCAGATGTTTCTCATTTTAAACAACTTTCCACTGACAACGAAAGTAAAGTAAAGTATTGGATTTTTTTAAAGGGAACATGTGAATGAATACACAGGACTTATTATATCAGAGTGAGTAATCGGTTGGTTGGTTGATTGATTGATTGATTGATACATTCAGCTTCCTGCTGCTAGCAATGCCACGATTTAGATTTAATGATGCTTCAGTGGAAATCAATCAGAAGGTATTCTGACCTTGTGAACATCAGAAGGTATTTTTTAACTCCCAAGCAGTAGCAGGACGATGATAGGGCTGGAGGGCTATGGATTCCCAGCCCATCCCTGTGAAGGAGTAGGCCACTCTTTAAGTGAAGGATTGGATGATTGTTCATAATACATAAAGTTCTCTGTAATTACAACTAAATTATTATGCCCTCTTCTCACAGTCAAAAGGAACTGGGTGGTTTGGTTTTTGTTGCTTTTTTAGATTTATTGTCCCATGTGGGATGAGTTTTTAAATGCCACAAGACATAATTTAAAATAAATAAACTTTGGGAAAAGGTGTAAAACAGTAGCCCCATCACATTTGTGATACTGACAGGTATCAACCCAGAAGCCCATGAACTGTGTTTCCATCCTTTGCATTTCTCTGCGAGTAGTTCCACACAGGTTTGTAAGTAAGTAAGAAAGAAGGCAAATTGATTCAAATGTTACAAAAAAACCCTTCTTGGTGGATTAGACAGGTTAAATATATAAACAAACAAACAAAAATTGCTCAAAAAAGAGGAGAAAAGCTCAAGAGGAAAAGCTAAGGACTGGTAGGAAAAAGCTTTACTCTTTCATGCCATTTTATTTCTTTTTGATTTTTAAATCATTCATTCAATAGATACCACCGTGTGACCTATAATTTTGCAAATCTGTTACCTCTGACATCAAGTGTAATTAGCTTTTGGAGAGTGGGCTGACATCAAGTGTAATTAGCTTTTGGAGAGTGGGTTTTGTCCATTATTAATAATTAATTAATTAACATCAAACACGGCTTCTCATGCTATTTCTACCTCACTTTGGTTTTGGGGTGTTCCTGATAATTGTGCACACCTGAGTTCACAGCTTCACCACTTGTCCATTGCGTTATTTTCTTTTTCCTTTATAATTCTTTCTTTTTCCTTCATAATTTTCAAAAGAAAACCCAAAGCTCTAAGGTAACAAATTACCAAATTACATGAAGATTTGGTTTTTGTCTTGCATTTTTTTCCTTTATGTGACGCTGGACCTTTTCTTTACCCAAGGATTTTTAAAACTCAGATTTAAAACAAGGGGTTACTTTACATCCTACTAAGAAGTTTAAGTAAGTAAGTTTCATTCTAAAATCAGAGGTAAATAGAGTGCATAAATAATTTTGTTTTAATCTTTTTGTTTTTCTTTTAGACACATTAGCTCTGGAGTGAGTCTGTCATAATATTTGAACAAAAATTGAGAGCTTTATTGCTGCATTTTAAGCATAATTAATTTGGACATTATTTCGTGTTGTGTTCTTTATAACCACCAAGTATTAAACTGTAAATCATAATGTAACTGAAGCATAAACATCACATGGCATGTTTTGTCATTGTTTTCAGGTACTGAGTTCTTACTTGAGTATCATAATATATTGTGTTTTAACACCAACACTGTAACATTTACGAATTATTTTTTTAAACTTCAGTTTTACTGCATTTTCACAACATATCAGACTTCACCAAATATATGCCTTACTATTGTATTATAGTACTGCTTTACTGTGTATCTCAATAAAGCACGCAGTTATGTTAC'
#ref = 'PAAYLNPCSAMDYSLAAALTLHGHWGLGQVVTDYVHGDALQKAAKAGLLALSALTFAGLCYFNYHDVGICKAVAMLWKL*'
#alt = 'PAAYLNPCSAMTIPWLQPSLFMVTGALDKLLLTMFMGMPCRKLPRQGFWHFQL*'

#ref = 'KGFRLLNPHPKPNPKNN*'
#alt = 'KGFRLLNPHPSQTPKTTDIITQEIFATLVFFQHQQLLLNCQTQLAIYIETSVLKDL*'

description = describe.describe_dna(ref, alt)

ref_annotation = []
alt_annotation = []
#for rv in description:
#    for i in rv.annotated_inserted:
#        ref_annotation.append([(i.start - 1, i.end)])
#        alt_annotation.append([(i.sample_start - 1, i.sample_end)])
#        print '({}, {}), {}, ({}, {})'.format(
#            i.start, i.end, rv.start, i.sample_start, i.sample_end)

print '    p.{}'.format(description)
#print '    q.{}'.format(description.nhgvs())

#print
#print monoseq.pprint_sequence(ref, ref_annotation, format=monoseq.AnsiFormat)
#print
#print monoseq.pprint_sequence(alt, alt_annotation, format=monoseq.AnsiFormat)
#print
