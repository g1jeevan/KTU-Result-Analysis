import PyPDF2
import os
import copy
import re
import psycopg2
import sys


#++++++++++ From DataBase +++++++
#-------Helper
#nextval('your_sequence_name'::regclass)
#nextval('idincrement'::regclass)

def doit():
 os.chdir('c:\\pypro')
 collegename='AJC'
 #----------- Establishing DataBase Connection

 #cur.execute("SELECT * FROM Products")
   #while True:
    #row = cur.fetchone()
    #if row == None:
     #break
    #print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))
 
 
 conn = None
 
 try:
   conn = psycopg2.connect(database="mcatest", user = "postgres", password = "amma", host = "127.0.0.1", port = "5432")
   cur=conn.cursor()

   collegename='TKM'
   print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
   print('++++++ MCA S3 Result analysis - TKM college of ENGINEERING ++++++')
   print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
   print('')
   print('')
   
   cur.execute("SELECT count(*) FROM public.s3result where college='"+collegename+"'");
   k = cur.fetchone()
   lentotal=int(k[0])
   print("Total appeared : " +str(lentotal))

   cur.execute("SELECT count(*) FROM public.s3result where college='"+collegename+"' and \
   (rlmca201 ='F' or rlmca203 ='F' or rlmca205 ='F' or \
   rlmca207 ='F' or rlmca209 ='F' or rlmca231 ='F' or rlmca233 ='F')");
   k = cur.fetchone()
   lentotalfail=int(k[0])
   print("Total Pass  : " +str(lentotal-lentotalfail))
   print("Total Fail  : " +str(lentotalfail))

   cur.execute("select count(*) from s3result where college='"+collegename+"' \
   and (rlmca201 ='FE' or rlmca203 ='FE' or rlmca205 ='FE' or \
   rlmca207 ='FE' or rlmca209 ='FE' or rlmca231 ='FE' or rlmca233 ='FE' \
   or rlmca201 ='NA' or rlmca203 ='NA' or rlmca205 ='NA' or rlmca207 ='NA'\
   or rlmca209 ='NA' or rlmca231 ='NA' or rlmca233 ='NA')");
   k = cur.fetchone()
   lentotalnafe=int(k[0])
   print("Total FE and Not Available  : " +str(lentotalnafe))

   a1=abs(lentotal-lentotalfail)
   a1=a1/lentotal
   a1=a1*100
   print('Pass % with all students details on the report : '+str(a1))
   a=abs(lentotal-lentotalfail-lentotalnafe)
   a=a/(lentotal-lentotalnafe)
   a=a*100
   print('Pass % without FE and NA students on the report : '+str(a))

 
   ###################################################################
   
   print('')
   print('********** Subject Wise  List **********')
   print('')
   print('******  RLMCA201 - COMPUTER NETWORKS  ******  ')
   print('')
   
   print("Total appeared : " +str(lentotal))
   cur.execute("SELECT count(*) FROM s3result where \
   college='"+collegename+"' and rlmca201='F'")
   k = cur.fetchone()
   rlmca201fail=int(k[0])
   print("Total Pass  : " +str(lentotal-rlmca201fail))
   print("Total Fail  : " +str(rlmca201fail))
   a1=abs(lentotal-rlmca201fail)
   a1=a1/lentotal
   a1=a1*100
   print('Pass % of COMPUTER NETWORKS : '+str(a1))
   print('')
   
   print('Students Failed For COMPUTER NETWORKS are :')
   cur.execute("SELECT collegeyearcode,roll FROM s3result where \
   college='"+collegename+"' and rlmca201='F'");
   while True:
    row = cur.fetchone()
    if row == None:
     break
    print(" "+row[0][0:8]+""+str(row[1]))
    #print(row)
    
    ##################################################################
    

   print('')
   print('')
   print('******  RLMCA203 - SOFTWARE ENGINEERING  ******  ')
   print('')
   
   print("Total appeared : " +str(lentotal))
   cur.execute("SELECT count(*) FROM s3result where \
   college='"+collegename+"' and rlmca203='F'")
   k = cur.fetchone()
   rlmca203fail=int(k[0])
   print("Total Pass  : " +str(lentotal-rlmca203fail))
   print("Total Fail  : " +str(rlmca203fail))
   a1=abs(lentotal-rlmca203fail)
   a1=a1/lentotal
   a1=a1*100
   print('Pass % of SOFTWARE ENGINEERING : '+str(a1))
   print('')
   
   print('Students Failed For SOFTWARE ENGINEERING are :')
   cur.execute("SELECT collegeyearcode,roll FROM s3result where \
   college='"+collegename+"' and rlmca203='F'");
   while True:
    row = cur.fetchone()
    if row == None:
     break
    print(" "+row[0][0:8]+""+str(row[1]))
    #print(row)
    
    ##################################################################

    
   print('')
   print('')
   print('******  RLMCA205 - DATABASE MANAGEMENT SYSTEMS  ******  ')
   print('')
   
   print("Total appeared : " +str(lentotal))
   cur.execute("SELECT count(*) FROM s3result where \
   college='"+collegename+"' and rlmca205='F'")
   k = cur.fetchone()
   rlmca205fail=int(k[0])
   print("Total Pass  : " +str(lentotal-rlmca205fail))
   print("Total Fail  : " +str(rlmca205fail))
   a1=abs(lentotal-rlmca205fail)
   a1=a1/lentotal
   a1=a1*100
   print('Pass % of DATABASE MANAGEMENT SYSTEMS : '+str(a1))
   print('')
   
   print('Students Failed For DATABASE MANAGEMENT SYSTEMS are :')
   cur.execute("SELECT collegeyearcode,roll FROM s3result where \
   college='"+collegename+"' and rlmca205='F'");
   while True:
    row = cur.fetchone()
    if row == None:
     break
    print(" "+row[0][0:8]+""+str(row[1]))
    #print(row)
    
    ##################################################################

   print('')
   print('')
   print('******  RLMCA207 - DESIGN AND ANALYSIS OF ALGORITHMS  ******  ')
   print('')
   
   print("Total appeared : " +str(lentotal))
   cur.execute("SELECT count(*) FROM s3result where \
   college='"+collegename+"' and rlmca207='F'")
   k = cur.fetchone()
   rlmca207fail=int(k[0])
   print("Total Pass  : " +str(lentotal-rlmca207fail))
   print("Total Fail  : " +str(rlmca207fail))
   a1=abs(lentotal-rlmca207fail)
   a1=a1/lentotal
   a1=a1*100
   print('Pass % of DESIGN AND ANALYSIS OF ALGORITHMS : '+str(a1))
   print('')
   
   print('Students Failed For DESIGN AND ANALYSIS OF ALGORITHMS are :')
   cur.execute("SELECT collegeyearcode,roll FROM s3result where \
   college='"+collegename+"' and rlmca207='F'");
   while True:
    row = cur.fetchone()
    if row == None:
     break
    print(" "+row[0][0:8]+""+str(row[1]))
    #print(row)
    
    ##################################################################

    
   print('')
   print('')
   print('******  RLMCA209 - WEB PROGRAMMING  ******  ')
   print('')
   
   print("Total appeared : " +str(lentotal))
   cur.execute("SELECT count(*) FROM s3result where \
   college='"+collegename+"' and rlmca209='F'")
   k = cur.fetchone()
   rlmca209fail=int(k[0])
   print("Total Pass  : " +str(lentotal-rlmca209fail))
   print("Total Fail  : " +str(rlmca209fail))
   a1=abs(lentotal-rlmca209fail)
   a1=a1/lentotal
   a1=a1*100
   print('Pass % of WEB PROGRAMMING : '+str(a1))
   print('')
   
   print('Students Failed For WEB PROGRAMMING are :')
   cur.execute("SELECT collegeyearcode,roll FROM s3result where \
   college='"+collegename+"' and rlmca209='F'");
   while True:
    row = cur.fetchone()
    if row == None:
     break
    print(" "+row[0][0:8]+""+str(row[1]))
    #print(row)
    
    ##################################################################

   
    ############# ************EOF*********  ################### 
 except psycopg2.Error as e:
  if conn:
   conn.rollback()
 
  print('Error %s' % e)    
  sys.exit(1)
 
 finally:   
  if conn:
   conn.close()
