#----Create a list of parameter sets for the Markov model
 
import numpy as np
import os

num_groups = 800		#set the number of output files

parsetlist = []
#-----------------specify parameters---------------------
#The code below creates every possible combination of the parameters specified in each for loop
for DSBcondition in [0.015625/16,0.015625/8,0.015625/4,0.015625/2,0.015625,0.03125,0.0625,0.125,0.25,0.5,1.,2.,4.,8.,16.,32.,64.]: #Specify the levels of damage
	for Kd_G1toG0 in [0.015625/16,0.015625/4,0.015625,0.0625,0.25,1,4,16,64]: #Specify the default values for Kd_G1toG0
		for Kd_G2toG0 in [0.015625/16,0.015625/4,0.015625,0.0625,0.25,1,4,16,64]: #Specify the default values for Kd_G2toG0
			for Kd_G0toS in [0.015625/16,0.015625/4,0.015625,0.0625,0.25,1,4,16,64]: #Specify the default values for Kd_G0toS
				for G1checki in [1]: #Specify the strengths of the G1 checkpoint inhibition. For example, 1 means no increase in the default Kd_G1toG0 and Kd_G0toS values, while 2 represents a twofold increase.
					for G2checki in [1]: #Specify the strengths of the G2 checkpoint inhibition. For example, 1 means no increase in the default Kd_G2toG0 values, while 2 represents a twofold increase.
						for checki in [1]: #Specify the strengths of the general checkpoints inhibition. For example, 1 means no increase in all the Kd values, while 2 represents a twofold increase. 
							for t_G1toG0 in [24]: #Specify the speed of the G1 checkpoint, based on Jeggo's paper. 
								for t_G2toG0 in [1]: #Specify the speed of the G2 checkpoint, based on Jeggo's paper
									parsetlist.append([DSBcondition,Kd_G1toG0,Kd_G2toG0,Kd_G0toS,G1checki,G2checki,checki,t_G1toG0,t_G2toG0])

directory = "Parameterscan_default" #Specify the directory's name in which the parameter list files will be stored
parent_dir = "./" #Specify the parent directory
path = os.path.join(parent_dir,directory)
os.mkdir(path)

#--------------------------------------------------------

for group in range(0,num_groups):
	outname = parent_dir + directory + "/"+"parameterset_" + str(group)+".txt"
	fileout = open(outname,"w")
	fileout.write("DSBcondition\tKd_G1toG0\tKd_G2toG0\tKd_G0toS\tG1check_inhibition\tG2check_inhibition\tcheck_inhibition\tt_G1toG0\tt_G2toG0\n")
	fileout.flush()
	fileout.close()
	
for parset_num in range(0,len(parsetlist)):

	DSBcondition = str(parsetlist[parset_num][0])
	Kd_G1toG0 = str(parsetlist[parset_num][1])
	Kd_G2toG0 = str(parsetlist[parset_num][2])
	Kd_G0toS = str(parsetlist[parset_num][3])
	G1checki = str(parsetlist[parset_num][4]) 
	G2checki = str(parsetlist[parset_num][5])
	checki = str(parsetlist[parset_num][6])
	t_G1toG0 = str(parsetlist[parset_num][7])
	t_G2toG0 = str(parsetlist[parset_num][8])

	group = parset_num%num_groups
	outname = parent_dir + directory + "/"+"parameterset_" + str(group)+".txt"
	fileout = open(outname,"a")
	fileout.write(DSBcondition+"\t"+Kd_G1toG0+"\t"+Kd_G2toG0+"\t"+Kd_G0toS+"\t"+G1checki+"\t"+G2checki+"\t"+checki+"\t"+t_G1toG0+"\t"+t_G2toG0+"\n")
			
	

		
					
					
					
