import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

import pyrenn as prn

###
#Read Example Data

df = pd.ExcelFile('dataset.xlsx').parse('Sheet6')
#P0 = np.array([df['s1'].values,df['s2'].values,df['s3'].values,df['s4'].values,df['s5'].values,df['s6'].values,df['s7'].values,df['s8'].values,df['s9'].values,df['s10'].values,df['s11'].values,df['s12'].values,df['s13'].values,df['s14'].values,df['s15'].values,df['s16'].values,df['s17'].values,df['s18'].values,df['s19'].values,df['s20'].values,df['s21'].values,df['s22'].values,df['s23'].values,df['s24'].values,df['s25'].values,df['s26'].values,df['s27'].values,df['s28'].values,df['s29'].values,df['s30'].values,df['s31'].values,df['s32'].values,df['s33'].values,df['s34'].values,df['s35'].values,df['s36'].values,df['s37'].values,df['s38'].values,df['s39'].values,df['s40'].values,df['s41'].values,df['s42'].values,df['s43'].values,df['s44'].values,df['s45'].values,df['s46'].values,df['s47'].values,df['s48'].values,df['s49'].values,df['s50'].values])
P = np.array([df['agitation'].values,df['apyrexial'].values,df['ascites'].values,df['asthenia'].values,df['blackout'].values,df['bradycardia'].values,df['breath sounds decreased'].values,df['chest tightness'].values,df['chill'].values,df['consciousness clear'].values,df['cough'].values,df['decreased body weight'].values,df['diarrhea'].values,df['difficulty'].values,df['distress respiratory'].values,df['drowsiness'].values,df['dyspnea'].values,df['facial paresis'].values,df['fatigue'].values,df['feeling hopeless'].values,df['feeling suicidal'].values,df['fever'].values,df['guaiac positive'].values,df['haemorrhage'].values,df['hallucinations auditory'].values,df['hallucinations visual'].values,df['headache'].values,df['hematuria'].values,df['hemodynamically stable'].values,df['homelessness'].values,df['hypokinesia'].values,df['hypotension'].values,df['intoxication'].values,df['irritable mood'].values,df['lesion'].values,df['mass of body structure'].values,df['mental status changes'].values,df['mood depressed'].values,df['nausea'].values,df['orthopnea'].values,df['pain'].values,df['pain abdominal'].values,df['pain chest'].values,df['patient non compliance'].values,df['pleuritic pain'].values,df['prostatism'].values,df['rale'].values,df['shortness of breath'].values,df['sleeplessness'].values,df['sore to touch'].values])
Y = np.array([df['acquired immuno-deficiency syndrome'].values,df['adhesion'].values,df['affect labile'].values,df['Alzheimers disease'].values,df['anemia'].values,df['aphasia'].values,df['asthma'].values,df['biliary calculus'].values,df['bipolar disorder'].values,df['carcinoma prostate'].values,df['cholecystitis'].values,df['chronic alcoholic intoxication'].values,df['chronic kidney failure'].values,df['chronic obstructive airway disease'].values,df['coronary arteriosclerosis'].values,df['decubitus ulcer'].values,df['degenerative polyarthritis'].values,df['deglutition disorder'].values,df['dehydration'].values,df['depressive disorder'].values,df['diverticulosis'].values,df['embolism pulmonary'].values,df['encephalopathy'].values,df['endocarditis'].values,df['epilepsy'].values,df['failure heart'].values,df['failure kidney'].values,df['fibroid tumor'].values,df['gastritis'].values,df['gout'].values,df['hepatitis'].values,df['hernia hiatal'].values,df['hyperbilirubinemia'].values,df['hypercholesterolemia'].values,df['hyperglycemia'].values,df['hypothyroidism'].values,df['ileus'].values,df['incontinence'].values,df['infection urinary tract'].values,df['influenza'].values,df['insufficiency renal'].values,df['lymphoma'].values,df['malignant neoplasm of breast'].values,df['malignant neoplasm of prostate'].values,df['malignant tumor of colon'].values,df['myocardial infarction'].values,df['neoplasm'].values,df['neoplasm metastasis'].values,df['obesity'].values,df['obesity morbid'].values])
#Ptest = np.array([df['CT1'].values,df['CT2'].values,df['CT3'].values,df['CT4'].values,df['CT5'].values,df['CT6'].values,df['CT7'].values,df['CT8'].values,df['CT9'].values,df['CT10'].values,df['CT11'].values,df['CT12'].values,df['CT13'].values,df['CT14'].values,df['CT15'].values,df['CT16'].values])
#Ytest = np.array([df['CT17'].values,df['CT18'].values,df['CT19'].values,df['CT20'].values,df['CT21'].values,df['CT22'].values,df['CT23'].values])

###
#Create and train NN

