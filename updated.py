from tkinter import *
from tkinter import ttk, messagebox
from sql_connection import get_sql_connection

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title('Hospital Management System')
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        label_title = Label(self.root, bd=20, relief='ridge', text='Hospital Management System', fg='red', bg='white', font=("Times New Roman", 50, "bold"))
        label_title.pack(side=TOP, fill=X)

        # ========================= Dataframe =========================
        Dataframe = Frame(self.root, bd=20, relief='ridge')
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief='ridge', padx=10, font=("Times New Roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief='ridge', padx=10, font=("Times New Roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ========================= ButtonFrame =========================
        Buttonframe = Frame(self.root, bd=10, relief='ridge')
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ======================== Details Frame ========================
        Detailsframe = Frame(self.root, bd=10, relief='ridge')
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ======================= Data Frame Left =======================
        lblNameTablet = Label(DataframeLeft, text="Name of Tablet", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly", font=("Arial", 12, "bold"), width=33)
        comNametablet["values"] = ("Acetaminophen", "Adderall", "Amitriptyline", "Amlodipine", "Amoxicillin", "Ativan", "Atorvastatin", "Azithromycin")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Reference No: ", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, textvariable=self.ref, font=("Arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Dose: ", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, textvariable=self.Dose, font=("Arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablet = Label(DataframeLeft, font=("Arial", 12, "bold"), text="No of Tablets: ", padx=2, pady=6)
        lblNoOftablet.grid(row=3, column=0, sticky=W)
        txtNoOftablet = Entry(DataframeLeft, textvariable=self.NumberofTablets, font=("Arial", 13, "bold"), width=35)
        txtNoOftablet.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Lot: ", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, textvariable=self.Lot, font=("Arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Issue Date: ", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, textvariable=self.IssueDate, font=("Arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Exp. Date: ", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, textvariable=self.ExpDate, font=("Arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Daily Dose: ", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, textvariable=self.DailyDose, font=("Arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Side Effect: ", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, textvariable=self.sideEffect, font=("Arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        lblfurtherinfo = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Further Information: ", padx=6)
        lblfurtherinfo.grid(row=0, column=2, sticky=W)
        txtfurtherinfo = Entry(DataframeLeft, textvariable=self.FurtherInformation, font=("Arial", 13, "bold"), width=35)
        txtfurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Blood Pressure: ", padx=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("Arial", 13, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Storage Advice: ", padx=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, textvariable=self.StorageAdvice, font=("Arial", 13, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Medication: ", padx=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, textvariable=self.HowToUseMedication, font=("Arial", 13, "bold"), width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Patient Id: ", padx=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, textvariable=self.PatientId, font=("Arial", 13, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("Arial", 12, "bold"), text="NHS Number: ", padx=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, textvariable=self.nhsNumber, font=("Arial", 13, "bold"), width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Patient Name: ", padx=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, textvariable=self.PatientName, font=("Arial", 13, "bold"), width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Date of Birth: ", padx=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, textvariable=self.DateOfBirth, font=("Arial", 13, "bold"), width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("Arial", 12, "bold"), text="Patient Address: ", padx=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, textvariable=self.PatientAddress, font=("Arial", 13, "bold"), width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ======================= Data Frame Right =======================
        self.txtPrescription = Text(DataframeRight, font=("Arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ========================== Buttons ============================
        btnPrescription = Button(Buttonframe, command=self.iPrescriptionData, text="Prescription", bg="green", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, command=self.iPrescription, text="Show Data", bg="blue", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data, text="Update", bg="yellow", fg="black", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.idelete, text="Delete", bg="red", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.clear, text="Clear", bg="purple", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, command=self.iExit, text="Exit", bg="black", fg="white", font=("Arial", 12, "bold"), width=23, height=1, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ========================== Scroll Bar ==========================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsNumber", "patientname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsNumber", text="NHS Number")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsNumber", width=100)
        self.hospital_table.column("patientname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def iPrescriptionData(self):
        if self.ref.get() == "" or self.PatientId.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = get_sql_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO hospital (nameoftablets, ref, dose, nooftablets, lot, issuedate, expdate, dailydose, storage, nhsNumber, patientname, dob, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                ))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")

    def fetch_data(self):
        try:
            conn = get_sql_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hospital")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}")

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def update_data(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            try:
                conn = get_sql_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE hospital SET nameoftablets=%s, dose=%s, nooftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsNumber=%s, patientname=%s, dob=%s, address=%s WHERE ref=%s", (
                    self.Nameoftablets.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                    self.ref.get()
                ))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Record has been updated successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")

    def idelete(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
        else:
            try:
                conn = get_sql_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM hospital WHERE ref=%s", (self.ref.get(),))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Record has been deleted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

    def iPrescription(self):
        self.txtPrescription.insert(END, f"Name of Tablets: {self.Nameoftablets.get()}\n")
        self.txtPrescription.insert(END, f"Reference No: {self.ref.get()}\n")
        self.txtPrescription.insert(END, f"Dose: {self.Dose.get()}\n")
        self.txtPrescription.insert(END, f"No of Tablets: {self.NumberofTablets.get()}\n")
        self.txtPrescription.insert(END, f"Lot: {self.Lot.get()}\n")
        self.txtPrescription.insert(END, f"Issue Date: {self.IssueDate.get()}\n")
        self.txtPrescription.insert(END, f"Exp Date: {self.ExpDate.get()}\n")
        self.txtPrescription.insert(END, f"Daily Dose: {self.DailyDose.get()}\n")
        self.txtPrescription.insert(END, f"Storage: {self.StorageAdvice.get()}\n")
        self.txtPrescription.insert(END, f"NHS Number: {self.nhsNumber.get()}\n")
        self.txtPrescription.insert(END, f"Patient Name: {self.PatientName.get()}\n")
        self.txtPrescription.insert(END, f"DOB: {self.DateOfBirth.get()}\n")
        self.txtPrescription.insert(END, f"Address: {self.PatientAddress.get()}\n")


if __name__ == "__main__":
    root = Tk()
    Hospital(root)
    root.mainloop()
