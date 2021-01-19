#import all libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import font as tkFont
from tkinter import messagebox
import mysql.connector
import time
import pymysql


#========================MainClass=================================================================
class Dashboard:
    def __init__(self,front_page):
#=======================Mysql Database Connectivity==========================================
        self.connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="", database="departmental_data")
        self.cursordb = self.connectiondb.cursor()
        self.front_page = front_page
        self.front_page.title("Home Dashboard")
        self.front_page.geometry("1365x2100+0+0")
        self.front_page.configure(bg="lemon chiffon")
        self.front_page.iconbitmap(r'favlogoicon.ico')
#===========================date label and Validation label===================================
        self.dtlabel = Label(self.front_page, text="Date   and   Time", font=("Comic Sans MS", 20, "bold"), bg="lemon chiffon")
        self.dtlabel.place(x=590, y=100)

        self.val_label = Label(self.front_page, text="* indicate that the fields are mandatory",
                          font=("Comic Sans MS", 12, "bold"), bg="lemon chiffon", fg="red")
        self.val_label.place(x=550, y=610)

        #front_page.resizable(False,False)
#=========================Date and Time============================================
        self.clocklbl=Label(self.front_page, font=("Comic Sans MS", 20, "bold"), bg="lemon chiffon")
        self.clocklbl.place(x=491, y=150)
        self.clocktick()
#==================================================================================

        self.Top_frame = Frame(self.front_page, bd=4, relief="groove")
        self.Top_frame.place(x=1, y=4, height=65, width=1366)
        self.logoimage = Image.open("LogoofCUPB.jpg")
        self.load = ImageTk.PhotoImage(self.logoimage)

        self.logolabel = Label(self.Top_frame, bg='white', image=self.load)
        self.logolabel.place(x=0, y=0, height=55, width=45)

        self.toplabel = Label(self.Top_frame, text="DEPARTMENT MANAGEMENT SYSTEM", fg="SeaGreen3", font=("Comic Sans MS", 40, "bold"))
        self.toplabel.pack()

        self.bottom_frame = Frame(self.front_page, bd=4, relief="groove", bg="snow")
        self.bottom_frame.place(x=1, y=640, height=65, width=1366)

        self.botmlabel = Label(self.bottom_frame, bg="snow",text="Copyright 2020 | Department Management System | Waseem Akram Khan | M.Tech.(CST) | Central University of Punjab | waseemakhan4@gmail.com | 0164 286 4122", font=("times new roman" ,12,"bold" ), fg="LightSteelBlue4")
        self.botmlabel.place(x=140,y=20)

        self.right_frame = Frame(self.front_page, bd=4, relief="groove")
        self.right_frame.place(x=900, y=70, height=570, width=465)

        self.right_label = Label(self.right_frame, text="***SUMMARY OF DEPARTMENT***", fg="green", font=("Times new roman", 15, "bold"))
        self.right_label.pack()
        self.mgs = """The School of Engineering & Technology offers admission to M.Tech.programme 
                in Computer Science and Technology and in Cyber Security. The objective of the 
                programme is to impart advanced computer technology education to bridge the 
                gap between industry and academia. The centre has well equipped state of the art 
                SoftwareLaboratory, Cyber Security and Research Laboratory for academics and 
                research purposes. The aim of the centre is to focus on various research areas like
                wireless networks and their security, cloud computing, mobile computing, 
                software engineering and image processing.

                Faculty of Our Department
                *************************
                1. Dr. Amandeep Kaur (Dean of Department)
                2. Dr. Satwinder Singh (Head of Department)
                3. Dr. Parvinder Singh, Assistant Professor
                4. Er. Meenakshi, Assistant Professor
                5. Er. Surinder Khurana, Assistant Professor
                6. Er. Anam Bansal, Assistant Professor
                """

        self.rightlabel = Label(self.right_frame, text=self.mgs, font=("Times new roman", 10), fg="gray25")
        self.rightlabel.pack()

        self.deptimage = Image.open("SE&T.PNG")
        self.deptload = ImageTk.PhotoImage(self.deptimage)
        self.deptlabel = Label(self.right_frame, bg='white',bd=3, relief='flat', image = self.deptload)
        self.deptlabel.place(x=0, y=324, height=235, width=455)
        self.leftside_frame = Frame(self.front_page, bd=4, relief="groove")
        self.leftside_frame.place(x=1, y=70, height=570, width=500)

        self.blwlogo=Label(self.leftside_frame, text="User Login", fg="black", font=("Comic Sans MS",16,"bold"))
        self.blwlogo.pack(padx=30,pady=208)

        self.adlogo = Image.open("a2.png")
        self.adlogoload = ImageTk.PhotoImage(self.adlogo)
        self.adminlabel = Label(self.leftside_frame , bg='gray', relief="groove", bd=3, image = self.adlogoload)
        self.adminlabel.place(x=165,y=32, height = 175, width = 175)

        self.userlabel = Label(self.leftside_frame, text="Username*", font=("Times new roman", 19,"bold"))
        self.userlabel.place(x=80, y=281)
        self.passlabel = Label(self.leftside_frame, text="Password*", font=("Times new roman", 19,"bold"))
        self.passlabel.place(x=80, y=323)
        self.Username=StringVar()
        self.Password=StringVar()

        self.user_entry = Entry(self.leftside_frame, width=35, bd=2, relief="raised",highlightbackground = 'green', highlightthickness = 2,textvariable=self.Username)
        self.user_entry.place(x=215, y=292)

        self.pass_entry = Entry(self.leftside_frame, width=35,bd=2, show="*", relief="raised",highlightbackground = 'green', highlightthickness = 2,textvariable=self.Password)
        self.pass_entry.place(x=215, y=334)

        self.btnlogin = Button(self.leftside_frame, text="Login", relief ="raised", bd=3, fg="black", font=10, width=10,bg='brown', command=self.login_button)
        self.btnlogin.place(x=80,y=400)
        self.btnreset = Button(self.leftside_frame, text="Reset", relief ="raised", bd=3, fg="black", font=10, width=10,bg='brown')
        self.btnreset.place(x=225,y=400)
        self.btnexit = Button(self.leftside_frame, text="Exit", relief ="raised", bd=3, fg="black", font=10, width=10,bg='brown')
        self.btnexit.place(x=360,y=400)