#create feed forward neural network with 1 input, 2 hidden layers with 
#4 neurons each and 1 output
#the NN has a recurrent connection with delay of 1 timesteps from the output
# to the first layer
#print len(P),len(Y)
net = prn.CreateNN([50,50,50])
net = prn.loadNN('/usr/local/lib/python2.7/site-packages/examples/minor_final.csv')

#Train NN with training data P=input and Y=target
#Set maximum number of iterations k_max to 500
#Set termination condition for Error E_stop to 1e-5
#The Training will stop after 500 iterations or when the Error <=E_stop
net = prn.train_LM(P,Y,net,verbose=True,k_max=50,E_stop=1e-5) 


###
#Calculate outputs of the trained NN for train and test data
#j=0;
#diseases = ['AIDS (acquired immuno-deficiency syndrome)','Adhesion','Affect labile','Alzheimers disease','Anemia','Aphasia','Asthma','Biliary calculus','Bipolar disorder','Carcinoma prostate','Cholecystitis','Chronic alcoholic intoxication','Chronic kidney failure','Chronic obstructive airway disease','Coronary arteriosclerosis','Decubitus ulcer','Degenerative polyarthritis','Deglutition disorder','Dehydration','Depressive disorder','Diverticulosis','Pulmonary Embolism','Encephalopathy','Endocarditis','Epilepsy','Heart Failure','Kidney Failure','Fibroid tumor','Gastritis','Gout','Hepatitis','Hernia hiatal','Hyperbilirubinemia','Hypercholesterolemia','Hyperglycemia','Hypothyroidism','Ileus','Incontinence','Infection urinary tract','Influenza','Insufficiency renal','Lymphoma','Malignant neoplasm of breast','Malignant neoplasm of prostate','Malignant tumor of colon','Myocardial infarction','Neoplasm','Neoplasm Metastasis','Obesity','Obesity Morbid']
y = prn.NNOut(P,net)
print len(P);
#print len(y);
#for i in range(len(y)):
#    print (y[i][0]);

#z=y;
#np.around(y,0,z);

#for i in range(len(z)):
#    print (z[i][0]);
#    if z[i][0]==1:
#        print diseases[i];
        
#for i in range(len(disease_map)): not sure
    #print disease_map
    
#ytest = prn.NNOut(Ptest,net)
#prn.NNOut(P, net[, P0=None, Y0=None])
prn.saveNN(net,'/usr/local/lib/python2.7/site-packages/examples/minor_final.csv')
###
#Plot results
#fig = plt.figure(figsize=(15,10))
#ax0 = fig.add_subplot(221)
#ax1 = fig.add_subplot(222,sharey=ax0)
#ax2 = fig.add_subplot(223)
#ax3 = fig.add_subplot(224,sharey=ax2)
#fs=18

#t = np.arange(0,480.0)/4 #480 timesteps in 15 Minute resolution
#Train Data
#ax0.set_title('Train Data',fontsize=fs)
#ax0.plot(y[0],color='b',lw=2,label='NN Output')
#ax0.plot(Y[0],color='r',marker='None',linestyle=':',lw=3,markersize=8,label='Data')
#ax0.tick_params(labelsize=fs-2)
#ax0.legend(fontsize=fs-2,loc='upper left')
#ax0.grid()
#ax0.set_ylabel('Storage Pressure [bar]',fontsize=fs)
#plt.setp(ax0.get_xticklabels(), visible=False)

#ax2.plot(y[1],color='b',lw=2,label='NN Output')
#ax2.plot(Y[1],color='r',marker='None',linestyle=':',lw=3,markersize=8,label='Train Data')
#ax2.tick_params(labelsize=fs-2)
#ax2.grid()
#ax2.set_xlabel('Time [h]',fontsize=fs)
#ax2.set_ylabel('el. Power [kW]',fontsize=fs)

#Test Data
#ax1.set_title('Test Data',fontsize=fs)
#ax1.plot(ytest[0],color='b',lw=2,label='NN Output')
#ax1.plot(Ytest[0],color='r',marker='None',linestyle=':',lw=3,markersize=8,label='Test Data')
#ax1.tick_params(labelsize=fs-2)
# ax1.legend(fontsize=fs-2,loc='upper left')
#ax1.grid()
#plt.setp(ax1.get_xticklabels(), visible=False)
#plt.setp(ax1.get_yticklabels(), visible=False)

#ax3.plot(ytest[1],color='b',lw=2,label='NN Output')
#ax3.plot(Ytest[1],color='r',marker='None',linestyle=':',lw=3,markersize=8,label='Test Data')
#ax3.tick_params(labelsize=fs-2)
#ax3.grid()
#ax3.set_xlabel('Time [h]',fontsize=fs)
#plt.setp(ax3.get_yticklabels(), visible=False)

#fig.tight_layout()
#plt.show()
