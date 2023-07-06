# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3
import os
from tkinter import ttk
import datetime
import customtkinter
import sys
from dateutil.relativedelta import relativedelta
import numpy as np
import time

customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
#root.resizable(width=False, height=False)
width_sc = root.winfo_screenwidth()
height_sc = root.winfo_screenheight()
mybutton_font=("Times New Roman", 16, "bold")


def revers_words(string):
 s = string.split()[::-1]
 l = []
 for i in s:
    l.append(i)
 return " ".join(l)

def date_after(xx,dates):
 my_date = datetime.datetime(int(dates.split("/")[2]),int(dates.split("/")[1]),int(dates.split("/")[0]))
 now =  revers_words(str((my_date + relativedelta(months=+xx)).date()).replace("-",' ')).replace(" ",'/')
 return now

def dbase():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 c.execute("""
 create table if not exists siyana(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date text,
  mohima text,
  ism_3amil text,
  mawqi3_3amil text,
  ism_fani text,
  raqm_fatora_chira text,
  tarikh_fatora_chira text,
  naw3_jihaz text,
  modil_jihaz text,
  phone_number1 text,
  phone_number2 text,
  naw3_siyana text,
  molahadat text,
  naw3_daman text,
  sabab text,

  siyana__chahr_3 text,
  raq_fatorat_siyana_3 text,
  hal_tamat_siyana_3 text,
  molahadat_2_3 text,
  
  siyana__chahr_6 text,
  raq_fatorat_siyana_6 text,
  hal_tamat_siyana_6 text,
  molahadat_2_6 text,

  siyana__chahr_9 text,
  raq_fatorat_siyana_9 text,
  hal_tamat_siyana_9 text,
  molahadat_2_9 text,

  siyana__chahr_12 text,
  raq_fatorat_siyana_12 text,
  hal_tamat_siyana_12 text,
  molahadat_2_12 text,

  siyana__chahr_15 text,
  raq_fatorat_siyana_15 text,
  hal_tamat_siyana_15 text,
  molahadat_2_15 text,

  siyana__chahr_18 text,
  raq_fatorat_siyana_18 text,
  hal_tamat_siyana_18 text,
  molahadat_2_18 text,

  siyana__chahr_21 text,
  raq_fatorat_siyana_21 text,
  hal_tamat_siyana_21 text,
  molahadat_2_21 text,

  siyana__chahr_24 text,
  raq_fatorat_siyana_24 text,
  hal_tamat_siyana_24 text,
  molahadat_2_24 text
)""")
 conn.commit()
 conn.close()
dbase()

def userd_db_int():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 c.execute("""create table if not exists users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username text,
  password text,
  type text
 )""")
 conn.commit()
 conn.close()

userd_db_int()
def refresh_db():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 sql = "SELECT id,naw3_daman,sabab,siyana__chahr_24 FROM siyana"
 c.execute(sql)
 rows = c.fetchall()
 timenow = str(datetime.datetime.now()).split(' ')[0]
 
 yearnow = int(timenow.split("-")[0])
 mounthnow = int(timenow.split("-")[1])
 daynow = int(timenow.split("-")[2])
 for i in rows:
  id_s = i[0]
  naw3_daman = i[1]
  sabab = i[2]
  siyana__chahr24 = str(i[3]).split(" ")[0]
  ### siyana__chahr24 ###
  year24 = int(siyana__chahr24.split("/")[2])
  mounth24 = int(siyana__chahr24.split("/")[2])
  day24 = int(siyana__chahr24.split("/")[2])
  ### siyana__chahr24 ###
  params0 = ("خارج الضمان","انتهاء المدة 24 شهر ",id_s,)
  sql0 = """UPDATE siyana SET naw3_daman=?,sabab=? WHERE id=?"""
  
  params1 = ("داخل الضمان","",id_s,)
  sql1 = """UPDATE siyana SET naw3_daman=?,sabab=? WHERE id=?"""

  if(year24==yearnow and mounth24<mounthnow):
    c.execute(sql0, params0)
    conn.commit()
  elif(year24==yearnow and mounth24==mounthnow and day24<=daynow):
    c.execute(sql0, params0)
    conn.commit()
  elif(year24<yearnow):
    c.execute(sql0, params0)
    conn.commit()
  else:
    c.execute(sql1, params1)
    conn.commit()
 conn.close()

refresh_db()


def clear_opp():
 click1.set('')
 click2.set('')
 click3.set('')
 click4.set('')
 click5.set('')
 click11.set('')
 click22.set('')
 click33.set('')
 click44.set('')
 click55.set('')
 click66.set('')
 notes.set('')
 vvvs.configure(text_color='#21B000')
 notes.set("تم التفريغ بنجاح ")

def clear_siyan():
 click1_butt_siyana.set('')
 click22_butt_siyana.set('')
 click3_butt_siyana.set('')
 click5_butt_siyana.set('')
 click4_butt_siyana.set('')


def show_infos():
 
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 click6.set('')
 if(len(click2.get())>0):
  c.execute("""SELECT * FROM siyana WHERE ism_3amil=? """, (str(click2.get()),))
  vvvs.configure(text_color='#21B000')
  notes.set("تم العرض بنجاح")
 elif(len(click5.get())>0):
  c.execute("""SELECT * FROM siyana WHERE raqm_fatora_chira=? """, (str(click5.get()),))
  vvvs.configure(text_color='#21B000')
  notes.set("تم العرض بنجاح")
 elif(len(click33.get())>0):
  c.execute("""SELECT * FROM siyana WHERE phone_number1=? """, (str(click33.get()),))
  vvvs.configure(text_color='#21B000')
  notes.set("تم العرض بنجاح")
 elif(len(click44.get())>0):
  c.execute("""SELECT * FROM siyana WHERE phone_number2=? """, (str(click44.get()),))
  vvvs.configure(text_color='#21B000')
  notes.set("تم العرض بنجاح")
 else:
  vvvs.configure(text_color='#F02849')
  txt = '! يرجى ادخال اسم العميل او رقم فاتورة الشراء او رقم الهاتف لاظهار البيانات '
  notes.set(txt)
 rowss = c.fetchall()
 rows = np.asarray(rowss[0])
 ii=0
 for i in rows:
  if(i=='-' and ii!=1):
   rows[ii]=''
  ii = ii + 1
  
 click1.set(rows[2])
 click2.set(rows[3])
 click3.set(rows[4])
 click4.set(rows[5])
 click5.set(rows[6])
 click6.set(rows[7])
 click11.set(rows[8])
 click22.set(rows[9])
 click33.set(rows[10])
 click44.set(rows[11])
 click55.set(rows[12])
 click66.set(rows[13])
 conn.close()


def create_my_table(rol,i,rows,frame):
 for row in rows:
  e1= customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/13))-40,border_width=0,font=mybutton_font,corner_radius=0)
  e1.grid(row=rol, column=i)
  e1.insert(END,row[0]) 
  i=i-1
  e2=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)-30),border_width=0,font=mybutton_font,corner_radius=0)
  e2.grid(row=rol, column=i)
  e2.insert(END,row[1]) 
  i=i-1
  e3=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e3.grid(row=rol, column=i)
  e3.insert(END,row[2])
  i=i-1
  e4=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)+10),border_width=0,font=mybutton_font,corner_radius=0)
  e4.grid(row=rol, column=i)
  e4.insert(END,row[3])
  i=i-1
  e5=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)+20),border_width=0,font=mybutton_font,corner_radius=0)
  e5.grid(row=rol, column=i)
  e5.insert(END,row[4]) 
  i=i-1
  e6=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e6.grid(row=rol, column=i)
  e6.insert(END,row[5])
  i=i-1
  e7=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e7.grid(row=rol, column=i)
  e7.insert(END,row[6]) 
  i=i-1
  e8=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e8.grid(row=rol, column=i)
  e8.insert(END,row[7])
  i=i-1
  e9=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e9.grid(row=rol, column=i)
  e9.insert(END,row[8]) 
  i=i-1
  e10=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e10.grid(row=rol, column=i)
  e10.insert(END,"صيانة "+row[9] + " شهر")
  i=i-1
  e11=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)),border_width=0,font=mybutton_font,corner_radius=0)
  e11.grid(row=rol, column=i)
  e11.insert(END,row[10])
  i=i-1
  e12=customtkinter.CTkEntry(frame,justify='right',width=int((width_sc/12)+20),border_width=0,font=mybutton_font,corner_radius=0)
  e12.grid(row=rol, column=i)
  e12.insert(END,row[11])
  i = 11
  rol = rol + 1