#==============================Exit Button Function============================================

    def clocktick(self):
        self.time_string = time.strftime("%H:%M:%S")
        self.date_string = time.strftime("%d-%m-%Y")
        self.clocklbl.configure(text=" " + self.date_string + "  and  " + self.time_string)
        self.clocklbl.after(200, self.clocktick)

#====================================Reset Button Fuction======================================
    #def Reset(self):
        #self.Username.set("")
        #self.Password.set("")
        #self.user_entry.focus()
        #self.pass_entry.focus()
#=======================================Login Button Function==================================
    def login_button(self):
        if self.Username.get() == "":
            pass
            #messagebox.showinfo("Alert!", "Enter your Valid Username")
        elif self.Password.get() == "":
            messagebox.showinfo("Alert!", "Enter your Valid Password")
        else:
            self.user_verification = self.Username.get()
            self.pass_verification = self.Password.get()
            self.sql = "select role_type from user where username = %s and password = %s"
            self.cursordb.execute(self.sql, [(self.user_verification), (self.pass_verification)])
            self.results = self.cursordb.fetchone()
            self.nxtpanel = ("D".join(self.results))
            #print(nxtpanel)
            if self.nxtpanel:
                if self.nxtpanel == 'Admin':
                    self.admin_window()
                elif self.nxtpanel == 'Teacher':
                    messagebox.showinfo("Success", "Teacher Panel")
                elif self.nxtpanel == 'Student':
                    self.student_view()
                    #messagebox.showinfo("Success", "Student Panel")
                else:
                    messagebox.showinfo("Warning", "Role does not match")
            else:
                messagebox.showinfo("Alert!", "You have Provided Wrong Credential")
    # ================================End of Login_button function==============================
    #def exitwindow(self):
        #self.exitwindow = messagebox.askyesno("Department Management System Dashboard", "Confirm if you want to really Exit")
        #if self.exitwindow>0:
            #self.front_page.destroy()

    def admin_window(self):
        self.front_page.withdraw()
        self.adminWindow = Toplevel(self.front_page)
        self.obj1= AdminWindow(self.adminWindow)

    def student_view(self):
        self.front_page.withdraw()
        self.StudentView = Toplevel(self.front_page)
        self.obj2 = Student_View(self.StudentView)
#===============================================================================================

class AdminWindow:
    def __init__(self, nextpage):
        self.nextpage = nextpage
        self.nextpage.title("Administrative Panel")
        self.nextpage.geometry("1365x2100+0+0")
        self.nextpage.config(bg = "lemon chiffon")
        self.nextpage.iconbitmap(r'administrator_icon.ico'.center(400))
        self.helv36 = tkFont.Font(family='Comic Sans MS', size=17, weight=tkFont.BOLD)
#======================================All Frames are Here!!!=========================================
        self.topframe = Frame(self.nextpage, bd=3, relief="ridge",bg="white")
        self.topframe.place(x=0, y=1, height=70, width=1365)
        self.topblwframe= Frame(self.nextpage,bd=3, relief="ridge", bg="white")
        self.topblwframe.place(x=0, y=72.2, height=80, width=1365)
#==================================================All tiles Frames==================================
        self.tilesframe1 = Frame(self.nextpage, bd=4, relief = "ridge", bg ="#556b82")
        self.tilesframe1.place(x=115, y=207, height=235, width=235)

        self.tilesframe2 = Frame(self.nextpage, bd=4, relief="ridge", bg="#556b82")
        self.tilesframe2.place(x=415, y=207, height=235, width=235)

        self.tilesframe3 = Frame(self.nextpage, bd=4, relief="ridge", bg="#556b82")
        self.tilesframe3.place(x=717, y=207, height=235, width=235)

        self.tilesframe4 = Frame(self.nextpage, bd=4, relief="ridge", bg="#556b82")
        self.tilesframe4.place(x=1010, y=207, height=235, width=235)
#=======================================All Labels are Here===========================================
        self.toplabel=Label(self.topframe, text="Welcome to School of Engineering & Technology", font=("Poppins", 33, "bold"), bg="White", fg="#41aea9")
        self.toplabel.place(x=150, y=4)

