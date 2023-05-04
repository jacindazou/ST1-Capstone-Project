import tkinter as tk
# import faulthandler
# faulthandler.enable()
# import matplotlib
# matplotlib.use("TkAgg")
import shop_value_customer_classifier_model
from shop_value_customer_classifier_model import best_model, model_accuracy

class SCV_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Customer Value Predictor")

        # Create frames to group widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()

        # Create the widgets for one frame. (title display)
        self.title_label = tk.Label(self.one_frame, text='VALUED CUSTOMER PREDICTOR',fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()


        # Create the widgets for two frame. (age input)
        self.age_label = tk.Label(self.two_frame, text='Age:')
        self.age_entry = tk.Entry(self.two_frame, bg="white", fg="black", width = 10)
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')



        # Create the widgets for three frame. (sex/gender input)
        self.sex_label = tk.Label(self.three_frame, text='Gender:')
        self.click_sex_var = tk.StringVar()
        self.click_sex_var.set("Male")
        self.sex_inp = tk.OptionMenu(self.three_frame,self.click_sex_var, "Male", "Female")
        self.sex_label.pack(side='left')
        self.sex_inp.pack(side='left')


        # Create the widgets for four frame. (Annual income input)
        self.annual_income_label = tk.Label(self.four_frame, text='Annual income:')
        self.annual_income_entry = tk.Entry(self.four_frame, bg="white", fg="black", width = 10)
        self.annual_income_label.pack(side='left')
        self.annual_income_entry.pack(side='left')

        # Create the widgets for six frame. (work exp  input)
        self.work_exp_label = tk.Label(self.five_frame, text='Work Experience(Year):')
        self.work_exp_entry = tk.Entry(self.five_frame, bg="white", fg="black")
        self.work_exp_label.pack(side='left')
        self.work_exp_entry.pack(side='left')

        # Create the widgets for seven frame. (family size  input)
        self.family_size_label = tk.Label(self.six_frame, text='Family size(people):')
        self.family_entry = tk.Entry(self.six_frame, bg="white", fg="black")
        self.family_size_label.pack(side='left')
        self.family_entry.pack(side='left')


        #Create the widgets for fifteen frame = hd (prediction of valued customer)
        self.cv_predict_ta = tk.Text(self.seven_frame,height = 10, width = 25,bg= 'light blue')

        #Create predict button and quit button
        self.btn_predict = tk.Button(self.eight_frame, text='Predict Customer Value', command=self.predict_cv)
        self.btn_quit = tk.Button(self.eight_frame, text='Quit', command=self.main_window.destroy)


        self.cv_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()

        # Pack the frames.
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()


        # Enter the tkinter main loop.
        tk.mainloop()

    def predict_cv(self):
        result_string = ""

        self.cv_predict_ta.delete(0.0, tk.END)
        customer_age = self.age_entry.get()
        customer_sex = self.click_sex_var.get()
        if(customer_sex == "Male"):
            customer_sex = 1
        else:
            customer_sex = 0

        customer_income = self.annual_income_entry.get()
        customer_work_exp = self.work_exp_entry.get()
        customer_family_size = self.family_entry.get()

        result_string += "===Patient Diagnosis=== \n"
        customer_info = (customer_age,customer_sex,customer_income, customer_work_exp,customer_family_size)


        cv_prediction = best_model.predict([customer_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = cv_prediction

        if(cv_prediction == [0]):
            result_string = (disp_string, '\n', "0 - The customer have lower chance to spending more than 50 scores")
        else:
            result_string = (disp_string, '\n'+ "1 - The customer have higher chance to spending more than 50 scores")
        self.cv_predict_ta.insert('1.0',result_string)


my_cvd_GUI = SCV_GUI()