scans = 0
def insert_to_db():
 conn = sqlite3.connect('sin.db')
 conf = conn.cursor()

 _one=str(click1.get())
 _two=str(click2.get())
 _mm=str(click3.get())
 _four=str(click4.get())
 _five=str(click5.get())
 _six=str(click6.get())
 _seven=str(click11.get())
 _eight=str(click22.get())
 _night=str(click33.get())
 _ten=str(click44.get())
 _eleven=str(click55.get())
 _twelve=str(click66.get())
 
 if(len(_one)==0 and len(_two)==0 and len(_mm)==0 and len(_four)==0 and len(_five)==0 
  and len(_seven)==0 and len(_eight)==0 and len(_night)==0 
  and len(_ten)==0 and len(_eleven)==0 and len(_twelve)==0):
  vvvs.configure(text_color='#F02849')
  notes.set('يرجى ملئ احد الحقول لادخال بيانات مستخدم جديد ,او التعديل')
  conn.close()

 opt = (_two,_five,_night,_ten,)
 conf.execute("""SELECT * FROM siyana WHERE ism_3amil=? or raqm_fatora_chira=? or phone_number1=? or 
     phone_number2=?""",opt)
 rows = conf.fetchall()
 date_now_y_m_d = datetime.datetime.now().strftime("%d/%m/%Y")
 a="raq_fatorat_siyana_3,hal_tamat_siyana_3,molahadat_2_3"
 b="raq_fatorat_siyana_6,hal_tamat_siyana_6,molahadat_2_6"
 c="raq_fatorat_siyana_9,hal_tamat_siyana_9,molahadat_2_9"
 d="raq_fatorat_siyana_12,hal_tamat_siyana_12,molahadat_2_12"
 e="raq_fatorat_siyana_15,hal_tamat_siyana_15,molahadat_2_15"
 f="raq_fatorat_siyana_18,hal_tamat_siyana_18,molahadat_2_18"
 g="raq_fatorat_siyana_21,hal_tamat_siyana_21,molahadat_2_21"
 h="raq_fatorat_siyana_24,hal_tamat_siyana_24,molahadat_2_24"
 if(len(rows)==0): 
  if(len(_one)==0):
   _one="-"
  if(len(_two)==0):
   _two="-"
  if(len(_mm)==0):
   _mm="-"
  if(len(_four)==0):
   _four="-"
  if(len(_five)==0):
   _five="-"
  if(len(_six)==0):
   _six="-"
  if(len(_seven)==0):
   _seven="-"
  if(len(_eight)==0):
   _eight="-"
  if(len(_night)==0):
   _night="-"
  if(len(_ten)==0):
   _ten="-"
  if(len(_eleven)==0):
   _eleven="-"
  if(len(_twelve)==0):
   _twelve="-"
  if(_eleven=="اشهر 3"):
   chahr3 = date_after(3,_six)
   chahr6 = date_after(6,_six)
   chahr9 = date_after(9,_six)
   chahr12 = date_after(12,_six)
   chahr15 = date_after(15,_six)
   chahr18 = date_after(18,_six)
   chahr21 = date_after(21,_six)
   chahr24 = date_after(24,_six)
   params = (date_now_y_m_d,_one,_two,_mm,_four,_five,_six,_seven,_eight,_night,_ten,_eleven,_twelve,chahr3,chahr6,chahr9,chahr12,chahr15,chahr18,chahr21,chahr24,)
  
   sq_sup = """siyana__chahr_3,"""+a+""",siyana__chahr_6,"""+b+""",siyana__chahr_9,"""+c+""",siyana__chahr_12,"""+d+""",siyana__chahr_15,"""+e+""",siyana__chahr_18,"""+f+""",siyana__chahr_21,"""+g+""",siyana__chahr_24,"""+h
   sql = """INSERT INTO siyana (date,mohima ,ism_3amil ,mawqi3_3amil,ism_fani 
  ,raqm_fatora_chira ,tarikh_fatora_chira , naw3_jihaz ,modil_jihaz 
  ,phone_number1 ,phone_number2,naw3_siyana , molahadat,naw3_daman,sabab,"""+sq_sup+""")
   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,'داخل الضمان','-',?,"-","-","-",?,"-","-","-",?,"-","-","-",?,"-","-","-",?,"-","-","-",?,"-","-","-",?,"-","-","-",?,"-","-","-")
  """
  else:
   chahr3 = ""
   chahr6 = date_after(6,_six)
   chahr9 = ""
   chahr12 = date_after(12,_six)
   chahr15 = ""
   chahr18 = date_after(18,_six)
   chahr21 = ""
   chahr24 = date_after(24,_six)

   params = (date_now_y_m_d,_one,_two,_mm,_four,_five,_six,_seven,_eight,_night,_ten,_eleven,_twelve,chahr6,chahr12,chahr18,chahr24,)
  
   sq_sup = """siyana__chahr_3,"""+a+""",siyana__chahr_6,"""+b+""",siyana__chahr_9,"""+c+""",siyana__chahr_12,"""+d+""",siyana__chahr_15,"""+e+""",siyana__chahr_18,"""+f+""",siyana__chahr_21,"""+g+""",siyana__chahr_24,"""+h
   sql = """INSERT INTO siyana (date,mohima ,ism_3amil ,mawqi3_3amil,ism_fani 
  ,raqm_fatora_chira ,tarikh_fatora_chira , naw3_jihaz ,modil_jihaz 
  ,phone_number1 ,phone_number2,naw3_siyana , molahadat,naw3_daman,sabab,"""+sq_sup+""")
   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,'داخل الضمان','-','-',"-","-","-",?,"-","-","-",'-',"-","-","-",?,"-","-","-",'-',"-","-","-",?,"-","-","-",'-',"-","-","-",?,"-","-","-")
  """

  conf.execute(sql, params)
  conn.commit()
  clear_opp()
  vvvs.configure(text_color='#21B000')
  notes.set("تم الحفظ بنجاح")
 else:

  if(len(_eleven)>0):
   conf.execute("""UPDATE siyana SET naw3_siyana=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_eleven,_two,_five,_night,_ten,))
   conn.commit()
   
  if(len(_twelve)>0):
   conf.execute("""UPDATE siyana SET molahadat=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_twelve,_two,_five,_night,_ten,))
   conn.commit()
   
  if(len(_one)>0):
   conf.execute("""UPDATE siyana SET mohima=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_one,_two,_five,_night,_ten,))
   conn.commit()
  
  if(len(_mm)>0):
   conf.execute("""UPDATE siyana SET mawqi3_3amil=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_mm,_two,_five,_night,_ten,))
   conn.commit()
   
  if(len(_four)>0):
   conf.execute("""UPDATE siyana SET ism_fani=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_four,_two,_five,_night,_ten,))
   conn.commit()
   
  if(len(_six)>0):
   conf.execute("""UPDATE siyana SET tarikh_fatora_chira=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_six,_two,_five,_night,_ten,))
   conn.commit()
   
  if(len(_seven)>0):
   conf.execute("""UPDATE siyana SET naw3_jihaz=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_seven,_two,_five,_night,_ten,))
   conn.commit()
  
  if(len(_eight)>0):
   conf.execute("""UPDATE siyana SET modil_jihaz=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_eight,_two,_five,_night,_ten,))
   conn.commit()
  
  if(len(_two)>0):
   conf.execute("""UPDATE siyana SET ism_3amil=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_two,_two,_five,_night,_ten,))
   conn.commit()
  
  if(len(_five)>0):
   conf.execute("""UPDATE siyana SET raqm_fatora_chira=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_five,_two,_five,_night,_ten,))
   conn.commit()
  
  if(len(_night)>0):
   conf.execute("""UPDATE siyana SET phone_number1=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_night,_two,_five,_night,_ten,))
   conn.commit()
  
  if(len(_ten)>0):
   conf.execute("""UPDATE siyana SET phone_number2=? WHERE ism_3amil=? or raqm_fatora_chira=? or 
     phone_number1=? or phone_number2=?""",(_ten,_two,_five,_night,_ten,))
   conn.commit()
  clear_opp()
  vvvs.configure(text_color='#21B000')
  notes.set("تم تعديل بيانات المستخدم بنجاح")
  
 conn.close()


def user_optsd():

 usr_opt = customtkinter.CTkFrame(root,width=500,height=300,fg_color='transparent')
 butt = customtkinter.CTkFrame(usr_opt,fg_color='transparent')
 logout = customtkinter.CTkButton(butt,fg_color='#F02849',text="عودة",font=mybutton_font,command=lambda :first_win(True,usr_opt))
 ard = customtkinter.CTkButton(butt,text="عرض",font=mybutton_font,command=a3ard_opt)
 tafrigh = customtkinter.CTkButton(butt,text="تفريغ",font=mybutton_font,command=tafrigh_opt)
 
 logout.grid(row=1,column=1,padx=15,pady=15,ipady=5)
 tafrigh.grid(row=1,column=2,padx=15,pady=15,ipady=5)
 ard.grid(row=1,column=3,padx=15,pady=15,ipady=5)
 butt.pack(padx=30,pady=30)
 tabl_opt = customtkinter.CTkFrame(usr_opt)
 
 mystr1 = customtkinter.StringVar()
 mystr1.set( "رقم" )
 td1 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=1,column=8)
 mystr2 = customtkinter.StringVar()
 mystr2.set( "التاريخ" )
 td2 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=2,column=8)
 mystr3 = customtkinter.StringVar()
 mystr3.set( "المهمة" )
 td3 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=3,column=8)
 mystr4 = customtkinter.StringVar()
 mystr4.set( "اسم العميل" )
 td4 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=4,column=8)
 mystr5 = customtkinter.StringVar()
 mystr5.set( "موقع العميل" )
 td5 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=5,column=8)
 mystr6 = customtkinter.StringVar()
 mystr6.set( "اسم الفني" )
 td6 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=6,column=8)
 mystr7 = customtkinter.StringVar()
 mystr7.set( "رقم ف الشراء" )
 td7 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=7,column=8)
 mystr8 = customtkinter.StringVar()
 mystr8.set( "تاريخ ف الشراء" )
 td8 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=8,column=8)
 mystr9 = customtkinter.StringVar()
 mystr9.set( "نوع الجهاز" )
 td9 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=9,column=8)
 mystr10 = customtkinter.StringVar()
 mystr10.set( "موديل الجهاز" )
 td10 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=10,column=8)
 mystr11 = customtkinter.StringVar()
 mystr11.set( "رقم الهاتف 1" )
 td11 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=11,column=8)
 mystr12 = customtkinter.StringVar()
 mystr12.set( "رقم الهاتف 2" )
 td12 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr12,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td12.grid(row=12,column=8)
 #---
 global s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12
 s1 = customtkinter.StringVar()
 ss1 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s1,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss1.grid(row=1,column=7)
 s2 = customtkinter.StringVar()
 ss2 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s2,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss2.grid(row=2,column=7)
 s3 = customtkinter.StringVar()
 ss3 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s3,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss3.grid(row=3,column=7)
 s4 = customtkinter.StringVar()
 ss4 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s4,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss4.grid(row=4,column=7)
 s5 = customtkinter.StringVar()
 ss5 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s5,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss5.grid(row=5,column=7)
 s6 = customtkinter.StringVar()
 ss6 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s6,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss6.grid(row=6,column=7)
 s7 = customtkinter.StringVar()
 ss7 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s7,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss7.grid(row=7,column=7)
 s8 = customtkinter.StringVar()
 ss8 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s8,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss8.grid(row=8,column=7)
 s9 = customtkinter.StringVar()
 ss9 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s9,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss9.grid(row=9,column=7)
 s10 = customtkinter.StringVar()
 ss10 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s10,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss10.grid(row=10,column=7)
 s11 = customtkinter.StringVar()
 ss11 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s11,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss11.grid(row=11,column=7)
 s12 = customtkinter.StringVar()
 ss12 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s12,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss12.grid(row=12,column=7)
 mystr13 = customtkinter.StringVar()
 mystr13.set( "نوع الصيانة" )
 td13 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr13,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td13.grid(row=1,column=6)
 mystr14 = customtkinter.StringVar()
 mystr14.set( "ملاحظات" )
 td14 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr14,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td14.grid(row=2,column=6)
 mystr15 = customtkinter.StringVar()
 mystr15.set( "نوع الضمان" )
 td15 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr15,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td15.grid(row=3,column=6)
 mystr16 = customtkinter.StringVar()
 mystr16.set( "السبب" )
 td16 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr16,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td16.grid(row=4,column=6)
 mystr17 = customtkinter.StringVar()
 mystr17.set( "صيانة 3 اشهر" )
 td17 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr17,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td17.grid(row=5,column=6)
 mystr18 = customtkinter.StringVar()
 mystr18.set( "رقم فاتورة الصيانة" )
 td18 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr18,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td18.grid(row=6,column=6)
 mystr19 = customtkinter.StringVar()
 mystr19.set( "هل تمت الصيانة" )
 td19 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr19,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td19.grid(row=7,column=6)
 mystr20 = customtkinter.StringVar()
 mystr20.set( "ملاحظات" )
 td20 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr20,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td20.grid(row=8,column=6)
 mystr21 = customtkinter.StringVar()
 mystr21.set( "صيانة 6 اشهر " )
 td21 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr21,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td21.grid(row=9,column=6)
 mystr22 = customtkinter.StringVar()
 mystr22.set( "رقم فاتورة الصيانة" )
 td22 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr22,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td22.grid(row=10,column=6)
 mystr23 = customtkinter.StringVar()
 mystr23.set( "هل تمت الصيانة" )
 td23 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr23,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td23.grid(row=11,column=6)
 mystr24 = customtkinter.StringVar()
 mystr24.set( "ملاحظات" )
 td24 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr24,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td24.grid(row=12,column=6)
 #--
 global s_11,s22,s33,s44,s55,s66,s77,s88,s99,s100,s110,s120

 s_11 = customtkinter.StringVar()
 ss11 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s_11,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss11.grid(row=1,column=5)
 s22 = customtkinter.StringVar()
 ss22 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s22,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss22.grid(row=2,column=5)
 s33 = customtkinter.StringVar()
 ss33 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s33,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss33.grid(row=3,column=5)
 s44 = customtkinter.StringVar()
 ss44 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s44,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss44.grid(row=4,column=5)
 s55 = customtkinter.StringVar()
 ss55 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s55,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss55.grid(row=5,column=5)
 s66 = customtkinter.StringVar()
 ss66 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s66,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss66.grid(row=6,column=5)
 s77 = customtkinter.StringVar()
 ss77 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s77,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss77.grid(row=7,column=5)
 s88 = customtkinter.StringVar()
 ss88 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s88,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss88.grid(row=8,column=5)
 s99 = customtkinter.StringVar()
 ss99 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s99,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss99.grid(row=9,column=5)
 s100 = customtkinter.StringVar()
 ss100 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s100,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss100.grid(row=10,column=5)
 s110 = customtkinter.StringVar()
 ss110 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s110,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss110.grid(row=11,column=5)
 s120 = customtkinter.StringVar()
 ss120 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s120,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss120.grid(row=12,column=5)

 #//////////////// taqrir akhir ---------////////////////
 mystr25 = customtkinter.StringVar()
 mystr25.set( "صيانة 9 اشهر" )
 td25 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr25,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td25.grid(row=1,column=4)
 
 mystr26 = customtkinter.StringVar()
 mystr26.set( "رقم فاتورة الصيانة" )
 td26 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr26,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td26.grid(row=2,column=4)

 mystr27 = customtkinter.StringVar()
 mystr27.set( "هل تمت الصيانة" )
 td27 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr27,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td27.grid(row=3,column=4)

 mystr28 = customtkinter.StringVar()
 mystr28.set( "ملاحظات" )
 td28 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr28,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td28.grid(row=4,column=4)

 mystr29 = customtkinter.StringVar()
 mystr29.set( "صيانة 12 شهر" )
 td29 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr29,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td29.grid(row=5,column=4)

 mystr30 = customtkinter.StringVar()
 mystr30.set( "رقم فاتورة الصيانة" )
 td30 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr30,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td30.grid(row=6,column=4)

 mystr31 = customtkinter.StringVar()
 mystr31.set( "هل تمت الصيانة" )
 td31 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr31,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td31.grid(row=7,column=4)

 mystr32 = customtkinter.StringVar()
 mystr32.set( "ملاحظات" )
 td32 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr32,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td32.grid(row=8,column=4)

 mystr33 = customtkinter.StringVar()
 mystr33.set( "صيانة 15 شهر" )
 td33 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr33,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td33.grid(row=9,column=4)

 mystr34 = customtkinter.StringVar()
 mystr34.set( "رقم فاتورة الصيانة" )
 td34 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr34,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td34.grid(row=10,column=4)

 mystr35 = customtkinter.StringVar()
 mystr35.set( "هل تمت الصيانة" )
 td35 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr35,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td35.grid(row=11,column=4)

 mystr36 = customtkinter.StringVar()
 mystr36.set( "ملاحظات" )
 td36 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr36,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td36.grid(row=12,column=4)
 #--
 global s111,s221,s331,s441,s551,s661,s771,s881,s991,s1001,s1101,s1201

 s111 = customtkinter.StringVar()
 ss111 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s111,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss111.grid(row=1,column=3)
 s221 = customtkinter.StringVar()
 ss221 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s221,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss221.grid(row=2,column=3)
 s331 = customtkinter.StringVar()
 ss331 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s331,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss331.grid(row=3,column=3)
 s441 = customtkinter.StringVar()
 ss441 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s441,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss441.grid(row=4,column=3)
 s551 = customtkinter.StringVar()
 ss551 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s551,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss551.grid(row=5,column=3)
 s661 = customtkinter.StringVar()
 ss661 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s661,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss661.grid(row=6,column=3)
 s771 = customtkinter.StringVar()
 ss771 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s771,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss771.grid(row=7,column=3)
 s881 = customtkinter.StringVar()
 ss881 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s881,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss881.grid(row=8,column=3)
 s991 = customtkinter.StringVar()
 ss991 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s991,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss991.grid(row=9,column=3)
 s1001 = customtkinter.StringVar()
 ss1001 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s1001,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss1001.grid(row=10,column=3)
 s1101 = customtkinter.StringVar()
 ss1101 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s1101,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss1101.grid(row=11,column=3)
 s1201 = customtkinter.StringVar()
 ss1201 = customtkinter.CTkEntry(tabl_opt,justify='right',font=mybutton_font,textvariable=s1201,border_width=0.8,corner_radius=0,width=int((width_sc/13))+30)
 ss1201.grid(row=12,column=3)
 #taqrir ///////////////////---


 mystr37 = customtkinter.StringVar()
 mystr37.set( "صيانة 18 شهر" )
 td37 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr37,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td37.grid(row=1,column=2)

 mystr38 = customtkinter.StringVar()
 mystr38.set( "رقم فاتورة الصيانة" )
 td38 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr38,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td38.grid(row=2,column=2)

 mystr39 = customtkinter.StringVar()
 mystr39.set( "هل تمت الصيانة" )
 td39 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr39,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td39.grid(row=3,column=2)

 mystr40 = customtkinter.StringVar()
 mystr40.set( "ملاحظات" )
 td40 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr40,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td40.grid(row=4,column=2)

 mystr41 = customtkinter.StringVar()
 mystr41.set( "صيانة 21 شهر" )
 td41 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr41,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td41.grid(row=5,column=2)

 mystr42 = customtkinter.StringVar()
 mystr42.set( "رقم فاتورة الصيانة" )
 td42= customtkinter.CTkEntry(tabl_opt,textvariable=mystr42,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td42.grid(row=6,column=2)

 mystr43 = customtkinter.StringVar()
 mystr43.set( "هل تمت الصيانة" )
 td43 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr43,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td43.grid(row=7,column=2)

 mystr44 = customtkinter.StringVar()
 mystr44.set( "ملاحظات" )
 td44 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr44,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td44.grid(row=8,column=2)

 mystr45 = customtkinter.StringVar()
 mystr45.set( "صيانة 24 شهر" )
 td45 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr45,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td45.grid(row=9,column=2)

 mystr46 = customtkinter.StringVar()
 mystr46.set( "رقم فاتورة الصيانة" )
 td46 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr46,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td46.grid(row=10,column=2)

 mystr47 = customtkinter.StringVar()
 mystr47.set( "هل تمت الصيانة" )
 td47 = customtkinter.CTkEntry(tabl_opt,textvariable=mystr47,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td47.grid(row=11,column=2)

 mystr48 = customtkinter.StringVar()
 mystr48.set( "ملاحظات" )
 td48= customtkinter.CTkEntry(tabl_opt,textvariable=mystr48,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)+30),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td48.grid(row=12,column=2)
#--

 global s112,s222,s332,s442,s552,s662,s772,s882,s992,s1002,s1102,s1202

 s112 = customtkinter.StringVar()
 ss112 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s112,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss112.grid(row=1,column=1)
 s222 = customtkinter.StringVar()
 ss222 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s222,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss222.grid(row=2,column=1)
 s332 = customtkinter.StringVar()
 ss332 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s332,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss332.grid(row=3,column=1)
 s442 = customtkinter.StringVar()
 ss442 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s442,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss442.grid(row=4,column=1)
 s552 = customtkinter.StringVar()
 ss552 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s552,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss552.grid(row=5,column=1)
 s662 = customtkinter.StringVar()
 ss662 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s662,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss662.grid(row=6,column=1)
 s772 = customtkinter.StringVar()
 ss772 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s772,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss772.grid(row=7,column=1)
 s882 = customtkinter.StringVar()
 ss882 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s882,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss882.grid(row=8,column=1)
 s992 = customtkinter.StringVar()
 ss992 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s992,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss992.grid(row=9,column=1)
 s1002 = customtkinter.StringVar()
 ss1002 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s1002,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss1002.grid(row=10,column=1)
 s1102 = customtkinter.StringVar()
 ss1102 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s1102,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss1102.grid(row=11,column=1)
 s1202 = customtkinter.StringVar()
 ss1202 = customtkinter.CTkEntry(tabl_opt,justify='right',textvariable=s1202,border_width=0.8,corner_radius=0.8,font=mybutton_font,width=int((width_sc/13))+30)
 ss1202.grid(row=12,column=1)

 tabl_opt.pack(pady=50,padx=20)
 usr_opt.pack()

def a3ard_opt():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 id_ = str(s1.get())
 ism_3=str(s4.get())
 raqm_fatora_chir=str(s7.get())
 phon1=str(s11.get())
 phon2=str(s12.get())
 print(id_+" "+ism_3+" "+raqm_fatora_chir+" "+phon1+" "+phon2)
 sqq = "select * from siyana where id=? or ism_3amil=? or raqm_fatora_chira=? or phone_number1=? or phone_number2=?"

 c.execute(sqq,(id_,ism_3,raqm_fatora_chir,phon1,phon2,))
 row = np.asarray(c.fetchall()[0])
 s1.set(row[0])
 s2.set(row[1])
 s3.set(row[2])
 s4.set(row[3])
 s5.set(row[4])
 s6.set(row[5])
 s7.set(row[6])
 s8.set(row[7])
 s9.set(row[8])
 s10.set(row[9])
 s11.set(row[10])
 s12.set(row[11])
 s_11.set(row[12])
 s22.set(row[13])
 s33.set(row[14])
 s44.set(row[15])
 s55.set(row[16])
 s66.set(row[17])
 s77.set(row[18])
 s88.set(row[19])
 s99.set(row[20])
 s100.set(row[21])
 s110.set(row[22])
 s120.set(row[23])
 s111.set(row[24])
 s221.set(row[25])
 s331.set(row[26])
 s441.set(row[27])
 s551.set(row[28])
 s661.set(row[29])
 s771.set(row[30])
 s881.set(row[31])
 s991.set(row[32])
 s1001.set(row[33])
 s1101.set(row[34])
 s1201.set(row[35])
 s112.set(row[36])
 s222.set(row[37])
 s332.set(row[38])
 s442.set(row[39])
 s552.set(row[40])
 s662.set(row[41])
 s772.set(row[42])
 s882.set(row[43])
 s992.set(row[44])
 s1002.set(row[45])
 s1102.set(row[46])
 s1202.set(row[47])
 conn.close()
dbase()
def tafrigh_opt():
 s1.set("")
 s2.set("")
 s3.set("")
 s4.set("")
 s5.set("")
 s6.set("")
 s7.set("")
 s8.set("")
 s9.set("")
 s10.set("")
 s11.set("")
 s12.set("")
 s_11.set("")
 s22.set("")
 s33.set("")
 s44.set("")
 s55.set("")
 s66.set("")
 s77.set("")
 s88.set("")
 s99.set("")
 s100.set("")
 s110.set("")
 s120.set("")
 s111.set("")
 s221.set("")
 s331.set("")
 s441.set("")
 s551.set("")
 s661.set("")
 s771.set("")
 s881.set("")
 s991.set("")
 s1001.set("")
 s1101.set("")
 s1201.set("")
 s112.set("")
 s222.set("")
 s332.set("")
 s442.set("")
 s552.set("")
 s662.set("")
 s772.set("")
 s882.set("")
 s992.set("")
 s1002.set("")
 s1102.set("")
 s1202.set("")

 
def c9_comm():
 clear_frame(choose_frame)
 root.state("zoomed")
 root.resizable(width=True, height=True)
 user_optsd()
 






def db_show_all():
 global sc2
 global hscrollbar,vscrollbar,canvas,frame
 root.state("zoomed")
 root.resizable(width=True,height=True)

 frame = Frame(root,width=width_sc,height=height_sc)
 frame2 = Frame(frame,width=width_sc,height=height_sc)

 logout = customtkinter.CTkButton(frame2,fg_color='#F02849',text="عودة",font=mybutton_font,command=lambda :first_win(True,frame))
 logout.pack()
 frame2.pack(pady=10,padx=10)

 hscrollbar = Scrollbar(frame, orient = HORIZONTAL)
 vscrollbar = Scrollbar(frame, orient = VERTICAL)
 canvas = Canvas(frame,width=width_sc,height=height_sc, bd=0, highlightthickness=0, yscrollcommand = vscrollbar.set, xscrollcommand = hscrollbar.set)
 
 vscrollbar.config(command = canvas.yview)
 hscrollbar.config(command = canvas.xview)


# Add controls here
 sc2 = Frame(canvas,width=width_sc,height=height_sc)

 mystr1 = customtkinter.StringVar()
 mystr1.set( "رقم" )
 td1 = customtkinter.CTkEntry(sc2,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=0,column=48)

 mystr2 = customtkinter.StringVar()
 mystr2.set( "التاريخ" )
 td2 = customtkinter.CTkEntry(sc2,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=0,column=47)
 
 mystr3 = customtkinter.StringVar()
 mystr3.set( "المهمة" )
 td3 = customtkinter.CTkEntry(sc2,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=0,column=46)

 mystr4 = customtkinter.StringVar()
 mystr4.set( "اسم العميل" )
 td4 = customtkinter.CTkEntry(sc2,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=0,column=45)

 mystr5 = customtkinter.StringVar()
 mystr5.set( "موقع العميل" )
 td5 = customtkinter.CTkEntry(sc2,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=0,column=44)

 mystr6 = customtkinter.StringVar()
 mystr6.set( "اسم الفني" )
 td6 = customtkinter.CTkEntry(sc2,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=0,column=43)

 mystr7 = customtkinter.StringVar()
 mystr7.set( "رقم ف الشراء" )
 td7 = customtkinter.CTkEntry(sc2,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=0,column=42)
 
 mystr8 = customtkinter.StringVar()
 mystr8.set( "تاريخ ف الشراء" )
 td8 = customtkinter.CTkEntry(sc2,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=0,column=41)
 
 mystr9 = customtkinter.StringVar()
 mystr9.set( "نوع الجهاز" )
 td9 = customtkinter.CTkEntry(sc2,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=0,column=40)
 
 mystr10 = customtkinter.StringVar()
 mystr10.set( "موديل الجهاز" )
 td10 = customtkinter.CTkEntry(sc2,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=0,column=39)

 mystr11 = customtkinter.StringVar()
 mystr11.set( "رقم الهاتف 1" )
 td11 = customtkinter.CTkEntry(sc2,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=0,column=38)

 mystr12 = customtkinter.StringVar()
 mystr12.set( "رقم الهاتف 2" )
 td12 = customtkinter.CTkEntry(sc2,textvariable=mystr12,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td12.grid(row=0,column=37)

 mystr13 = customtkinter.StringVar()
 mystr13.set( "نوع الصيانة" )
 td13 = customtkinter.CTkEntry(sc2,textvariable=mystr13,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td13.grid(row=0,column=36)

 mystr14 = customtkinter.StringVar()
 mystr14.set( "ملاحظات" )
 td14 = customtkinter.CTkEntry(sc2,textvariable=mystr14,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td14.grid(row=0,column=35)

 mystr15 = customtkinter.StringVar()
 mystr15.set( "نوع الضمان" )
 td15 = customtkinter.CTkEntry(sc2,textvariable=mystr15,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td15.grid(row=0,column=34)

 mystr16 = customtkinter.StringVar()
 mystr16.set( "السبب" )
 td16 = customtkinter.CTkEntry(sc2,textvariable=mystr16,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td16.grid(row=0,column=33)

 mystr17 = customtkinter.StringVar()
 mystr17.set( "صيانة 3 اشهر" )
 td17 = customtkinter.CTkEntry(sc2,textvariable=mystr17,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td17.grid(row=0,column=32)

 mystr18 = customtkinter.StringVar()
 mystr18.set( "رقم فاتورة الصيانة" )
 td18 = customtkinter.CTkEntry(sc2,textvariable=mystr18,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td18.grid(row=0,column=31)

 mystr19 = customtkinter.StringVar()
 mystr19.set( "هل تمت الصيانة" )
 td19 = customtkinter.CTkEntry(sc2,textvariable=mystr19,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td19.grid(row=0,column=30)

 mystr20 = customtkinter.StringVar()
 mystr20.set( "ملاحظات" )
 td20 = customtkinter.CTkEntry(sc2,textvariable=mystr20,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td20.grid(row=0,column=29)

 mystr21 = customtkinter.StringVar()
 mystr21.set( "صيانة 6 اشهر " )
 td21 = customtkinter.CTkEntry(sc2,textvariable=mystr21,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td21.grid(row=0,column=28)

 mystr22 = customtkinter.StringVar()
 mystr22.set( "رقم فاتورة الصيانة" )
 td22 = customtkinter.CTkEntry(sc2,textvariable=mystr22,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td22.grid(row=0,column=27)

 mystr23 = customtkinter.StringVar()
 mystr23.set( "هل تمت الصيانة" )
 td23 = customtkinter.CTkEntry(sc2,textvariable=mystr23,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td23.grid(row=0,column=26)

 mystr24 = customtkinter.StringVar()
 mystr24.set( "ملاحظات" )
 td24 = customtkinter.CTkEntry(sc2,textvariable=mystr24,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td24.grid(row=0,column=25)

 mystr25 = customtkinter.StringVar()
 mystr25.set( "صيانة 9 اشهر" )
 td25 = customtkinter.CTkEntry(sc2,textvariable=mystr25,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td25.grid(row=0,column=24)
 
 mystr26 = customtkinter.StringVar()
 mystr26.set( "رقم فاتورة الصيانة" )
 td26 = customtkinter.CTkEntry(sc2,textvariable=mystr26,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td26.grid(row=0,column=23)

 mystr27 = customtkinter.StringVar()
 mystr27.set( "هل تمت الصيانة" )
 td27 = customtkinter.CTkEntry(sc2,textvariable=mystr27,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td27.grid(row=0,column=22)

 mystr28 = customtkinter.StringVar()
 mystr28.set( "ملاحظات" )
 td28 = customtkinter.CTkEntry(sc2,textvariable=mystr28,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td28.grid(row=0,column=21)

 mystr29 = customtkinter.StringVar()
 mystr29.set( "صيانة 12 شهر" )
 td29 = customtkinter.CTkEntry(sc2,textvariable=mystr29,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td29.grid(row=0,column=20)

 mystr30 = customtkinter.StringVar()
 mystr30.set( "رقم فاتورة الصيانة" )
 td30 = customtkinter.CTkEntry(sc2,textvariable=mystr30,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td30.grid(row=0,column=19)

 mystr31 = customtkinter.StringVar()
 mystr31.set( "هل تمت الصيانة" )
 td31 = customtkinter.CTkEntry(sc2,textvariable=mystr31,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td31.grid(row=0,column=18)

 mystr32 = customtkinter.StringVar()
 mystr32.set( "ملاحظات" )
 td32 = customtkinter.CTkEntry(sc2,textvariable=mystr32,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td32.grid(row=0,column=17)

 mystr33 = customtkinter.StringVar()
 mystr33.set( "صيانة 15 شهر" )
 td33 = customtkinter.CTkEntry(sc2,textvariable=mystr33,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td33.grid(row=0,column=16)

 mystr34 = customtkinter.StringVar()
 mystr34.set( "رقم فاتورة الصيانة" )
 td34 = customtkinter.CTkEntry(sc2,textvariable=mystr34,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td34.grid(row=0,column=15)

 mystr35 = customtkinter.StringVar()
 mystr35.set( "هل تمت الصيانة" )
 td35 = customtkinter.CTkEntry(sc2,textvariable=mystr35,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td35.grid(row=0,column=14)

 mystr36 = customtkinter.StringVar()
 mystr36.set( "ملاحظات" )
 td36 = customtkinter.CTkEntry(sc2,textvariable=mystr36,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td36.grid(row=0,column=13)

 mystr37 = customtkinter.StringVar()
 mystr37.set( "صيانة 18 شهر" )
 td37 = customtkinter.CTkEntry(sc2,textvariable=mystr37,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td37.grid(row=0,column=12)

 mystr38 = customtkinter.StringVar()
 mystr38.set( "رقم فاتورة الصيانة" )
 td38 = customtkinter.CTkEntry(sc2,textvariable=mystr38,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td38.grid(row=0,column=11)

 mystr39 = customtkinter.StringVar()
 mystr39.set( "هل تمت الصيانة" )
 td39 = customtkinter.CTkEntry(sc2,textvariable=mystr39,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td39.grid(row=0,column=10)

 mystr40 = customtkinter.StringVar()
 mystr40.set( "ملاحظات" )
 td40 = customtkinter.CTkEntry(sc2,textvariable=mystr40,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td40.grid(row=0,column=9)

 mystr41 = customtkinter.StringVar()
 mystr41.set( "صيانة 21 شهر" )
 td41 = customtkinter.CTkEntry(sc2,textvariable=mystr41,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td41.grid(row=0,column=8)

 mystr42 = customtkinter.StringVar()
 mystr42.set( "رقم فاتورة الصيانة" )
 td42= customtkinter.CTkEntry(sc2,textvariable=mystr42,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td42.grid(row=0,column=7)

 mystr43 = customtkinter.StringVar()
 mystr43.set( "هل تمت الصيانة" )
 td43 = customtkinter.CTkEntry(sc2,textvariable=mystr43,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td43.grid(row=0,column=6)

 mystr44 = customtkinter.StringVar()
 mystr44.set( "ملاحظات" )
 td44 = customtkinter.CTkEntry(sc2,textvariable=mystr44,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td44.grid(row=0,column=5)

 mystr45 = customtkinter.StringVar()
 mystr45.set( "صيانة 24 شهر" )
 td45 = customtkinter.CTkEntry(sc2,textvariable=mystr45,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#2071B0')
 td45.grid(row=0,column=4)

 mystr46 = customtkinter.StringVar()
 mystr46.set( "رقم فاتورة الصيانة" )
 td46 = customtkinter.CTkEntry(sc2,textvariable=mystr46,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td46.grid(row=0,column=3)

 mystr47 = customtkinter.StringVar()
 mystr47.set( "هل تمت الصيانة" )
 td47 = customtkinter.CTkEntry(sc2,textvariable=mystr47,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td47.grid(row=0,column=2)

 mystr48 = customtkinter.StringVar()
 mystr48.set( "ملاحظات" )
 td48= customtkinter.CTkEntry(sc2,textvariable=mystr48,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)+30),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td48.grid(row=0,column=1)



def select_all_db():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 c.execute("select * from siyana")
 data = c.fetchall()
 i = 48
 rol = 1
 
 for row in data:
   e0= customtkinter.CTkEntry(sc2,justify='left',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e0.grid(row=rol, column=i)
   e0.insert(END,(str(row[0])))
   i=i-1

   e1= customtkinter.CTkEntry(sc2,justify='left',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e1.grid(row=rol, column=i)
   e1.insert(END,(row[1]))
   i=i-1
   
   e2=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e2.grid(row=rol, column=i)
   e2.insert(END,row[2]) 
   i=i-1
   
   e3=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e3.grid(row=rol, column=i)
   e3.insert(END,row[3])
   i=i-1
   
   e4=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13)+30),border_width=0,font=mybutton_font,corner_radius=0)
   e4.grid(row=rol, column=i)
   e4.insert(END,row[4])
   i=i-1

   e5=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13)+30),border_width=0,font=mybutton_font,corner_radius=0)
   e5.grid(row=rol, column=i)
   e5.insert(END,row[5])
   i=i-1

   e6=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e6.grid(row=rol, column=i)
   e6.insert(END,row[6])
   i=i-1

   e7=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e7.grid(row=rol, column=i)
   e7.insert(END,row[7])
   i=i-1

   e8=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e8.grid(row=rol, column=i)
   e8.insert(END,row[8])
   i=i-1

   e9=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e9.grid(row=rol, column=i)
   e9.insert(END,row[9])
   i=i-1

   e10=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e10.grid(row=rol, column=i)
   e10.insert(END,row[10])
   i=i-1

   e11=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e11.grid(row=rol, column=i)
   e11.insert(END,row[11])
   i=i-1

   e12=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e12.grid(row=rol, column=i)
   e12.insert(END,row[12])
   i=i-1

   e13=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e13.grid(row=rol, column=i)
   e13.insert(END,row[13])
   i=i-1

   e14=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e14.grid(row=rol, column=i)
   e14.insert(END,row[14])
   i=i-1

   e15=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e15.grid(row=rol, column=i)
   e15.insert(END,row[15])
   i=i-1

   e16=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e16.grid(row=rol, column=i)
   e16.insert(END,row[16])
   i=i-1

   e17=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e17.grid(row=rol, column=i)
   e17.insert(END,row[17])
   i=i-1

   e18=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e18.grid(row=rol, column=i)
   e18.insert(END,row[18])
   i=i-1

   e19=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e19.grid(row=rol, column=i)
   e19.insert(END,row[19])
   i=i-1

   e20=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e20.grid(row=rol, column=i)
   e20.insert(END,row[20])
   i=i-1

   e21=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e21.grid(row=rol, column=i)
   e21.insert(END,row[21])
   i=i-1

   e22=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e22.grid(row=rol, column=i)
   e22.insert(END,row[22])
   i=i-1

   e23=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e23.grid(row=rol, column=i)
   e23.insert(END,row[23])
   i=i-1

   e24=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e24.grid(row=rol, column=i)
   e24.insert(END,row[24])
   i=i-1

   e25=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e25.grid(row=rol, column=i)
   e25.insert(END,row[25])
   i=i-1

   e26=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e26.grid(row=rol, column=i)
   e26.insert(END,row[26])
   i=i-1

   e27=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e27.grid(row=rol, column=i)
   e27.insert(END,row[27])
   i=i-1

   e28=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e28.grid(row=rol, column=i)
   e28.insert(END,row[28])
   i=i-1

   e29=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e29.grid(row=rol, column=i)
   e29.insert(END,row[29])
   i=i-1

   e30=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e30.grid(row=rol, column=i)
   e30.insert(END,row[30])
   i=i-1
   
   e31=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e31.grid(row=rol, column=i)
   e31.insert(END,row[31])
   i=i-1

   e32=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e32.grid(row=rol, column=i)
   e32.insert(END,row[32])
   i=i-1

   e33=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e33.grid(row=rol, column=i)
   e33.insert(END,row[33])
   i=i-1

   e34=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e34.grid(row=rol, column=i)
   e34.insert(END,row[34])
   i=i-1

   e35=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e35.grid(row=rol, column=i)
   e35.insert(END,row[35])
   i=i-1

   e36=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e36.grid(row=rol, column=i)
   e36.insert(END,row[36])
   i=i-1

   e37=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e37.grid(row=rol, column=i)
   e37.insert(END,row[37])
   i=i-1

   e38=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e38.grid(row=rol, column=i)
   e38.insert(END,row[38])
   i=i-1

   e39=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e39.grid(row=rol, column=i)
   e39.insert(END,row[39])
   i=i-1

   e40=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e40.grid(row=rol, column=i)
   e40.insert(END,row[40])
   i=i-1

   e41=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e41.grid(row=rol, column=i)
   e41.insert(END,row[41])
   i=i-1

   e42=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e42.grid(row=rol, column=i)
   e42.insert(END,row[42])
   i=i-1

   e43=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e43.grid(row=rol, column=i)
   e43.insert(END,row[43])
   i=i-1

   e44=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e44.grid(row=rol, column=i)
   e44.insert(END,row[44])
   i=i-1

   e45=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e45.grid(row=rol, column=i)
   e45.insert(END,row[45])
   i=i-1

   e46=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e46.grid(row=rol, column=i)
   e46.insert(END,row[46])
   i=i-1

   e47=customtkinter.CTkEntry(sc2,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e47.grid(row=rol, column=i)
   e47.insert(END,row[47])
   i=i-1
   rol = rol + 1
   i = 48
 conn.close()

def c8_comm():
 global sc2
 
 clear_frame(choose_frame)
 db_show_all()
 select_all_db()
 
 hscrollbar.pack( fill=X, side=BOTTOM)
 vscrollbar.pack( fill=Y, side=RIGHT)
 sc2.pack(fill = BOTH, expand = True)
 canvas.pack(side = LEFT, fill = BOTH, expand= True)
 canvas.create_window(0,0, window = sc2)
 frame.pack(expand = True, fill = BOTH)
 
 root.update_idletasks() # update geometry
 canvas.config(scrollregion = canvas.bbox("all"))
 canvas.xview_moveto(99999) 
 canvas.yview_moveto(0)


####   


first_row = ("السبب","نوع الضمان","رقم الهاتف 2","رقم الهاتف 1","موديل الجهاز","نوع الجهاز","تاريخ ف الشراء","رقم ف الشراء","اسم الفني","موقع العميل","اسم العميل","المهمة","امر الصيانة")
def print_daman():
 mystr1 = customtkinter.StringVar()
 mystr1.set( "امر الصيانة" )
 td1 = customtkinter.CTkEntry(hohols,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=0,column=13)

 mystr2 = customtkinter.StringVar()
 mystr2.set( "المهمة" )
 td2 = customtkinter.CTkEntry(hohols,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))-30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=0,column=12)
 
 mystr3 = customtkinter.StringVar()
 mystr3.set( "اسم العميل" )
 td3 = customtkinter.CTkEntry(hohols,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=0,column=11)

 mystr4 = customtkinter.StringVar()
 mystr4.set( "موقع العميل" )
 td4 = customtkinter.CTkEntry(hohols,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=0,column=10)

 mystr5 = customtkinter.StringVar()
 mystr5.set( "اسم الفني" )
 td5 = customtkinter.CTkEntry(hohols,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=0,column=9)

 mystr6 = customtkinter.StringVar()
 mystr6.set( "رقم ف الشراء" )
 td6 = customtkinter.CTkEntry(hohols,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=0,column=8)

 mystr7 = customtkinter.StringVar()
 mystr7.set( "تاريخ ف الشراء" )
 td7 = customtkinter.CTkEntry(hohols,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=0,column=7)
 
 mystr8 = customtkinter.StringVar()
 mystr8.set( "نوع الجهاز" )
 td8 = customtkinter.CTkEntry(hohols,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=0,column=6)
 
 mystr9 = customtkinter.StringVar()
 mystr9.set( "موديل الجهاز" )
 td9 = customtkinter.CTkEntry(hohols,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=0,column=5)
 
 mystr10 = customtkinter.StringVar()
 mystr10.set( "رقم الهاتف 1" )
 td10 = customtkinter.CTkEntry(hohols,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=0,column=4)

 mystr11 = customtkinter.StringVar()
 mystr11.set( "رقم الهاتف 2" )
 td11 = customtkinter.CTkEntry(hohols,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=0,column=3)

 mystr12 = customtkinter.StringVar()
 mystr12.set( "نوع الضمان" )
 td12 = customtkinter.CTkEntry(hohols,textvariable=mystr12,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td12.grid(row=0,column=2)

 mystr13 = customtkinter.StringVar()
 mystr13.set( "السبب" )
 td13 = customtkinter.CTkEntry(hohols,textvariable=mystr13,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))+30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td13.grid(row=0,column=1)

def hoversing(d=""):
 ggg = getvalueop_daman.get() 
 getvalueop_daman.set(revers_words(ggg)) 
def taqrir_naw3_daman_1():
 refresh_db()

 frame_ism_mawqi3_1 = Frame(root,padx=10,pady=10)
 logout = customtkinter.CTkButton(frame_ism_mawqi3_1,fg_color='#F02849',text="عودة",font=mybutton_font,command=lambda :first_win(True,frame_ism_mawqi3_1))
 tiba3a = customtkinter.CTkButton(frame_ism_mawqi3_1,text="طباعة",font=mybutton_font)
 searchv = customtkinter.CTkButton(frame_ism_mawqi3_1,text="عرض النتائج",command=taqrir_naw3_daman_db,font=mybutton_font)

 global getvalueop_daman
 getvalueop_daman = customtkinter.StringVar()
 getvalueop_daman.set("داخل الضمان")
 optionss = customtkinter.CTkOptionMenu(frame_ism_mawqi3_1,corner_radius=0,font=mybutton_font,command=hoversing,variable=getvalueop_daman,
  values=[revers_words("داخل الضمان"),revers_words("خارج الضمان")])


 optionss.grid(row=1, column=4,pady=10,ipady=5)
 logout.grid(row=1, column=0,padx=10, pady=10,ipady=5)
 tiba3a.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 searchv.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 frame_ism_mawqi3_1.pack(padx=10, pady=10)
 
 print_daman()

def taqrir_naw3_daman_db():
 
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 v1 = getvalueop_daman.get()
 sql = """naw3_siyana,mohima,ism_3amil,mawqi3_3amil,ism_fani,raqm_fatora_chira,
           tarikh_fatora_chira,naw3_jihaz,modil_jihaz,phone_number1,phone_number2,naw3_daman,sabab"""

 c.execute("""SELECT """+sql+""" FROM siyana WHERE naw3_daman=? """, (v1,))

 rows = c.fetchall()
 i = 13
 rol = 1
 for widget in hohols.winfo_children():
   widget.destroy()
 print_daman()
 
 
 if(len(rows)!=0):
  nti0.set("")
  for row in rows:
   e1= customtkinter.CTkEntry(hohols,justify='left',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e1.grid(row=rol, column=i)
   e1.insert(END,(row[0]))
   i=i-1
   
   e2=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)-30),border_width=0,font=mybutton_font,corner_radius=0)
   e2.grid(row=rol, column=i)
   e2.insert(END,row[1]) 
   i=i-1
   
   e3=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e3.grid(row=rol, column=i)
   e3.insert(END,row[2])
   i=i-1
   
   e4=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e4.grid(row=rol, column=i)
   e4.insert(END,row[3])
   i=i-1
   
   e5=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e5.grid(row=rol, column=i)
   e5.insert(END,row[4]) 
   
   i=i-1
   e6=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e6.grid(row=rol, column=i)
   e6.insert(END,row[5])
  
   i=i-1
   e7=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e7.grid(row=rol, column=i)
   e7.insert(END,row[6])
   
   i=i-1
   e8=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e8.grid(row=rol, column=i)
   e8.insert(END,row[7])
   
   i=i-1
   e9=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e9.grid(row=rol, column=i)
   e9.insert(END,row[8]) 
   i=i-1
   
   e10=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e10.grid(row=rol, column=i)
   e10.insert(END,row[9])
   
   i=i-1
   e11=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e11.grid(row=rol, column=i)
   e11.insert(END,row[10])
   
   i=i-1
   e12=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13)),border_width=0,font=mybutton_font,corner_radius=0)
   e12.grid(row=rol, column=i)
   e12.insert(END,row[11])
   
   i=i-1
   e13=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/13))+30,border_width=0,font=mybutton_font,corner_radius=0)
   e13.grid(row=rol, column=i)
   e13.insert(END,row[12])
   
   i=i-1
   i = 13
   rol = rol + 1
 else:
  for widget in hohols.winfo_children():
   widget.destroy()
  print_daman()
  hohols.configure(height=0)
  nti0.set("لايوجد نتائج")

 
 
def c7_comm():
 global hoholv
 global hohols
 clear_frame(choose_frame)
 root.state("zoomed")
 root.resizable(width=True, height=True)
 hohols = customtkinter.CTkScrollableFrame(root,width=width_sc-20,height=height_sc-20,fg_color="transparent")
 taqrir_naw3_daman_1()
 hohols.pack()
 
 global frmsgg,nti0
 frmsgg = Frame(root,pady=10)
 nti0= customtkinter.StringVar()
 vvvd = customtkinter.CTkLabel(frmsgg,bg_color='transparent',font=("Times New Roman", 19, "bold"),textvariable=nti0)
 vvvd.grid(row=0, column=0)
 frmsgg.pack()


##



def print_fatra0():
 mystr1 = customtkinter.StringVar()
 mystr1.set( "امر الصيانة" )
 td1 = customtkinter.CTkEntry(hohols,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11))+10,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=0,column=11)

 mystr2 = customtkinter.StringVar()
 mystr2.set( "مهمة" )
 td2 = customtkinter.CTkEntry(hohols,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11))-30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=0,column=10)
 
 mystr3 = StringVar()
 mystr3.set( "اسم العميل" )
 td3 = customtkinter.CTkEntry(hohols,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=0,column=9)

 mystr4 = StringVar()
 mystr4.set( "موقع العميل" )
 td4 = customtkinter.CTkEntry(hohols,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=0,column=8)

 mystr5 = StringVar()
 mystr5.set( "اسم الفني" )
 td5 = customtkinter.CTkEntry(hohols,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=0,column=7)

 mystr6 = StringVar()
 mystr6.set( "رقم فاتورة الشراء" )
 td6 = customtkinter.CTkEntry(hohols,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=0,column=6)

 mystr7 = StringVar()
 mystr7.set( "تاريخ فاتورة الشراء" )
 td7 = customtkinter.CTkEntry(hohols,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=0,column=5)
 
 mystr8 = StringVar()
 mystr8.set( "نوع الجهاز" )
 td8 = customtkinter.CTkEntry(hohols,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=0,column=4)
 
 mystr9 = StringVar()
 mystr9.set( "موديل الجهاز" )
 td9 = customtkinter.CTkEntry(hohols,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=0,column=3)
 
 mystr10 = StringVar()
 mystr10.set( "رقم الهاتف 1" )
 td10 = customtkinter.CTkEntry(hohols,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=0,column=2)

 mystr11 = StringVar()
 mystr11.set( "رقم الهاتف 2" )
 td11 = customtkinter.CTkEntry(hohols,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=0,column=1)


def taqrir_bil_fatra():
 taqrir_bil_fatra_1 = Frame(root,padx=10,pady=10)
 logout = customtkinter.CTkButton(taqrir_bil_fatra_1,fg_color='#F02849',text="عودة",font=mybutton_font,command=lambda :first_win(True,taqrir_bil_fatra_1))
 tiba3a = customtkinter.CTkButton(taqrir_bil_fatra_1,text="طباعة",font=mybutton_font,)
 searchv = customtkinter.CTkButton(taqrir_bil_fatra_1,text="عرض النتائج",command=ard_nataij_bydate,font=mybutton_font)
 
 global getfirst_date,getsecond_date
 getfirst_date = customtkinter.StringVar()
 getsecond_date = customtkinter.StringVar()
 
 mien = customtkinter.CTkLabel(taqrir_bil_fatra_1,text=" : من     ",font=mybutton_font)
 ila = customtkinter.CTkLabel(taqrir_bil_fatra_1,text="  :  الى     ",font=mybutton_font)
 
 first_date = customtkinter.CTkEntry(taqrir_bil_fatra_1,textvariable=getfirst_date,font=mybutton_font) ##get this 
 second_date = customtkinter.CTkEntry(taqrir_bil_fatra_1,textvariable=getsecond_date,font=mybutton_font) ##get this 
 getsecond_date.set(datetime.datetime.now().strftime("%d/%m/20%y"))
 getfirst_date.set(datetime.datetime.now().strftime("01/%m/20%y"))

 logout.grid(row=1, column=0,padx=10, pady=10,ipady=5)
 tiba3a.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 searchv.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 second_date.grid(row=1,column=3,pady=10,ipady=5) 
 ila.grid(row=1,column=4,pady=10,ipady=5) 
 first_date.grid(row=1, column=5,pady=10,ipady=5)
 mien.grid(row=1,column=6,pady=10,ipady=5) 
 taqrir_bil_fatra_1.pack(padx=10, pady=10)
 print_fatra0()

def ard_nataij_bydate():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 v2 = getsecond_date.get()
 v1 = getfirst_date.get()
 
 y1 = int(v1.split("/")[-1])
 m1 = int(v1.split("/")[1])
 d1 = int(v1.split("/")[0])

 y2 = int(v2.split("/")[-1])
 m2 = int(v2.split("/")[1])
 d2 = int(v2.split("/")[0])
 middleyears = []
 all2=[]
 sames=[]

 if(y1 != y2):
  second_middlemounths = []
  if(y2>y1):
   for i in range(y1+1,y2):
    middleyears.append("%"+str(i)+"%")
  else:
    print("y2<y1 !!!!!!")
  for im in range(m1+1,13):
   middleyears.append("%"+str(im)+"/"+str(y1)+"%")
  for im2 in range(1,m2):
   second_middlemounths.append(im2)
   middleyears.append("%"+str(im2)+"/"+str(y2)+"%")

  for idd in range(d1,32):
   if(int(m1)<10):
    middleyears.append("%"+str(idd)+"/0"+str(m1)+"/"+str(y1)+"%")
   else:
    middleyears.append("%"+str(idd)+"/"+str(m1)+"/"+str(y1)+"%")

  for id2 in range(1,d2+1):
   if(int(second_middlemounths[-1])<10):
    middleyears.append("%"+str(id2)+"/0"+str(second_middlemounths[-1]+1)+"/"+str(y2)+"%")
   else:
    middleyears.append("%"+str(id2)+"/"+str(second_middlemounths[-1]+1)+"/"+str(y2)+"%")

 if(y1 == y2 and m1==m2):
  for i in range(d1,d2+1):
   if(m1<10):
    sames.append("%"+str(i)+"/0"+str(m1)+"/"+str(y1)+"%")
   else:
    sames.append("%"+str(i)+"/"+str(m1)+"/"+str(y1)+"%")
 if(y1 == y2 and m1!=m2):
  for im2 in range(m1+1,m2):
   all2.append("%"+str(im2)+"/"+str(y1)+"%")
  for d1 in range(d1,32):
   if(m1<10):
    all2.append("%"+str(d1)+"/0"+str(m1)+"/"+str(y1)+"%") 
   else:
    all2.append("%"+str(d1)+"/"+str(m1)+"/"+str(y1)+"%") 
  for dd2 in range(1,d2+1):
   if(m2<10):
    all2.append("%"+str(dd2)+"/0"+str(m2)+"/"+str(y1)+"%") 
   else:
    all2.append("%"+str(dd2)+"/"+str(m2)+"/"+str(y1)+"%") 
 
 data = ()
 sqls=""
 
 q="""naw3_siyana,mohima,ism_3amil,mawqi3_3amil,ism_fani,raqm_fatora_chira,tarikh_fatora_chira,naw3_jihaz,modil_jihaz,phone_number1,phone_number2"""
 if(len(middleyears)!=0):
  sqls = "SELECT "+q+" FROM siyana WHERE date "+"LIKE (?) or date "*(len(middleyears))
  sqls = sqls[0:-8]
  data = str( tuple(middleyears)).replace(")","").replace("(","").replace("'",'')
  data= str(tuple(map(str,data.split(', ')))).replace(")",",)")
 if(len(all2)!=0):
  sqls = "SELECT "+q+" FROM siyana WHERE date "+"LIKE (?) or date "*len(all2)
  sqls = sqls[0:-8]
  data = str( tuple(all2)).replace(")","").replace("(","").replace("'",'')
  data= str(tuple(map(str,data.split(', ')))).replace(")",",)")
 if(len(sames)!=0):
  sqls = "SELECT "+q+" FROM siyana WHERE date "+"LIKE (?) or date "*len(sames)
  sqls = sqls[0:-8]
  data = str( tuple(sames)).replace(")","").replace("(","").replace("'",'')
  data= str(tuple(map(str,data.split(', ')))).replace(")",",)")
 if(y1 == y2 and m1==m2 and d1==d2):
  sqls = "SELECT "+q+" FROM siyana WHERE date LIKE (?)"
  data = "('%"+str(v1)+"%'"+',)'
  
 eval("c.execute(\""+sqls+"\","+data+")")
 rowse = c.fetchall()

 for widget in hohols.winfo_children():
  widget.destroy()
 print_fatra0()

 i = 11
 rol = 1
 if(len(rowse)!=0):
  nti0.set("")
  for row in rowse:
   e1= customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11))+10,border_width=0,font=mybutton_font,corner_radius=0)
   e1.grid(row=rol, column=i)
   e1.insert(END,row[0]) 
   i=i-1
   e2=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)-30),border_width=0,font=mybutton_font,corner_radius=0)
   e2.grid(row=rol, column=i)
   e2.insert(END,row[1]) 
   i=i-1
   e3=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e3.grid(row=rol, column=i)
   e3.insert(END,row[2])
   i=i-1
   e4=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e4.grid(row=rol, column=i)
   e4.insert(END,row[3])
   i=i-1
   e5=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e5.grid(row=rol, column=i)
   e5.insert(END,row[4]) 
   i=i-1
   e6=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e6.grid(row=rol, column=i)
   e6.insert(END,row[5])
   i=i-1
   e7=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e7.grid(row=rol, column=i)
   e7.insert(END,row[6]) 
   i=i-1
   e8=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e8.grid(row=rol, column=i)
   e8.insert(END,row[7])
   i=i-1
   e9=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e9.grid(row=rol, column=i)
   e9.insert(END,row[8]) 
   i=i-1
   e10=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e10.grid(row=rol, column=i)
   e10.insert(END,row[9])
   i=i-1
   e11=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e11.grid(row=rol, column=i)
   e11.insert(END,row[10])
   i=i-1
   i = 11
   rol = rol + 1
 else:
  for widget in hohols.winfo_children():
   widget.destroy()
  print_fatra0()
  hohols.configure(height=0)
  nti0.set("لايوجد نتائج")
  
  
def c6_comm():

 global hohols
 clear_frame(choose_frame)
 root.state("zoomed")
 root.resizable(width=True, height=True)
 hohols = customtkinter.CTkScrollableFrame(root,width=width_sc-20,height=height_sc-20,fg_color="transparent")
 taqrir_bil_fatra()
 hohols.pack()
 global frmsgg,nti0
 frmsgg = Frame(root,pady=10)
 nti0= customtkinter.StringVar()
 vvvd = customtkinter.CTkLabel(frmsgg,bg_color='transparent',font=("Times New Roman", 19, "bold"),textvariable=nti0)
 vvvd.grid(row=0, column=0)
 frmsgg.pack()


##


def print_ism_mawq():
 mystr1 = customtkinter.StringVar()
 mystr1.set( "امر الصيانة" )
 td1 = customtkinter.CTkEntry(hohols,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11))+10,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=0,column=11)

 mystr2 = customtkinter.StringVar()
 mystr2.set( "مهمة" )
 td2 = customtkinter.CTkEntry(hohols,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11))-30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=0,column=10)
 
 mystr3 = customtkinter.StringVar()
 mystr3.set( "اسم العميل" )
 td3 = customtkinter.CTkEntry(hohols,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=0,column=9)

 mystr4 = customtkinter.StringVar()
 mystr4.set( "موقع العميل" )
 td4 = customtkinter.CTkEntry(hohols,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=0,column=8)

 mystr5 = customtkinter.StringVar()
 mystr5.set( "اسم الفني" )
 td5 = customtkinter.CTkEntry(hohols,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=0,column=7)

 mystr6 = customtkinter.StringVar()
 mystr6.set( "رقم فاتورة الشراء" )
 td6 = customtkinter.CTkEntry(hohols,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=0,column=6)

 mystr7 = customtkinter.StringVar()
 mystr7.set( "تاريخ فاتورة الشراء" )
 td7 = customtkinter.CTkEntry(hohols,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=0,column=5)
 
 mystr8 = customtkinter.StringVar()
 mystr8.set( "نوع الجهاز" )
 td8 = customtkinter.CTkEntry(hohols,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=0,column=4)
 
 mystr9 = customtkinter.StringVar()
 mystr9.set( "موديل الجهاز" )
 td9 = customtkinter.CTkEntry(hohols,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=0,column=3)
 
 mystr10 = customtkinter.StringVar()
 mystr10.set( "رقم الهاتف 1" )
 td10 = customtkinter.CTkEntry(hohols,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=0,column=2)

 mystr11 = customtkinter.StringVar()
 mystr11.set( "رقم الهاتف 2" )
 td11 = customtkinter.CTkEntry(hohols,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=0,column=1)


def print_getvalueop_mawqi3(sdcgb=''):
 trv = revers_words(getvalueop_mawqi3.get())
 getvalueop_mawqi3.set(trv)

def taqrir_ism_mawqi3():
 frame_ism_mawqi3_1 = Frame(root,padx=10,pady=10)
 logout = customtkinter.CTkButton(frame_ism_mawqi3_1,fg_color='#F02849',text="عودة",font=mybutton_font,command=lambda :first_win(True,frame_ism_mawqi3_1))
 tiba3a = customtkinter.CTkButton(frame_ism_mawqi3_1,text="طباعة",font=mybutton_font)
 searchv = customtkinter.CTkButton(frame_ism_mawqi3_1,text="عرض النتائج",command=ard_nataij_mawqi3,font=mybutton_font)

 global getvalueop_mawqi3
 getvalueop_mawqi3 = customtkinter.StringVar()
 getvalueop_mawqi3.set('المهرجان')
 optionss = customtkinter.CTkComboBox(frame_ism_mawqi3_1,corner_radius=0,command=print_getvalueop_mawqi3,font=mybutton_font,variable=getvalueop_mawqi3,
  values=[revers_words("المهرجان"),revers_words("السليمانية"),revers_words("الخالدية")
   ,revers_words("الفيصلية"),revers_words("سلطانه"),revers_words("الورود")
   ,revers_words("المروج"),revers_words("السلمان")
   ,revers_words("السلام"),revers_words("القادسيه"),revers_words("البوادي")
   ,revers_words("السبيع"),revers_words("المنتزه"),revers_words("الحمرا")
   ,revers_words("ط.المدينة"),revers_words("م.العسكريه"),revers_words("ق.الجويه")
   ,revers_words("ط.عمان"),revers_words("الجديده"),revers_words("الاندلس")
   ,revers_words("العرجان"),revers_words("مروج الامير"),revers_words("النظيم")
   ,revers_words("كريم"),revers_words("الرابيه"),revers_words("الصفا")
   ,revers_words("الاخضر"),revers_words("النهضه"),revers_words("السعاده")
   ,revers_words("ابو سبعه"),revers_words("العليا"),revers_words("قرطبه")
   ,revers_words("المصيف"),revers_words("النخيل"),revers_words("دمج")
   ,revers_words("الجزيره"),revers_words("الدخل"),revers_words("العزيزيه")
   ,revers_words("الاسكان"),revers_words("الاشرفيه"),revers_words("الهضيبه")
   ,revers_words("الضلفه"),revers_words("ضباء"),revers_words("حقل")
   ,revers_words("شقري"),revers_words("العلا"),revers_words("البدع")
   ,revers_words("البير"),revers_words("العيينه"),revers_words("تيماء")
   ,revers_words("الوجه"),revers_words("القليبه"),revers_words("الشفا")
   ,revers_words("الصالحيه"),revers_words("السعيدات"),revers_words("الرويعيات")
   ,revers_words("البساتين"),revers_words("رايس"),revers_words("الراجحي")
   ,revers_words("الراقي"),revers_words("اليرموك"),revers_words("الرواد")
   ,revers_words("الديسه"),revers_words("الروضه"),revers_words("النسيم")
   ,revers_words("المزارع"),revers_words("ابوراكه"),revers_words("شواق")
   ,revers_words("الحره"),revers_words("البر"),revers_words("الصناعيه")
   ,revers_words("الريان"),revers_words("البريكه"),revers_words("غرناطه")
   ,revers_words("خ.المدينه"),"الجمرك","الواحه"
   ,"باركمول","رحيل","الجامعه"
   ,"مجهول","التعاون","الصوامع"
   ,"الجوازات","القدس",revers_words("سنابل مول")
   ,"المدرعات",revers_words("دوار الرمانة")
   ])

 optionss.grid(row=1, column=4,pady=10,ipady=5)
 logout.grid(row=1, column=0,padx=10, pady=10,ipady=5)
 tiba3a.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 searchv.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 frame_ism_mawqi3_1.pack(padx=10, pady=10)
 
 print_ism_mawq()
 

def ard_nataij_mawqi3():
 
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 v1 = getvalueop_mawqi3.get()
 sql = """naw3_siyana,mohima,ism_3amil,mawqi3_3amil,ism_fani,raqm_fatora_chira,
           tarikh_fatora_chira,naw3_jihaz,modil_jihaz,phone_number1,phone_number2"""

 c.execute("""SELECT """+sql+""" FROM siyana WHERE mawqi3_3amil=? """, (v1,))

 rows = c.fetchall()
 i = 11
 rol = 1
 
 if(len(rows)!=0):
  nti0.set("")
  for row in rows:
   e1= customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11))+10,border_width=0,font=mybutton_font,corner_radius=0)
   e1.grid(row=rol, column=i)
   e1.insert(END,row[0]) 
   i=i-1
   e2=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)-30),border_width=0,font=mybutton_font,corner_radius=0)
   e2.grid(row=rol, column=i)
   e2.insert(END,row[1]) 
   i=i-1
   e3=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e3.grid(row=rol, column=i)
   e3.insert(END,row[2])
   i=i-1
   e4=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e4.grid(row=rol, column=i)
   e4.insert(END,row[3])
   i=i-1
   e5=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e5.grid(row=rol, column=i)
   e5.insert(END,row[4]) 
   i=i-1
   e6=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e6.grid(row=rol, column=i)
   e6.insert(END,row[5])
   i=i-1
   e7=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e7.grid(row=rol, column=i)
   e7.insert(END,row[6]) 
   i=i-1
   e8=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e8.grid(row=rol, column=i)
   e8.insert(END,row[7])
   i=i-1
   e9=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e9.grid(row=rol, column=i)
   e9.insert(END,row[8]) 
   i=i-1
   e10=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e10.grid(row=rol, column=i)
   e10.insert(END,row[9])
   i=i-1
   e11=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e11.grid(row=rol, column=i)
   e11.insert(END,row[10])
   i=i-1
   i = 11
   rol = rol + 1
 else:
  for widget in hohols.winfo_children():
   widget.destroy()
  print_ism_mawq()
  hohols.configure(height=0)
  nti0.set("لايوجد نتائج")
  
def c5_comm():
 global hohols
 clear_frame(choose_frame)
 root.state("zoomed")
 root.resizable(width=True, height=True)
 hohols = customtkinter.CTkScrollableFrame(root,width=width_sc-20,height=height_sc-20,fg_color="transparent")
 taqrir_ism_mawqi3()
 hohols.pack()
 
 global frmsgg,nti0
 frmsgg = Frame(root,pady=10)
 nti0= customtkinter.StringVar()
 vvvd = customtkinter.CTkLabel(frmsgg,bg_color='transparent',font=("Times New Roman", 19, "bold"),textvariable=nti0)
 vvvd.grid(row=0, column=0)
 frmsgg.pack()



##


def print_ism3amil():
 mystr1 = customtkinter.StringVar()
 mystr1.set( "امر الصيانة" )
 td1 = customtkinter.CTkEntry(hohols,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11))+10,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=0,column=11)

 mystr2 = customtkinter.StringVar()
 mystr2.set( "مهمة" )
 td2 = customtkinter.CTkEntry(hohols,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11))-30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=0,column=10)
 
 mystr3 = customtkinter.StringVar()
 mystr3.set( "اسم العميل" )
 td3 = customtkinter.CTkEntry(hohols,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=0,column=9)

 mystr4 = customtkinter.StringVar()
 mystr4.set( "موقع العميل" )
 td4 = customtkinter.CTkEntry(hohols,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=0,column=8)

 mystr5 = customtkinter.StringVar()
 mystr5.set( "اسم الفني" )
 td5 = customtkinter.CTkEntry(hohols,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=0,column=7)

 mystr6 = customtkinter.StringVar()
 mystr6.set( "رقم فاتورة الشراء" )
 td6 = customtkinter.CTkEntry(hohols,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=0,column=6)

 mystr7 = customtkinter.StringVar()
 mystr7.set( "تاريخ فاتورة الشراء" )
 td7 = customtkinter.CTkEntry(hohols,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=0,column=5)
 
 mystr8 = customtkinter.StringVar()
 mystr8.set( "نوع الجهاز" )
 td8 = customtkinter.CTkEntry(hohols,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=0,column=4)
 
 mystr9 = customtkinter.StringVar()
 mystr9.set( "موديل الجهاز" )
 td9 = customtkinter.CTkEntry(hohols,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=0,column=3)
 
 mystr10 = customtkinter.StringVar()
 mystr10.set( "رقم الهاتف 1" )
 td10 = customtkinter.CTkEntry(hohols,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=0,column=2)

 mystr11 = customtkinter.StringVar()
 mystr11.set( "رقم الهاتف 2" )
 td11 = customtkinter.CTkEntry(hohols,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/11)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=0,column=1)

def rever_ism_3aml(sdc=''):
 rt = revers_words(getvalueop.get())
 getvalueop.set(rt)

def taqrir_ism_3amil_1():
 frame_ism_3amil_1 = Frame(root,padx=10,pady=10)
 logout = customtkinter.CTkButton(frame_ism_3amil_1,fg_color='#F02849',text="عودة",font=mybutton_font,command=lambda :first_win(True,frame_ism_3amil_1))
 tiba3a = customtkinter.CTkButton(frame_ism_3amil_1,text="طباعة",font=mybutton_font,)
 searchv = customtkinter.CTkButton(frame_ism_3amil_1,text="عرض النتائج",command=ard_nataij,font=mybutton_font)
 
 global getvalueop,entr_usr
 getvalueop = customtkinter.StringVar()
 getvalueop.set('تقرير باسم العميل')
 optionss = customtkinter.CTkOptionMenu(frame_ism_3amil_1,command=rever_ism_3aml,corner_radius=0,font=mybutton_font,variable=getvalueop,values=[
  revers_words("تقرير باسم العميل"),revers_words("تقرير برقم الهاتف"),
  revers_words("تقرير برقم الفاتورة")])

 entr_usr = customtkinter.CTkEntry(frame_ism_3amil_1,font=mybutton_font,corner_radius=0,justify='right') ##get this 
 
 optionss.grid(row=1, column=4,pady=10,ipady=5)
 logout.grid(row=1, column=0,padx=10, pady=10,ipady=5)
 tiba3a.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 searchv.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 entr_usr.grid(row=1,column=3,pady=10,ipady=5) 
 frame_ism_3amil_1.pack(padx=10, pady=10)
 print_ism3amil()
 

def ard_nataij():
 
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 v1 = getvalueop.get()
 v2 = entr_usr.get()
 sql = """naw3_siyana,mohima,ism_3amil,mawqi3_3amil,ism_fani,raqm_fatora_chira,
           tarikh_fatora_chira,naw3_jihaz,modil_jihaz,phone_number1,phone_number2"""
 if(v1=="تقرير باسم العميل"):
  c.execute("""SELECT """+sql+""" FROM siyana WHERE ism_3amil=? """, (v2,))
 if(v1=="تقرير برقم الهاتف"):
  c.execute("""SELECT """+sql+""" FROM siyana WHERE phone_number1=? or phone_number2=?""", (v2,v2,))
 if(v1=="تقرير برقم الفاتورة"):
  c.execute("""SELECT """+sql+""" FROM siyana WHERE raqm_fatora_chira=? """, (v2,))
 
 rows = c.fetchall()
 i = 11
 rol = 1
 if(len(rows)!=0):
  nti0.set("")
  for row in rows:
   e1= customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11))+10,border_width=0,font=mybutton_font,corner_radius=0)
   e1.grid(row=rol, column=i)
   e1.insert(END,row[0]) 
   i=i-1
   e2=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)-30),border_width=0,font=mybutton_font,corner_radius=0)
   e2.grid(row=rol, column=i)
   e2.insert(END,row[1]) 
   i=i-1
   e3=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e3.grid(row=rol, column=i)
   e3.insert(END,row[2])
   i=i-1
   e4=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e4.grid(row=rol, column=i)
   e4.insert(END,row[3])
   i=i-1
   e5=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e5.grid(row=rol, column=i)
   e5.insert(END,row[4]) 
   i=i-1
   e6=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e6.grid(row=rol, column=i)
   e6.insert(END,row[5])
   i=i-1
   e7=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e7.grid(row=rol, column=i)
   e7.insert(END,row[6]) 
   i=i-1
   e8=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e8.grid(row=rol, column=i)
   e8.insert(END,row[7])
   i=i-1
   e9=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e9.grid(row=rol, column=i)
   e9.insert(END,row[8]) 
   i=i-1
   e10=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e10.grid(row=rol, column=i)
   e10.insert(END,row[9])
   i=i-1
   e11=customtkinter.CTkEntry(hohols,justify='right',width=int((width_sc/11)),border_width=0,font=mybutton_font,corner_radius=0)
   e11.grid(row=rol, column=i)
   e11.insert(END,row[10])
   i=i-1
   i = 11
   rol = rol + 1
 else:
  for widget in hohols.winfo_children():
   widget.destroy()
  print_ism3amil()
  hohols.configure(height=0)
  nti0.set("لايوجد نتائج")
  

def c4_comm():
 global hohols
 clear_frame(choose_frame)
 root.state("zoomed")
 root.resizable(width=True, height=True)
 hohols = customtkinter.CTkScrollableFrame(root,width=width_sc-20,height=height_sc-20,fg_color="transparent")
 taqrir_ism_3amil_1()
 hohols.pack()

 global frmsgg,nti0
 frmsgg = Frame(root,pady=10)
 nti0= customtkinter.StringVar()
 vvvd = customtkinter.CTkLabel(frmsgg,bg_color='transparent',font=("Times New Roman", 19, "bold"),textvariable=nti0)
 vvvd.grid(row=0, column=0)
 frmsgg.pack()

#


def print_siyana_dawriya():
 mystr1 = customtkinter.StringVar()
 mystr1.set( "رقم" )
 td1 = customtkinter.CTkEntry(hohol,textvariable=mystr1,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/13))-40,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td1.grid(row=0,column=11)

 mystr2 = customtkinter.StringVar()
 mystr2.set( "اسم العميل" )
 td2 = customtkinter.CTkEntry(hohol,textvariable=mystr2,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12))-30,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td2.grid(row=0,column=10)
 
 mystr3 = customtkinter.StringVar()
 mystr3.set( "موقع العميل" )
 td3 = customtkinter.CTkEntry(hohol,textvariable=mystr3,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td3.grid(row=0,column=9)

 mystr4 = customtkinter.StringVar()
 mystr4.set( "رقم فاتورة الشراء" )
 td4 = customtkinter.CTkEntry(hohol,textvariable=mystr4,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12))+10,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td4.grid(row=0,column=8)

 mystr5 = customtkinter.StringVar()
 mystr5.set( "تاريخ فاتورة الشراء" )
 td5 = customtkinter.CTkEntry(hohol,textvariable=mystr5,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12))+20,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td5.grid(row=0,column=7)

 mystr6 = customtkinter.StringVar()
 mystr6.set( "نوع الجهاز" )
 td6 = customtkinter.CTkEntry(hohol,textvariable=mystr6,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td6.grid(row=0,column=6)

 mystr7 = customtkinter.StringVar()
 mystr7.set( "موديل الجهاز" )
 td7 = customtkinter.CTkEntry(hohol,textvariable=mystr7,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td7.grid(row=0,column=5)
 
 mystr8 = customtkinter.StringVar()
 mystr8.set( "رقم الهاتف 1" )
 td8 = customtkinter.CTkEntry(hohol,textvariable=mystr8,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td8.grid(row=0,column=4)
 
 mystr9 = customtkinter.StringVar()
 mystr9.set( "رقم الهاتف 2" )
 td9 = customtkinter.CTkEntry(hohol,textvariable=mystr9,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td9.grid(row=0,column=3)
 
 mystr10 = customtkinter.StringVar()
 mystr10.set( "نوع الصيانة" )
 td10 = customtkinter.CTkEntry(hohol,textvariable=mystr10,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td10.grid(row=0,column=2)

 mystr11 = customtkinter.StringVar()
 mystr11.set( "تاريخ الصيانة" )
 td11 = customtkinter.CTkEntry(hohol,textvariable=mystr11,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12)),justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td11.grid(row=0,column=1)

 mystr12 = customtkinter.StringVar()
 mystr12.set( "رقم فاتورة الصيانة" )
 td12 = customtkinter.CTkEntry(hohol,textvariable=mystr12,border_width=0,corner_radius=0,state='disabled',width=int((width_sc/12))+20,justify='center',font=mybutton_font,text_color='white',fg_color='#21B000')
 td12.grid(row=0,column=0)

def search_by_input(dd=False):
 if(dd==False):
  data = str(getmounths.get().replace("الشهر ",'').replace(" ",""))+'/'+str(getyears.get())
 if(dd==True):
  data = str(datetime.datetime.now().strftime("%m"))[-1:]+'/20'+str(datetime.datetime.now().strftime("%y"))
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 sqq  ="""SELECT tarikh_fatora_chira from siyana where siyana__chahr_3 LIKE (?) or siyana__chahr_6 LIKE (?) or
  siyana__chahr_9 LIKE (?) or siyana__chahr_12 LIKE (?) or siyana__chahr_15 LIKE (?) or 
  siyana__chahr_18 LIKE (?) or siyana__chahr_21 LIKE (?) or siyana__chahr_24 LIKE (?)"""
 c.execute(sqq, ("%"+data+"%","%"+data+"%","%"+data+"%","%"+data+"%","%"+data+"%","%"+data+"%"
  "%"+data+"%","%"+data+"%","%"+data+"%",))
 rows1 = c.fetchall()

 for widget in hohol.winfo_children():
  widget.destroy()
 print_siyana_dawriya()
 my_mounths = []
 all_mounths = 0
 for i in rows1:
  mounth1 = int(str(i[0]).split('/')[1])
  year1 = int(str(i[0]).split('/')[2])
  tarikh_fatora = str(mounth1)+'/'+str(year1)
  mounth2 = int(str(data).split('/')[0])
  year2 = int(str(data).split('/')[1])
  if(year1==year2):
   my_mounths.append(str(mounth2-mounth1))
   all_mounths = all_mounths + (mounth2-mounth1)
  else:
   m1 =mounth1
   y1 =year1
   m2 =mounth2
   y2 =year2
   for i1 in range(m1,13):
    all_mounths = all_mounths + 1
   for i2 in range(y1+1,y2+1):
    if(i2!=y2):
     for i3 in range(1,13):
      all_mounths = all_mounths + 1
    else:
     for i4 in range(1,m2+1):
      all_mounths = all_mounths + 1
    all_mounths = all_mounths - 1
    my_mounths.append(all_mounths)

 rows = []
 iy = 0
 for infos in my_mounths:
  dd = """id,ism_3amil,mawqi3_3amil,raqm_fatora_chira,tarikh_fatora_chira,naw3_jihaz,modil_jihaz,phone_number1,phone_number2,"""
  ssq = """SELECT """+dd+"""siyana__chahr_"""+str(infos)+""" ,raq_fatorat_siyana_"""+str(infos)+""" FROM siyana WHERE siyana__chahr_"""+str(infos)+""" LIKE (?)"""
  c.execute(ssq,("%"+data+"%" ,))
  for ik in c.fetchall():
   ret = np.asarray(ik+(str(infos),))
   v3 = ret[-3]
   v2 = ret[-2]
   v1 = ret[-1]
  
   ret[-1] = v3
   ret[-2] = v2
   ret[-3] = v1

   ret[-2]=v3
   ret[-1]=v2
   rows.append(tuple(ret))
  iy = iy + 1
 rowss = set(rows)
 if(len(rowss)!=0):
  nti0.set("")
  create_my_table(1,11,rowss,hohol)
 else:
  for widget in hohol.winfo_children():
   widget.destroy()
  print_siyana_dawriya()
  hohol.configure(height=0)
  nti0.set("لايوجد نتائج")

 conn.close()


def rever_prints(r=""):
 ff = revers_words(getmounths.get())
 getmounths.set(ff)
def taqrir_siyana_dawriya_1():
 siyandawriyaframe = Frame(root,padx=10,pady=10,border=0)
 logout = customtkinter.CTkButton(siyandawriyaframe,fg_color='#F02849',font=mybutton_font,text="عودة",command=lambda :first_win(True,siyandawriyaframe))
 search1 = customtkinter.CTkButton(siyandawriyaframe,font=mybutton_font,text="على حسب المدخلات",command=lambda :search_by_input(False))
 searchbydate = customtkinter.CTkButton(siyandawriyaframe,font=mybutton_font,text="للشهر الحالي",command=lambda :search_by_input(True))
 prints = customtkinter.CTkButton(siyandawriyaframe,font=mybutton_font,text="طباعة")
 global getmounths,getyears
 getmounths = customtkinter.StringVar()
 getyears = customtkinter.StringVar() 
 framedating = Frame(siyandawriyaframe,padx=10,pady=10,border=0)
 mounths = customtkinter.CTkOptionMenu(framedating,font=mybutton_font,command=rever_prints,variable=getmounths,values=[
  revers_words("الشهر  1"),revers_words("الشهر  2"),revers_words("الشهر  3")
  ,revers_words("الشهر  4"),revers_words("الشهر  5"),revers_words("الشهر  6"),
  revers_words("الشهر  7"),revers_words("الشهر  8"),revers_words("الشهر  9")
  ,revers_words("الشهر  10"),revers_words("الشهر  11"),revers_words("الشهر  12")],corner_radius=0)
 mounths.set(str(int(str(datetime.datetime.now().strftime("%m"))[-1:]))+"  الشهر ")
 getyears.set("20"+datetime.datetime.now().strftime("%y"))
 
 year=customtkinter.CTkEntry(framedating,textvariable=getyears,font=mybutton_font,corner_radius=0,border_color="#2071B0"
  )
 mounths.grid(row=1, column=2,ipady=5)
 year.grid(row=1, column=1,ipady=5)
 

 logout.grid(row=1, column=0,padx=10, pady=10,ipady=5)
 framedating.grid(row=1,column=4,padx=10, pady=10)
 search1.grid(row=1, column=3,padx=10, pady=10,ipady=5)
 searchbydate.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 prints.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 siyandawriyaframe.pack()
 print_siyana_dawriya()


def c3_comm():
 clear_frame(choose_frame)
 root.state("zoomed")
 root.resizable(width=True, height=True)
 global hohol
 hohol = customtkinter.CTkScrollableFrame(root,width=width_sc-20,height=height_sc-20,fg_color="transparent")
 taqrir_siyana_dawriya_1()
 hohol.pack()

 global frmsgg,nti0
 frmsgg = Frame(root,pady=10)
 nti0= customtkinter.StringVar()
 vvvd = customtkinter.CTkLabel(frmsgg,bg_color='transparent',font=("Times New Roman", 19, "bold"),textvariable=nti0)
 vvvd.grid(row=0, column=0)
 frmsgg.pack()

##
##
##

def reverse_siyana_dawr(fvd=""):
 gr = revers_words(click22_butt_siyana.get())
 click22_butt_siyana.set(gr)
def insert_siyana_dawriya_1():
 
 global siyana_dwariya_inputs
 siyana_dwariya_inputs = Frame(root,padx=200,pady=40)
 l1 = customtkinter.CTkLabel(siyana_dwariya_inputs,font=mybutton_font,text="رقم فاتورة الشراء")
 l2 = customtkinter.CTkLabel(siyana_dwariya_inputs,font=mybutton_font,text="نوع الصيانة")
 l3 = customtkinter.CTkLabel(siyana_dwariya_inputs,font=mybutton_font,text="رقم فاتورة الصيانة")
 l4 = customtkinter.CTkLabel(siyana_dwariya_inputs,font=mybutton_font,text="هل تمت الصيانة")
 l5 = customtkinter.CTkLabel(siyana_dwariya_inputs,font=mybutton_font,text="ملاحظات")
 
 global click1_butt_siyana,click22_butt_siyana,click3_butt_siyana,click4_butt_siyana,click5_butt_siyana
 click1_butt_siyana = customtkinter.StringVar()
 click22_butt_siyana = customtkinter.StringVar()
 click3_butt_siyana = customtkinter.StringVar()
 click4_butt_siyana = customtkinter.StringVar()
 click5_butt_siyana = customtkinter.StringVar()
 
 e1 = customtkinter.CTkEntry(siyana_dwariya_inputs,border_width=1,width=220,textvariable=click1_butt_siyana,font=mybutton_font,justify='right')
 e22 =customtkinter.CTkComboBox(siyana_dwariya_inputs,command=reverse_siyana_dawr,border_width=1,width=220,font=mybutton_font,justify='right',variable=click22_butt_siyana,values=[
  revers_words("صيانة 3 اشهر"),revers_words("صيانة 6 اشهر"),
  revers_words("صيانة 9 اشهر"),revers_words("صيانة 12 شهر"),
  revers_words("صيانة 15 شهر"),revers_words("صيانة 18 شهر"),
  revers_words("صيانة 21 شهر"),revers_words("صيانة 24 شهر")
 ])
 
 e3 = customtkinter.CTkEntry(siyana_dwariya_inputs,border_width=1,width=220,textvariable=click3_butt_siyana,font=mybutton_font,justify='right')
 e4 = customtkinter.CTkEntry(siyana_dwariya_inputs,border_width=1,width=220,textvariable=click4_butt_siyana,font=mybutton_font,justify='right')
 e5 = customtkinter.CTkComboBox(siyana_dwariya_inputs,border_width=1,width=220,font=mybutton_font,justify='right',variable=click5_butt_siyana,values=["لا","نعم"])
 
 l1.grid(row=1, column=2)
 l2.grid(row=2, column=2)
 l3.grid(row=3, column=2)
 l4.grid(row=4, column=2)
 l5.grid(row=5, column=2)
 
 e1.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 e22.grid(row=2, column=1,padx=10, pady=10,ipady=5)
 e3.grid(row=3, column=1,padx=10, pady=10,ipady=5)
 e5.grid(row=4, column=1,padx=10, pady=10,ipady=5)
 e4.grid(row=5, column=1,padx=10, pady=10,ipady=5)
 
 siyana_dwariya_inputs.pack()
 
 global vvvd,nti0,frmsgg
 frmsgg = Frame(root,pady=10)
 nti0= customtkinter.StringVar()
 vvvd = customtkinter.CTkLabel(frmsgg,bg_color='transparent',font=("Times New Roman", 17, "bold"),textvariable=nti0)
 vvvd.grid(row=0, column=0)

 frmsgg.pack(padx=10, pady=10)

def siyana_dawriya_1():
 global window_height,window_width
 
 siyandawriyaframe = Frame(root,padx=100,pady=0,border=0)
 save = customtkinter.CTkButton(siyandawriyaframe,font=mybutton_font,text="حفظ",command=insert_siyana_dawriya_DB)
 logout = customtkinter.CTkButton(siyandawriyaframe,fg_color="#F02849",font=mybutton_font,text="عودة",command=lambda :first_win(True,siyandawriyaframe))
 save.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 logout.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 siyandawriyaframe.pack()

def insert_siyana_dawriya_DB():
 conn = sqlite3.connect('sin.db')
 c = conn.cursor()
 v1 = str(click1_butt_siyana.get())
 v2 = str(click22_butt_siyana.get())
 v3 = str(click3_butt_siyana.get())
 v4 = str(click5_butt_siyana.get())
 v5 = str(click4_butt_siyana.get())
 if(len(v3)==0):
  v3="-"
 if(len(v4)==0):
  v4="-"
 if(len(v5)==0):
  v5="-"
 if(len(v1)==0):
  vvvd.configure(text_color='#F02849')
  nti0.set("!يرجى ادخال رقم فاتورة الشراء")
  conn.close()
 
 date_now_y_m_d = datetime.datetime.now().strftime("%d/%m/%Y").split('/')
 sql = ""
 
 
 if(v2=="صيانة 3 اشهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_3=?,hal_tamat_siyana_3=?,
   molahadat_2_3=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 6 اشهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_6=?,hal_tamat_siyana_6=?,
   molahadat_2_6=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 9 اشهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_9=?,hal_tamat_siyana_9=?,
   molahadat_2_9=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 12 شهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_12=?,hal_tamat_siyana_12=?,
   molahadat_2_12=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 15 شهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_15=?,hal_tamat_siyana_15=?,
   molahadat_2_15=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 18 شهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_18=?,hal_tamat_siyana_18=?,
   molahadat_2_18=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 21 شهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_21=?,hal_tamat_siyana_21=?,
   molahadat_2_21=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 if(v2=="صيانة 24 شهر"):
  sql = """UPDATE siyana SET raq_fatorat_siyana_24=?,hal_tamat_siyana_24=?,
   molahadat_2_24=? WHERE raqm_fatora_chira=?"""
  params = (v3,v4,v5,v1,)
  c.execute(sql, params)
 
 clear_siyan()
 vvvd.configure(text_color='#21B000')
 nti0.set("تم الحفظ بنجاح")
 conn.commit()
 conn.close()

def c2_comm():
 clear_frame(choose_frame)
 root.resizable(width=False, height=False)
 siyana_dawriya_1()
 insert_siyana_dawriya_1()
 
 
##


def print_siyana_mawqi3us(gbf=''):
  cdc = revers_words(click3.get())
  click3.set(cdc)
def print_siyana_ismfani(trt):
  cdc = revers_words(click4.get())
  click4.set(cdc)
def print_jwt(ssdc):
 cdc = revers_words(click1.get())
 click1.set(cdc)

def chahr_print(dc):
 cdcc = revers_words(click55.get())
 click55.set(cdcc)


def siyana_first_part_1():
 global f2
 f2 = customtkinter.CTkFrame(root)
 f2.grid_rowconfigure(1, weight=1)
 f2.grid_columnconfigure(1, weight=1)
 
 logout = customtkinter.CTkButton(f2,text="عودة",font=mybutton_font,fg_color="#F02849",command=lambda :first_win(True,__f3),)
 save = customtkinter.CTkButton(f2,text="حفظ",font=mybutton_font,command= insert_to_db)
 show = customtkinter.CTkButton(f2,text="عرض",font=mybutton_font,command= show_infos)
 dump = customtkinter.CTkButton(f2,text="تفريغ ",font=mybutton_font,command=clear_opp)
 
 logout.grid(row=1, column=1,padx=10, pady=10,ipady=5)
 save.grid(row=1, column=2,padx=10, pady=10,ipady=5)
 show.grid(row=1, column=4,padx=10, pady=10,ipady=5)
 dump.grid(row=1, column=5,padx=10, pady=10,ipady=5)
 f2.grid(row=1, column=1)
 

def siyana_second_part_1():
 global __f3
 __f3 = Frame(root,padx=160,pady=10)
 __f3.grid_rowconfigure(2, weight=1)
 __f3.grid_columnconfigure(1, weight=1)
 
 l1 = customtkinter.CTkLabel(__f3,text="المهمة",font=mybutton_font)
 l2 = customtkinter.CTkLabel(__f3,text="اسم العميل",font=mybutton_font)
 l3 = customtkinter.CTkLabel(__f3,text="الموقع (الحي)",font=mybutton_font)
 l4 = customtkinter.CTkLabel(__f3,text="اسم الفني",font=mybutton_font)
 l5 = customtkinter.CTkLabel(__f3,text="رقم فاتورة الشراء",font=mybutton_font)
 l6 = customtkinter.CTkLabel(__f3,text="تاريخ فاتورة الشراء",font=mybutton_font)
 global click1,click2,click3,click4,click5,click6,vvvs
 global click11,click22,click33,click44,click55,click66,notes,frmsgg

 click1= customtkinter.StringVar()
 click2= customtkinter.StringVar()
 click3= customtkinter.StringVar()
 click4= customtkinter.StringVar()
 click5= customtkinter.StringVar()
 click6= StringVar()

 e1 = customtkinter.CTkComboBox(__f3,command=print_jwt,dropdown_font=mybutton_font,justify='right',border_width=1,width=220,variable=click1,values=[
 "تركيب جهاز","صيانة جهاز","نقل جهاز",
 "بدون تركيب","تركيب برادة"])
 
 e2 = customtkinter.CTkEntry(__f3,font=mybutton_font,border_width=1,width=220,textvariable=click2,justify='right')
 e3 = customtkinter.CTkComboBox(__f3,command=print_siyana_mawqi3us,dropdown_font=mybutton_font,justify='right',border_width=1,width=220,variable=click3,
 values=[revers_words("المهرجان"),revers_words("السليمانية"),revers_words("الخالدية")
   ,revers_words("الفيصلية"),revers_words("سلطانه"),revers_words("الورود")
   ,revers_words("المروج"),revers_words("السلمان")
   ,revers_words("السلام"),revers_words("القادسيه"),revers_words("البوادي")
   ,revers_words("السبيع"),revers_words("المنتزه"),revers_words("الحمرا")
   ,revers_words("ط.المدينة"),revers_words("م.العسكريه"),revers_words("ق.الجويه")
   ,revers_words("ط.عمان"),revers_words("الجديده"),revers_words("الاندلس")
   ,revers_words("العرجان"),revers_words("مروج الامير"),revers_words("النظيم")
   ,revers_words("كريم"),revers_words("الرابيه"),revers_words("الصفا")
   ,revers_words("الاخضر"),revers_words("النهضه"),revers_words("السعاده")
   ,revers_words("ابو سبعه"),revers_words("العليا"),revers_words("قرطبه")
   ,revers_words("المصيف"),revers_words("النخيل"),revers_words("دمج")
   ,revers_words("الجزيره"),revers_words("الدخل"),revers_words("العزيزيه")
   ,revers_words("الاسكان"),revers_words("الاشرفيه"),revers_words("الهضيبه")
   ,revers_words("الضلفه"),revers_words("ضباء"),revers_words("حقل")
   ,revers_words("شقري"),revers_words("العلا"),revers_words("البدع")
   ,revers_words("البير"),revers_words("العيينه"),revers_words("تيماء")
   ,revers_words("الوجه"),revers_words("القليبه"),revers_words("الشفا")
   ,revers_words("الصالحيه"),revers_words("السعيدات"),revers_words("الرويعيات")
   ,revers_words("البساتين"),revers_words("رايس"),revers_words("الراجحي")
   ,revers_words("الراقي"),revers_words("اليرموك"),revers_words("الرواد")
   ,revers_words("الديسه"),revers_words("الروضه"),revers_words("النسيم")
   ,revers_words("المزارع"),revers_words("ابوراكه"),revers_words("شواق")
   ,revers_words("الحره"),revers_words("البر"),revers_words("الصناعيه")
   ,revers_words("الريان"),revers_words("البريكه"),revers_words("غرناطه")
   ,revers_words("خ.المدينه"),"الجمرك","الواحه"
   ,"باركمول","رحيل","الجامعه"
   ,"مجهول","التعاون","الصوامع"
   ,"الجوازات","القدس",revers_words("سنابل مول")
   ,"المدرعات",revers_words("دوار الرمانة")
   ])
 e4 = customtkinter.CTkComboBox(__f3,command=print_siyana_ismfani,dropdown_font=mybutton_font,justify='right',border_width=1,width=220,variable=click4,values=["خالد","مهند",revers_words("عبدالرحمن")
 ,revers_words("السوداني"),revers_words("صلاح"),revers_words("شمس")
 ,revers_words("عبودومهند"),revers_words("عبود ومحمد"),revers_words("عماله سابقه")
 ,revers_words("مجهول"),revers_words("بدون تركيب"),revers_words("خالد و عبدالرحمن")
 ,revers_words("احمد"),revers_words("عبود واحمد"),revers_words("عمرو")
 ,revers_words("عبود احمد مهند"),revers_words("عمر احمد"),revers_words("عمر")
 ])
 e5 = customtkinter.CTkEntry(__f3,font=mybutton_font,border_width=1,width=220,textvariable=click5,justify='right')
 e6 = customtkinter.CTkEntry(__f3,border_width=1,width=220,justify='right',font=mybutton_font, textvariable=click6)
 e6.insert(END,str(datetime.datetime.now().strftime("%d/%m/%Y")))
 l1.grid(row=1, column=4,padx=10,pady=15)
 l2.grid(row=2, column=4,padx=10,pady=15)
 l3.grid(row=3, column=4,padx=10,pady=15)
 l4.grid(row=4, column=4,padx=10,pady=15)
 l5.grid(row=5, column=4,padx=10,pady=15)
 l6.grid(row=6, column=4,padx=10,pady=15)
 

 e1.grid(row=1, column=3,padx=10,pady=15,ipady=2)
 e2.grid(row=2, column=3,padx=10,pady=15,ipady=2)
 e3.grid(row=3, column=3,padx=10,pady=15,ipady=2)
 e4.grid(row=4, column=3,padx=10,pady=15,ipady=2)
 e5.grid(row=5, column=3,padx=10,pady=15,ipady=2)
 e6.grid(row=6, column=3,padx=10,pady=15,ipady=2)
 


 ll1_ = customtkinter.CTkLabel(__f3,text="        ",font=mybutton_font)
 ll2_ = customtkinter.CTkLabel(__f3,text="        ",font=mybutton_font)
 ll3_ = customtkinter.CTkLabel(__f3,text="        ",font=mybutton_font)
 ll4_ = customtkinter.CTkLabel(__f3,text="        ",font=mybutton_font)
 ll5_ = customtkinter.CTkLabel(__f3,text="        ",font=mybutton_font)
 ll6_ = customtkinter.CTkLabel(__f3,text="        ",font=mybutton_font)
 ll1_.grid(row=1, column=2,padx=10,pady=15)
 ll2_.grid(row=2, column=2,padx=10,pady=15)
 ll3_.grid(row=3, column=2,padx=10,pady=15)
 ll4_.grid(row=4, column=2,padx=10,pady=15)
 ll5_.grid(row=5, column=2,padx=10,pady=15)
 ll6_.grid(row=6, column=2,padx=10,pady=15)

 ll1 = customtkinter.CTkLabel(__f3,text="نوع الجهاز",font=mybutton_font)
 ll2 = customtkinter.CTkLabel(__f3,text="موديل الجهاز ",font=mybutton_font)
 ll3 = customtkinter.CTkLabel(__f3,text="رقم الهاتف 1",font=mybutton_font)
 ll4 = customtkinter.CTkLabel(__f3,text="رقم الهاتف 2 ",font=mybutton_font)
 ll5 = customtkinter.CTkLabel(__f3,text="نوع الصيانة ",font=mybutton_font)
 ll6 = customtkinter.CTkLabel(__f3,text="ملاحظات",font=mybutton_font)
 
 click11= customtkinter.StringVar()
 click22= customtkinter.StringVar()
 click33= customtkinter.StringVar()
 click44= customtkinter.StringVar()
 click55= customtkinter.StringVar()
 click66= customtkinter.StringVar()
 
 
 ee1 = customtkinter.CTkComboBox(__f3,dropdown_font=mybutton_font,justify='right',border_width=1,width=220,variable=click11,values=[
   "VOLCANO","VOLCANO STAND","HOMTEC",
   "FILMARC","CALSSIC PURE","BALCK HORS",
   "BLACK STAR","PURECOM","SUPE PRO",
   "SUPER PRO COOLER","SAMNAN","DELTA",
   "UNKNOWN","C.C.K","NAQI"
 ])
 
 ee2 = customtkinter.CTkComboBox(__f3,dropdown_font=mybutton_font,justify='right',border_width=1,width=220,variable=click22,values=[
     "5 STAGES","6 STAGES","7 STAGES",
     "FE-105","FE-106","FE-107",
     "FE-306","FE-307","FE-307 UV",
     "200GPD","400GPD","CE-2",
     "CE-3","CE-4","CE-5",
     "CE-6","CHA-3","3 STAGES JMBO 10\"",
     "3 STAGES JMBO 20\"","UNKNOWN","CCK-106",
     "CCK-107","CCK-306","CCK-307",
     "CCK-307 UV"
 ])

 ee3 = customtkinter.CTkEntry(__f3,font=mybutton_font,border_width=1,width=220,textvariable=click33,justify='right')
 ee4 = customtkinter.CTkEntry(__f3,font=mybutton_font,border_width=1,width=220,textvariable=click44,justify='right')
 ee5 = customtkinter.CTkComboBox(__f3,justify='right',border_width=1,width=220,variable=click55,values=[revers_words("3  اشهر"),revers_words("6  اشهر")])
 ee6 = customtkinter.CTkEntry(__f3,font=mybutton_font,border_width=1,width=220,textvariable=click66,justify='right')

 ll1.grid(row=1, column=1,padx=10,pady=15)
 ll2.grid(row=2, column=1,padx=10,pady=15)
 ll3.grid(row=3, column=1,padx=10,pady=15)
 ll4.grid(row=4, column=1,padx=10,pady=15)
 ll5.grid(row=5, column=1,padx=10,pady=15)
 ll6.grid(row=6, column=1,padx=10,pady=15)

 ee1.grid(row=1, column=0,padx=10,pady=15,ipady=2)
 ee2.grid(row=2, column=0,padx=10,pady=15,ipady=2)
 ee3.grid(row=3, column=0,padx=10,pady=15,ipady=2)
 ee4.grid(row=4, column=0,padx=10,pady=15,ipady=2)
 ee5.grid(row=5, column=0,padx=10,pady=15,ipady=2)
 ee6.grid(row=6, column=0,padx=10,pady=15,ipady=2)

 __f3.grid(row=2, column=1)
 
 frmsgg = Frame(root,pady=10)
 frmsgg.grid_rowconfigure(3, weight=1)
 frmsgg.grid_columnconfigure(1, weight=1)
 
 notes= customtkinter.StringVar()
 notes.set("")
 vvvs = customtkinter.CTkLabel(frmsgg,textvariable=notes,font=mybutton_font,text_color='green')
 vvvs.grid(row=0, column=0)

 frmsgg.grid(row=3, column=1)
 


def c1_comm(): 
 clear_frame(choose_frame)
 root.resizable(width=True, height=True)
 
 root.grid_rowconfigure(3, weight=1)
 root.grid_columnconfigure(1, weight=1)
 siyana_first_part_1()
 siyana_second_part_1()
 

 
 root.state("zoomed")
def clear_frame(frames):
 for widget in frames.winfo_children():
  widget.destroy()
 frames.pack_forget()
 frames.destroy()


def first_win(A=False,fmm=None):
 global choose_frame

 root.grid_rowconfigure(1, weight=1)
 root.grid_columnconfigure(1, weight=1)
 root.resizable(width=False, height=False)
 root.state("normal")

 choose_frame = customtkinter.CTkFrame(root,fg_color='transparent')
 choose_frame.grid_rowconfigure(1, weight=1)
 choose_frame.grid_columnconfigure(1, weight=1)
 
 fontin = ("Times New Roman", 18, "bold")
 c1 = customtkinter.CTkButton(choose_frame,text="استمارة الصيانة",font=fontin,command=c1_comm)
 c2 = customtkinter.CTkButton(choose_frame,text="الصيانة الدورية",font=fontin,command=c2_comm)
 c3 = customtkinter.CTkButton(choose_frame,text="تقرير الصيانة الدورية",command=c3_comm,font=fontin)
 c4 = customtkinter.CTkButton(choose_frame,text="تقرير باسم العميل",command=c4_comm,font=fontin)
 c5 = customtkinter.CTkButton(choose_frame,text="تقرير بالموقع ",command=c5_comm,font=fontin)
 c6 = customtkinter.CTkButton(choose_frame,text="تقرير بالفترة",command=c6_comm,font=fontin)
 c7 = customtkinter.CTkButton(choose_frame,text="تقرير شامل",font=fontin,command=c9_comm)
 c8 = customtkinter.CTkButton(choose_frame,text="قاعدة البيانات",font=fontin,command=c8_comm)
 c9 = customtkinter.CTkButton(choose_frame,text="تقرير نوع الضمان",font=fontin,command=c7_comm)
 #c10 = customtkinter.CTkButton(choose_frame,text="المستخدمين",font=fontin,command=c10_comm)
 #c10.grid(row=3, column=1,padx=20, pady=20,ipady=8,ipadx=8)
 if A==True:
  clear_frame(fmm)
  try:
   clear_frame(f2)
  except:
   pass
  try:
   clear_frame(__f3)
  except:
   pass
  try:
   clear_frame(siyana_dwariya_inputs)
  except:
   pass
  try:
   clear_frame(hohol)
  except:
   pass
  try:
   clear_frame(hohols)
  except:
   pass
  try:
   clear_frame(frmsgg)
  except:
   pass
 c1.grid(row=0, column=1,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c2.grid(row=0, column=2,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c3.grid(row=0, column=3,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c4.grid(row=1, column=1,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c6.grid(row=1, column=3,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c5.grid(row=1, column=2,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c7.grid(row=2, column=1,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c8.grid(row=2, column=2,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 c9.grid(row=2, column=3,padx=20, pady=20,ipady=8,ipadx=8,sticky='NSWE')
 choose_frame.grid(row=1,column=1,padx=20,pady=20)

 

def login():
 global usr_type
 username = user.get()
 pwd = passs.get()
 if(username!='1' and pwd !='1'):
  errors.configure(text_color='#F02849')
  user.configure(border_color="#F02849")
  passs.configure(border_color="#F02849")
  errors.grid(row=4, column=1,padx=20,pady=5)
 else:
  clear_frame(frame1)
  first_win()

global user,passs,errors,usr_type,frame1
root.resizable(width=False, height=False)

frame1 = customtkinter.CTkFrame(root,fg_color='transparent')
frame1.grid_rowconfigure(1, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame = customtkinter.CTkFrame(frame1,fg_color='transparent')
titls = customtkinter.CTkLabel(frame, text="لوحة الدخول ",justify='right',text_color='#2071B0',font=("Times New Roman", 25, "bold"))

user = customtkinter.CTkEntry(frame,placeholder_text="الستخدم اسم",width=300,justify='right',corner_radius=2,border_width=1)
passs = customtkinter.CTkEntry(frame,placeholder_text="المرور كلمة",width=300,justify='right',corner_radius=2,border_width=1)
logins = customtkinter.CTkButton(frame,text="دخول",width=120,font=mybutton_font,command=login)
errors = customtkinter.CTkLabel(frame, text="!كلمة السر او المستخدم خاطئة يرجى اعادة المحاولة  ",justify='right',text_color='#F02849',font=("Times New Roman", 15, "bold"))

user.grid(row=1, column=1,padx=20,pady=10,ipady=5)
passs.grid(row=2, column=1,padx=20,pady=10,ipady=5)
logins.grid(row=3, column=1,padx=10,pady=5,ipady=5,columnspan=2)
titls.grid(row=0, column=1,padx=10,pady=1)
frame.grid(row=0, column=1,padx=10,pady=5,sticky='NSWE')
frame1.grid(row=1,column=1,padx=16,pady=25)


root.mainloop()