#=======================================All Button Here==============================================
        self.logbtn = Button(self.topframe, text="Logout",command=self.logouttopframe, relief="raised", bd=2, fg="#0d0d0d", width=10, bg="#498b91")
        self.logbtn.place(x=1273, y=22)

        self.mngsbtn=Button(self.topblwframe, text="Manage\nStudent",relief ="raised", bd=3, fg="#0d0d0d",font=self.helv36, width=20,
                            bg="#498b91", command=self.manage_student)
        self.mngsbtn.place(x=5, y=2, height=70, width=140)

        self.mngsbtn = Button(self.topblwframe, text="Manage\nFaculties", relief="raised", bd=3, fg="#0d0d0d",font=self.helv36, width=20,
                              bg="#498b91", command= self.manage_faculty)
        self.mngsbtn.place(x=165, y=2, height=70, width=140)

        self.mngsbtn = Button(self.topblwframe, text="View\nAttendenace", relief="raised", bd=3, fg="#0d0d0d",
                              font=self.helv36, width=20, bg="#498b91")
        self.mngsbtn.place(x=325, y=2, height=70, width=150)
        self.mngsbtn = Button(self.topblwframe, text="Department\nEvents", relief="raised", bd=3, fg="#0d0d0d",
                              font=self.helv36, width=20, bg="#498b91")
        self.mngsbtn.place(x=495, y=2, height=70, width=160)

        self.mngsbtn = Button(self.topblwframe, text="View\nStudents", relief="raised", bd=3, fg="#0d0d0d",
                              font=self.helv36, width=20, bg="#498b91")
        self.mngsbtn.place(x=675, y=2, height=70, width=160)

        self.mngsbtn = Button(self.topblwframe, text="View\nFaculties", relief="raised", bd=3, fg="#0d0d0d",
                              font=self.helv36, width=20, bg="#498b91")
        self.mngsbtn.place(x=855, y=2, height=70, width=160)

        # ===================================All Images are Here!!!============================================
        self.adminlogo = Image.open("AdminCUPB.PNG")
        self.adminlogoload = ImageTk.PhotoImage(self.adminlogo)
        self.adminlbl = Label(self.topframe, bg='white', bd=3, relief='flat', image=self.adminlogoload)
        self.adminlbl.place(x=0, y=0, height=65, width=100)

        self.clocklbladmin = Label(self.topblwframe, font=("Comic Sans MS", 15, "bold"), bd=3, relief="sunken")
        self.clocklbladmin.place(x=1125, y=3, height=68, width=230)
        self.clockadmin()

    def logouttopframe(self):
        self.nextpage.destroy()

    def clockadmin(self):
        self.time_string = time.strftime("%H:%M:%S")
        self.date_string = time.strftime("%d-%m-%Y")
        self.clocklbladmin.configure(text="" + self.date_string + "\n" + self.time_string)
        self.clocklbladmin.after(200, self.clockadmin)
    def manage_student(self):
        self.nextpage.withdraw()
        self.stdWindow = Toplevel(self.nextpage)
        self.obj1 = student(self.stdWindow)
    def manage_faculty(self):
        self.nextpage.withdraw()
        self.facultyWindow = Toplevel(self.nextpage)
        self.obj1 = Employee(self.facultyWindow)
#=======================================================================================
class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Record")
        self.root.geometry("1365x2100+0+0")
        self.helv36 = tkFont.Font(family='Comic Sans MS', size=17, weight=tkFont.BOLD)
        # root.resizable(height = False, width = False)
        self.title = Label(self.root, text="Students Records Session 2020-2021",
                           font=("times new roman", 30, "bold"), bd=7, relief="ridge", fg="yellow", bg="#456c89").pack(
            side=TOP, fill=X)

        # =========================All Student related variables===================================
        self.redg_no_var = StringVar()
        self.Name_var = StringVar()
        self.fname_var = StringVar()
        self.Course_var = StringVar()
        self.DOB_var = StringVar()
        self.Gender_var = StringVar()
        self.contact_var=StringVar()
        self.email_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        # ==============================Student Manage Frame==================================
        self.manage_frame = LabelFrame(self.root, bd=7, relief="ridge", bg="#686d65", text="Manage Students",
                                       font=("times new roman", 15, "bold"), fg="white")
        self.manage_frame.place(x=2, y=80, width=1365, height=250)

        # ==============================Student Manage Entry's Label==================================
        self.redg = Label(self.manage_frame, text="Registration number  ", fg="white", bg="#686d65",
                          font=("times new roman", 20, "bold"))
        self.redg.place(x=10, y=12)

        self.name = Label(self.manage_frame, text="Name ", fg="white", bg="#686d65",
                          font=("times new roman", 20, "bold"))
        self.name.place(x=450, y=12)

        self.course = Label(self.manage_frame, text="Course ", fg="white", bg="#686d65",
                            font=("times new roman", 20, "bold"))
        self.course.place(x=765, y=12)

        self.gender = Label(self.manage_frame, text="Gender ", fg="white", bg="#686d65",
                            font=("times new roman", 20, "bold"))
        self.gender.place(x=1038, y=12)

        self.fname = Label(self.manage_frame, text="Father's Name ", fg="white", bg="#686d65",
                           font=("times new roman", 20, "bold"))
        self.fname.place(x=10, y=76)

        self.dob = Label(self.manage_frame, text="D.O.B ", fg="white", bg="#686d65",
                         font=("times new roman", 20, "bold"))
        self.dob.place(x=449, y=76)

        self.contact = Label(self.manage_frame, text="Contact No. ", fg="white", bg="#686d65",
                         font=("times new roman", 20, "bold"))
        self.contact.place(x=710, y=76)

        self.email = Label(self.manage_frame, text="Email id ", fg="white", bg="#686d65",
                             font=("times new roman", 20, "bold"))
        self.email.place(x=1037, y=76)

        #========================================Student Inside Manage Frame=======================
        self.inside_manage = Frame(self.manage_frame,bd=1, relief="flat", bg="#686d65")
        self.inside_manage.place(x=5, y=135, width=700, height=75)

        # =========================================Student Related Button Frame==============================
        self.Addbtn = Button(self.inside_manage, text="Save New", command=self.Add_student, bg="#42f5e9", relief="raised", bd=3,font=self.helv36)
        self.Addbtn.place(x=10, y=17,height=42, width=125)

        self.updatebtn = Button(self.inside_manage, text="Update", command=self.update_data,bg="#42f5e9", relief="raised", bd=3,font=self.helv36)
        self.updatebtn.place(x=158, y=17,height=42, width=110)

        self.delbtn = Button(self.inside_manage, text="Delete",bg="#42f5e9", relief="raised", bd=3,font=self.helv36, command=self.delete_date)
        self.delbtn.place(x=296, y=17,height=42, width=110)

        self.resetbtn = Button(self.inside_manage, text="Reset", command=self.reset,bg="#42f5e9", relief="raised", bd=3,font=self.helv36)
        self.resetbtn.place(x=434, y=17,height=42, width=110)

        self.prntbtn = Button(self.inside_manage, text="Back",bg="#42f5e9", relief="raised", bd=3,font=self.helv36)
        self.prntbtn.place(x=572, y=17,height=42, width=110)

        # ===============================All Student Manage Entries=====================================
        self.rdge_entry = Entry(self.manage_frame, textvariable=self.redg_no_var, relief="raised", bd=3,
                                font=("times new roman", 16, "bold"), width=10)
        self.rdge_entry.place(x=270, y=19)

        self.name_entry = Entry(self.manage_frame, textvariable=self.Name_var, relief="raised", bd=3,
                                font=("times new roman", 16, "bold"), width=15)
        self.name_entry.place(x=535, y=19)

        self.course_entry = Entry(self.manage_frame, textvariable=self.Course_var, relief="raised", bd=3,
                                  font=("times new roman", 16, "bold"), width=10)
        self.course_entry.place(x=870, y=17)

        self.combo_gender = ttk.Combobox(self.manage_frame, textvariable=self.Gender_var,
                                         font=("times new roman", 15, "bold"), state="readonly", width=10)
        self.combo_gender["values"] = ("Male", "Female", "Other")
        self.combo_gender.place(x=1143, y=19)

        self.fname_entry = Entry(self.manage_frame, textvariable=self.fname_var, relief="raised", bd=3,
                                 font=("times new roman", 16, "bold"),width=17)
        self.fname_entry.place(x=200, y=80)

        self.dob_entry = Entry(self.manage_frame, textvariable=self.DOB_var, relief="raised", bd=3,
                                  font=("times new roman", 16, "bold"),width=10)
        self.dob_entry.place(x=536, y=80)

        self.contact_entry = Entry(self.manage_frame, textvariable=self.contact_var, relief="raised", bd=3,
                               font=("times new roman", 16, "bold"), width=11)
        self.contact_entry.place(x=875, y=80)

        self.email_entry = Entry(self.manage_frame, textvariable=self.email_var, relief="raised", bd=3,
                                   font=("times new roman", 16, "bold"), width=17)
        self.email_entry.place(x=1152, y=80)

        # =============================Student detail Frame=====================================
        self.detail_frame = LabelFrame(self.root, bd=7, text="Student Details", font=("times new roman", 15, "bold"),
                                       fg="white", relief="ridge", bg="#686d65")
        self.detail_frame.place(x=2, y=350, width=1365, height=350)
        # ================================Student Detail Label==================================
        self.srchlabel = Label(self.detail_frame, text="Search By ", fg="white", bg="#686d65",
                               font=("Comic Sans MS", 20, "bold"))
        self.srchlabel.place(x=425, y=0)
        # =======================Studet Detail Entry============================================
        self.combo_gender = ttk.Combobox(self.detail_frame, font=("times new roman", 17, "bold"),textvariable=self.search_by, state="readonly", width=10)
        self.combo_gender["values"] = ("Email_id", "Course", "Registration Number")
        self.combo_gender.place(x=570, y=8)

        self.srchentry = Entry(self.detail_frame, relief="ridge", bd=3, textvariable=self.search_txt, font=("times new roman", 17, "bold"))
        self.srchentry.place(x=760, y=8)
        # ==============================Student Detail Button========================================
        self.srchbtn = Button(self.detail_frame, text="Search",font=self.helv36,bg="#42f5e9", relief="raised", bd=3)
        self.srchbtn.place(x=1050, y=7, width=120, height=35)
        self.shwbtn = Button(self.detail_frame, text="Show All",font=self.helv36,bg="#42f5e9", relief="raised", bd=3,command=self.fetch_value)
        self.shwbtn.place(x=1200, y=7, width=120, height=35)
        #=======================Student Table Frame================================

        self.Table_frame = Frame(self.detail_frame, bd=2, relief="ridge")
        self.Table_frame.place(x=0, y=50, width=1350, height=270)
        scroll_x = Scrollbar(self.Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(self.Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Student_table = ttk.Treeview(self.Table_frame,
                                          columns=("id","User_id","redg_no", "Name", "fname", "Course", "D.O.B", "Gender","contact","email"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("id", text="Sr. No.",anchor=CENTER)
        self.Student_table.heading("User_id", text="User Id",anchor=CENTER)
        self.Student_table.heading("redg_no", text="Registration Number",anchor=CENTER)
        self.Student_table.heading("Name", text="Name",anchor=CENTER)
        self.Student_table.heading("fname", text="Father's Name",anchor=CENTER)
        self.Student_table.heading("Course", text="Course",anchor=CENTER)
        self.Student_table.heading("D.O.B", text="Date of Birth",anchor=CENTER)
        self.Student_table.heading("Gender", text="Gender",anchor=CENTER)
        self.Student_table.heading("contact",text="Contact No.",anchor=CENTER)
        self.Student_table.heading("email",text="Email id",anchor=CENTER)
        self.Student_table["show"] = "headings"
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_data)
        self.fetch_value()

    def get_data(self, ev):
        cursor_row = self.Student_table.focus()
        data = self.Student_table.item(cursor_row)
        row = data['values']
        self.id.set(row[0])
        self.max_id.set(row[1])
        self.redg_no_var.set(row[0])
        self.Name_var.set(row[1])
        self.fname_var.set(row[2])
        self.Course_var.set(row[3])
        self.DOB_var.set(row[4])
        self.Gender_var.set(row[5])
        self.contact_var.set(row[6])
        self.email_var.set(row[7])

    # ============================================Student Database Working===================================
    def Add_student(self):
        if self.redg_no_var.get()=="" or self.Name_var.get()=="":
            messagebox.showwarning("Warning", "All Fields are Required!!!")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
            cur = conn.cursor()
            cur.execute("insert into user (username, password, role_type) values(%s, %s, %s)", (self.email_var.get(), self.contact_var.get(),'Student'))
            cur.execute("select MAX(id) from user")
            user_id = cur.fetchone()
            for max_id in user_id:
                pass
            cur.execute("insert into newstudent values(user_id,redg_no,Name,Father_name,Course,dob,gender,Contact_Number,Email_id) values(%s, %s, %s, %s, %s, %s, %s, %s,%s)", (max_id,self.redg_no_var.get(),
                                                                             self.Name_var.get(),
                                                                             self.fname_var.get(),
                                                                             self.Course_var.get(),
                                                                             self.DOB_var.get(),
                                                                             self.Gender_var.get(),
                                                                             self.contact_var.get(),
                                                                             self.email_var.get()
                                                                             ))
            conn.commit()
            self.fetch_value()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "One More Record has been Successfully Recorded!!!")

    # ==============================Student Fetching Data Functionalities===================================
    def fetch_value(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("select * from newstudent")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    # ================================Student Reset Button Functionalities===================================
    def reset(self):
        self.redg_no_var.set("")
        self.Name_var.set("")
        self.fname_var.set("")
        self.Course_var.set("")
        self.DOB_var.set("")
        self.Gender_var.set("")
        self.contact_var.set("")
        self.email_var.set("")

    # ================================Student Update Functionalities===============================
    def update_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("update newstudent set Name=%s,Father_name=%s,Course=%s,dob=%s,gender=%s,Contact_Number=%s, Email_id=%s where redg_no=%s", (
            self.Name_var.get(),
            self.fname_var.get(),
            self.Course_var.get(),
            self.DOB_var.get(),
            self.Gender_var.get(),
            self.contact_var.get(),
            self.email_var.get(),
            self.redg_no_var.get()
        ))
        conn.commit()
        self.fetch_value()
        self.reset()
        conn.close()
    def delete_date(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("delete from newstudent where redg_no=%s",self.redg_no_var.get())
        conn.commit()
        conn.close()
        self.fetch_value()
        self.reset()

    # =======================================Student Delete Functionalities==========================
    def search_values(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("select * from newstudent where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            conn.commit()
        conn.close()
#========================================End of Student Functionalities=============================
#================================Faculty Fucntionalities Start Here!!!==============================
class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard/Admin/Faculties Record")
        self.root.geometry("1365x695+0+0")
        root.resizable(height=True, width=True)
        self.helv36 = tkFont.Font(family='Comic Sans MS', size=17, weight=tkFont.BOLD)
        self.title = Label(self.root, text="Faculty Record Session 2020-2021",
                           font=("times new roman", 30, "bold"), bd=7, relief="ridge", fg="yellow", bg="#456c89").pack(
            side=TOP, fill=X)

        # =========================All Faculty related variables=====================================
        self.fid_var = StringVar()
        self.fname_var = StringVar()
        self.fdob_var = StringVar()
        self.fdoj_var = StringVar()
        self.fdesignation_var = StringVar()
        self.ftype_var = StringVar()
        self.married_var = StringVar()
        self.Gender_var = StringVar()
        self.areaspl_var = StringVar()
        self.fcontact_var = StringVar()
        self.femail_var = StringVar()

        # =========================Manage Faculty Frame=============================================
        self.fmanage_frame = LabelFrame(self.root, bd=7, relief="ridge", bg="#686d65", text="Manage Faculty",
                                        font=("times new roman", 15, "bold"), fg="white")
        self.fmanage_frame.place(x=2, y=70, width=1365, height=355)

        # ============================Faculty Detail Frame==========================================
        self.fdetail_frame = LabelFrame(self.root, bd=7, text="Student Details", font=("times new roman", 15, "bold"),
                                        fg="white", relief="ridge", bg="#686d65")
        self.fdetail_frame.place(x=2, y=435, width=1365, height=300)

        # =============================All Faculty related Labels====================================
        self.fid = Label(self.fmanage_frame, text="Faculty Id ", fg="white", bg="#686d65",
                         font=("times new roman", 20, "bold"))
        self.fid.place(x=10, y=10)

        self.fname = Label(self.fmanage_frame, text="Name ", fg="white", bg="#686d65",
                           font=("times new roman", 20, "bold"))
        self.fname.place(x=330, y=10)

        self.fdob = Label(self.fmanage_frame, text="D.O.B ", fg="white", bg="#686d65",
                          font=("times new roman", 20, "bold"))
        self.fdob.place(x=690, y=10)

        self.dojoin = Label(self.fmanage_frame, text="Joining Date ", fg="white", bg="#686d65",
                            font=("times new roman", 20, "bold"))
        self.dojoin.place(x=995, y=10)

        self.fdesig = Label(self.fmanage_frame, text="Designation ", fg="white", bg="#686d65",
                            font=("times new roman", 20, "bold"))
        self.fdesig.place(x=10, y=90)

        self.ftype = Label(self.fmanage_frame, text="Employee Type ", fg="white", bg="#686d65",
                           font=("times new roman", 20, "bold"))
        self.ftype.place(x=355, y=90)

        self.fmarital = Label(self.fmanage_frame, text="Marital Status ", fg="white", bg="#686d65",
                              font=("times new roman", 20, "bold"))
        self.fmarital.place(x=740, y=90)

        self.gender = Label(self.fmanage_frame, text="Gender ", fg="white", bg="#686d65",
                            font=("times new roman", 20, "bold"))
        self.gender.place(x=1105, y=90)

        self.Areasep = Label(self.fmanage_frame, text="Area Specialization ", fg="white", bg="#686d65",
                             font=("times new roman", 20, "bold"))
        self.Areasep.place(x=10, y=165)

        self.fcontact = Label(self.fmanage_frame, text="Contact No. ", fg="white", bg="#686d65",
                              font=("times new roman", 20, "bold"))
        self.fcontact.place(x=530, y=165)

        self.femail_id = Label(self.fmanage_frame, text="Email id ", fg="white", bg="#686d65",
                               font=("times new roman", 20, "bold"))
        self.femail_id.place(x=900, y=165)

        self.fdobsug = Label(self.fmanage_frame, text="##Date format should be DD/MM/YYYY", fg="#05f7a7", bg="#686d65",
                             font=("times new roman", 12, "bold"))
        self.fdobsug.place(x=1000, y=290)

        # ==============================All Faculties Label Entries=====================================
        self.fid_entry = Entry(self.fmanage_frame, textvariable=self.fid_var, relief="raised", bd=3,
                               font=("times new roman", 16, "bold"), width=10)
        self.fid_entry.place(x=145, y=15)

        self.fname_entry = Entry(self.fmanage_frame, textvariable=self.fname_var, relief="raised", bd=3,
                                 font=("times new roman", 16, "bold"), width=18)
        self.fname_entry.place(x=413, y=15)

        self.fdob_entry = Entry(self.fmanage_frame, textvariable=self.fdob_var, relief="raised", bd=3,
                                font=("times new roman", 16, "bold"), width=13)
        self.fdob_entry.place(x=780, y=15)

        self.fdoj_entry = Entry(self.fmanage_frame, textvariable=self.fdoj_var, relief="raised", bd=3,
                                font=("times new roman", 16, "bold"), width=13)
        self.fdoj_entry.place(x=1159, y=15)

        self.combo_fdesig = ttk.Combobox(self.fmanage_frame, textvariable=self.fdesignation_var,
                                         font=("times new roman", 15, "bold"), state="readonly", width=10)
        self.combo_fdesig["values"] = ("Professor", "Associate Professor", "Assistant Professor", "Lecturer")
        self.combo_fdesig.place(x=161, y=95)

        self.combo_ftype = ttk.Combobox(self.fmanage_frame, textvariable=self.ftype_var,
                                        font=("times new roman", 15, "bold"), state="readonly", width=10)
        self.combo_ftype["values"] = ("Permanent", "Adhoc", "Other")
        self.combo_ftype.place(x=545, y=95)

        self.combo_ftype = ttk.Combobox(self.fmanage_frame, textvariable=self.married_var,
                                        font=("times new roman", 15, "bold"), state="readonly", width=10)
        self.combo_ftype["values"] = ("Married", "Unmarried")
        self.combo_ftype.place(x=922, y=95)

        self.combo_gender = ttk.Combobox(self.fmanage_frame, textvariable=self.Gender_var,
                                         font=("times new roman", 15, "bold"), state="readonly", width=10)
        self.combo_gender["values"] = ("Male", "Female", "Other")
        self.combo_gender.place(x=1205, y=95)

        self.areaspl_entry = Entry(self.fmanage_frame, textvariable=self.areaspl_var, relief="raised", bd=3,
                                   font=("times new roman", 16, "bold"), width=19)
        self.areaspl_entry.place(x=252, y=170)

        self.fcontact_entry = Entry(self.fmanage_frame, textvariable=self.fcontact_var, relief="raised", bd=3,
                                    font=("times new roman", 16, "bold"), width=13)
        self.fcontact_entry.place(x=685, y=170)

        self.femail_entry = Entry(self.fmanage_frame, textvariable=self.femail_var, relief="raised", bd=3,
                                  font=("times new roman", 16, "bold"), width=20)
        self.femail_entry.place(x=1015, y=170)

        # ========================================Faculty Inside Manage Frame=====================================
        self.finside_manage = Frame(self.fmanage_frame, bd=1, relief="flat", bg="#686d65")
        self.finside_manage.place(x=5, y=235, width=800, height=75)

        # ==================================All Faculty Related Button============================================
        self.Addbtn = Button(self.finside_manage, text="Save New", bg="#42f5e9", relief="raised", bd=3,
                             font=self.helv36, command=self.Add_Faculty)
        self.Addbtn.place(x=17, y=17, height=42, width=125)

        self.updatebtn = Button(self.finside_manage, text="Update", bg="#42f5e9", relief="raised", bd=3,
                                font=self.helv36, command=self.update_data)
        self.updatebtn.place(x=190, y=17, height=42, width=110)

        self.delbtn = Button(self.finside_manage, text="Delete", bg="#42f5e9", relief="raised", bd=3, font=self.helv36,
                             command=self.delete_data)
        self.delbtn.place(x=355, y=17, height=42, width=110)

        self.resetbtn = Button(self.finside_manage, text="Reset", bg="#42f5e9", relief="raised", bd=3, font=self.helv36,
                               command=self.reset)
        self.resetbtn.place(x=515, y=17, height=42, width=110)

        self.prntbtn = Button(self.finside_manage, text="Print", bg="#42f5e9", relief="raised", bd=3, font=self.helv36)
        self.prntbtn.place(x=675, y=17, height=42, width=110)

        # =======================Faculty Detail Table Frame======================================================
        self.fTable_frame = Frame(self.fdetail_frame, bd=2, relief="ridge")
        self.fTable_frame.place(x=0, y=0, width=1350, height=245)

        scroll_x = Scrollbar(self.fTable_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(self.fTable_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Faculty_table = ttk.Treeview(self.fTable_frame,
                                          columns=("fid", "factlyName", "fdob", "fdoj", "fdesig", "ftype", "fmarital",
                                                   "gender", "areaspl", "contact", "email"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.Faculty_table.xview)
        scroll_y.config(command=self.Faculty_table.yview)
        self.Faculty_table.heading("fid", text="Faculty Id")
        self.Faculty_table.heading("factlyName", text="Faculty Name")
        self.Faculty_table.heading("fdob", text="Date of Birth")
        self.Faculty_table.heading("fdoj", text="Joining Date")
        self.Faculty_table.heading("fdesig", text="Designation")
        self.Faculty_table.heading("ftype", text="Faculty Type")
        self.Faculty_table.heading("fmarital", text="Marital Status")
        self.Faculty_table.heading("gender", text="Gender")
        self.Faculty_table.heading("areaspl", text="Area Specialization")
        self.Faculty_table.heading("contact", text="Contact number")
        self.Faculty_table.heading("email", text="Email id")
        self.Faculty_table["show"] = "headings"
        self.Faculty_table.pack(fill=BOTH, expand=1)
        self.Faculty_table.bind("<ButtonRelease-1>", self.get_Data)
        self.Fetch_Data()

    def get_Data(self, ev):
        cursor_row = self.Faculty_table.focus()
        data = self.Faculty_table.item(cursor_row)
        row = data['values']
        self.fid_var.set(row[0])
        self.fname_var.set(row[1])
        self.fdob_var.set(row[2])
        self.fdoj_var.set(row[3])
        self.fdesignation_var.set(row[4])
        self.ftype_var.set(row[5])
        self.married_var.set(row[6])
        self.Gender_var.set(row[7])
        self.areaspl_var.set(row[8])
        self.fcontact_var.set(row[9])
        self.femail_var.set(row[10])

    # ================================Faculty Reset Button Functionalities===================================
    def reset(self):
        self.fid_var.set("")
        self.fname_var.set("")
        self.fdob_var.set("")
        self.fdoj_var.set("")
        self.fdesignation_var.set("")
        self.ftype_var.set("")
        self.married_var.set("")
        self.Gender_var.set("")
        self.areaspl_var.set("")
        self.fcontact_var.set("")
        self.femail_var.set("")

    # ============================================Faculty Database Working===================================
    def Add_Faculty(self):
        if self.fid_var.get() == "" or self.fname_var.get() == "" or self.fdob_var.get() == "" or self.femail_var.get() == "":
            messagebox.showwarning("Warning", "All Fields are Required!!!")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
            cur = conn.cursor()
            cur.execute("insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.fid_var.get(),
                                                                                         self.fname_var.get(),
                                                                                         self.fdob_var.get(),
                                                                                         self.fdoj_var.get(),
                                                                                         self.fdesignation_var.get(),
                                                                                         self.ftype_var.get(),
                                                                                         self.married_var.get(),
                                                                                         self.Gender_var.get(),
                                                                                         self.areaspl_var.get(),
                                                                                         self.fcontact_var.get(),
                                                                                         self.femail_var.get()))
            conn.commit()
            self.Fetch_Data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "One more record has been Successfully recorded!!!")

    # ==============================Faculty Fetching Data Functionalities===================================
    def Fetch_Data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("select * from faculty")
        data_rows = cur.fetchall()
        if len(data_rows) != 0:
            self.Faculty_table.delete(*self.Faculty_table.get_children())
            for data_row in data_rows:
                self.Faculty_table.insert("", END, values=data_row)
            conn.commit()
        conn.close()

    # ================================Faculty Update Functionalities===============================
    def update_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute(
            "update faculty set Faculty_name=%s,DOB=%s,DOJ=%s,Designation=%s,Faculty_Type=%s, Marital_Status=%s,Gender=%s,Area_Specialization=%s, Contact_No=%s, Email_id=%s where Faculty_Id=%s",
            (self.fname_var.get(), self.fdob_var.get(), self.fdoj_var.get(), self.fdesignation_var.get(),
             self.ftype_var.get(),
             self.married_var.get(), self.Gender_var.get(), self.areaspl_var.get(), self.fcontact_var.get(),
             self.femail_var.get(), self.fid_var.get()))

        conn.commit()
        self.Fetch_Data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Record has been Successfully Updated!!!")

    # =======================================Faculty Delete Functionalities==========================
    def delete_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("delete from faculty where faculty_Id=%s", self.fid_var.get())
        conn.commit()
        conn.close()
        self.Fetch_Data()
        self.reset()
        messagebox.showinfo("Success", "Record has been deleted Successfully!!!")
    # ====================================Faculty Search Functionalities==============================
#=========================================End of Faculty Functionalities==============================
#===============================Student View Functionalities Dashboard================================
class Student_View:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard/Student")
        self.root.geometry("1365x695+0+0")
        root.resizable(height=True, width=True)
        self.helv36 = tkFont.Font(family='Comic Sans MS', size=17, weight=tkFont.BOLD)
        self.title = Label(self.root, text="Personal Student Dashboard",
                           font=("times new roman", 30, "bold"), bd=7, relief="ridge", fg="yellow", bg="#456c89").pack(
            side=TOP, fill=X)

        self.STable_frame = Frame(self.root, bd=7, relief="ridge")
        self.STable_frame.place(x=0, y=70, width=1363, height=630)

        self.welstd = Label(self.STable_frame, text="Welcome\n Zeeshan Ahmad!!",
                           font=self.helv36, bd=2, relief="flat", bg="#42f5e9")
        self.welstd.place(x=0,y=2)

        self.viewdetailstudent = Button(self.STable_frame, text="View\nDetails",bg="#42f5e9",
                             relief="raised", bd=3, font=self.helv36, command=self.fetch_student)
        self.viewdetailstudent.place(x=330, y=2, height=70, width=135)

        self.attendancestudent = Button(self.STable_frame, text="Student\nAttendance", bg="#42f5e9",
                                        relief="raised", bd=3, font=self.helv36, command=self.attendancestudent)
        self.attendancestudent.place(x=580, y=2, height=70, width=135)

        self.resultstudent = Button(self.STable_frame, text="View\nResults", bg="#42f5e9",
                                        relief="raised", bd=3, font=self.helv36, command=self.studentresults)
        self.resultstudent.place(x=830, y=2, height=70, width=135)

        self.backbutton = Button(self.STable_frame, text="Exit", bg="#42f5e9",
                                        relief="raised", bd=3, font=self.helv36, command=self.exitstudent)
        self.backbutton.place(x=1080, y=2, height=70, width=135)

        self.studentdetail_frame = LabelFrame(self.STable_frame, bd=7, text="Your Record", font=("times new roman", 15, "bold"),
        fg="white", relief="ridge", bg="#686d65")
        self.studentdetail_frame.place(x=1, y=150, width=1344, height=462)

        s = ttk.Style(root)
        s.theme_use('classic')
        s.configure(".", font=("helvetica", 11), fg='red')
        s.configure("Treeview.Heading", fg="red", font=("helvetica", 11, 'bold'))
        self.studentviewTable_frame = Frame(self.studentdetail_frame, bd=2, relief="ridge")
        self.studentviewTable_frame.place(x=0, y=0, width=1328, height=429)

        scroll_x = Scrollbar(self.studentviewTable_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = Scrollbar(self.studentviewTable_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.Studentview_table = ttk.Treeview(self.studentviewTable_frame,
        columns=("userid", "Redg_no", "Name", "fname", "course", "sdob", "gender",
        "Contact", "email"), xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.Studentview_table.xview)
        scroll_y.config(command=self.Studentview_table.yview)
        self.Studentview_table.heading("userid", text="Student Id", anchor=CENTER)
        self.Studentview_table.heading("Redg_no", text="Registration Number", anchor=CENTER)
        self.Studentview_table.heading("Name", text="Name of Student", anchor=CENTER)
        self.Studentview_table.heading("fname", text="Father's name", anchor=CENTER)
        self.Studentview_table.heading("course", text="Course", anchor=CENTER)
        self.Studentview_table.heading("sdob", text="Date of Birth", anchor=CENTER)
        self.Studentview_table.heading("gender", text="Gender", anchor=CENTER)
        self.Studentview_table.heading("Contact", text="Contact number", anchor=CENTER)
        self.Studentview_table.heading("email", text="Email id", anchor=CENTER)
        self.Studentview_table["show"] = "headings"
        self.Studentview_table.pack(fill=BOTH, expand=1)
        #self.fetch_student()

    def attendancestudent(self):
        messagebox.showwarning("Warning", "Under Development")
    def studentresults(self):
        messagebox.showinfo("OOPS", "No Records Found")
    def exitstudent(self):
        self.root.destroy()
    def fetch_student(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="departmental_data")
        cur = conn.cursor()
        cur.execute("select * from newstudent where Contact_Number='9991898294' and Email_id='zeeshan@gmail.com'")
        data_rows = cur.fetchall()
        if len(data_rows) != 0:
            self.Studentview_table.delete(*self.Studentview_table.get_children())
            for row in data_rows:
                self.Studentview_table.insert("", END, values=row)
        conn.commit()
        conn.close()






#=======================================================================================================

if __name__=="__main__":
    front_page=Tk()
    obj1=Dashboard(front_page)
    #obj1.exitwindow()   #fucntion calling
    #obj1.Reset()
    obj1.login_button()
    obj1.clocktick()
    front_page.mainloop()

#ok i will run this project wait please


