from codecs import escape_encode
from datetime import datetime
from email import message
from msilib.schema import CheckBox
from pathlib import Path
import csv
import tkinter as tk
from tkinter import Checkbutton, ttk

from numpy import datetime_as_string


class BoundText(tk.Text):
    """A Text widget with a bound variable."""
    """
    Needs
    1. pass in a StringVar
    2. update the widget contents
    3. update the variable contents
    """

    def __init__(self, *args, textvariable=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._variable = textvariable
        """needs 1"""

        if self._variable:
            self.insert('1.0', self._variable.get())
            # needs 2
            self._variable.trace_add('write', self._set_content)

            # needs 3
            self.bind('<<Modified>>', self._set_var)

    """needs 3"""

    def _set_var(self, *_):
        if self.edit_modified():
            content = self.get('1.0', 'end-1chars')
            self._variable.set(content)
            self.edit_modified(False)

    """needs 2"""

    def _set_content(self, *_):
        """Set the text contents to the variable"""
        self.delete('1.0', tk.END)
        self.insert('1.0', self._variable.get())


#########################################
# Creating a LabelInput compound widget #
#########################################
class LabelInput(tk.Frame):

    def __init__(
            self,
            parent,
            label,
            var,
            input_class=ttk.Entry,
            input_args=None,
            label_args=None,
            **kwargs
    ):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = var
        self.variable.label_widget = self

        if input_class in (ttk.Checkbutton, ttk.Button):
            input_args["text"] = label
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W+tk.E))

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["variable"] = self.variable
        else:
            input_args["textvariable"] = self.variable

        if input_class == ttk.Radiobutton:
            self.input = tk.Frame(self)
            for v in input_args.pop('value', []):
                button = ttk.Radiobutton(
                    self.input, value=v, text=v, **input_args
                )
                button.pack(
                    side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x'
                )
        else:
            self.input = input_class(self, **input_args)

        self.input.grid(row=1, column=0, sticky=(tk.W+tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E+tk.W), **kwargs):
        super().grid(sticky=sticky, **kwargs)


#######################################
# Building our application components #
#######################################

class DataRecordForm(ttk.Frame):
    def _add_frame(self, label, cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W+tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._vars = {
            'Date': tk.StringVar(),
            'Time': tk.StringVar(),
            'Technician': tk.StringVar(),
            'Lab': tk.StringVar(),
            'Plot': tk.IntVar(),
            'Seed Sample': tk.StringVar(),
            'Humidity': tk.DoubleVar(),
            'Light': tk.DoubleVar(),
            'Temperature': tk.DoubleVar(),
            'Equipment Fault': tk.BooleanVar(),
            'Plants': tk.IntVar(),
            'Blossoms': tk.IntVar(),
            'Fruit': tk.IntVar(),
            'Min Height': tk.DoubleVar(),
            'Max Height': tk.DoubleVar(),
            'Med Height': tk.DoubleVar(),
            'Notes': tk.StringVar()
        }

        r_info = self._add_frame("Record Information")

        # Line1
        LabelInput(
            r_info,
            "Date",
            self._vars['Date']
        ).grid(row=0, column=0)
        LabelInput(
            r_info,
            "Time",
            input_class=ttk.Combobox,
            var=self._vars['Time'],
            input_args={"values": ["8:00", "12:00", "16:00", "20:00"]}
        ).grid(row=0, column=1)
        LabelInput(
            r_info,
            "Technician",
            var=self._vars['Technician']
        ).grid(row=0, column=2)

        # Line2
        LabelInput(
            r_info,
            "Lab",
            input_class=ttk.Radiobutton,
            var=self._vars['Lab'],
            input_args={"values": ["A", "B", "C"]}
        ).grid(row=1, column=0)
        LabelInput(
            r_info,
            "Plot",
            input_class=ttk.Combobox,
            var=self._vars['Plot'],
            input_args={"values": list(range(1, 21))}
        ).grid(row=1, column=1)
        LabelInput(
            r_info,
            "Seed Sample",
            var=self._vars['Seed Sample']
        ).grid(row=1, column=2)

        e_info = self._add_frame("Environment Data")

        LabelInput(
            e_info,
            "Humidity (g/m³)",
            input_class=ttk.Spinbox,
            var=self._vars['Humidity'],
            input_args={"from_": 0.5, "to": 52.0, "increment": .01}
        ).grid(row=0, column=0)
        LabelInput(
            e_info,
            "Light (kix)",
            input_class=ttk.Spinbox,
            var=self._vars['Light'],
            input_args={"from_": 0, "to": 100, "increment": .01}
        ).grid(row=0, column=1)
        LabelInput(
            e_info,
            "Temperature (°C)",
            input_class=ttk.Spinbox,
            var=self._vars['Temperature'],
            input_args={"from_": 4, "to": 40, "increment": .01}
        ).grid(row=0, column=2)
        LabelInput(
            e_info,
            "Equipment Fault",
            input_class=ttk.Checkbutton, #if < ttk. ? is not, checkbutton is independently working
            var=self._vars['Equipment Fault']
        ).grid(row=1, column=0, columnspan=3)

        p_info = self._add_frame("Plant Data")

        LabelInput(
            p_info,
            "Plants",
            input_class=ttk.Spinbox,
            var=self._vars['Plants'],
            input_args={"from_": 0, "to": 20}
        ).grid(row=0, column=0)
        LabelInput(
            p_info,
            "Blossoms",
            input_class=ttk.Spinbox,
            var=self._vars['Blossoms'],
            input_args={"from_": 0, "to": 1000}
        ).grid(row=0, column=1)
        LabelInput(
            p_info,
            "Fruit",
            input_class=ttk.Spinbox,
            var=self._vars['Fruit'],
            input_args={"from_": 0, "to": 1000}
        ).grid(row=0, column=2)

        # Height data
        LabelInput(
            p_info,
            "Min Height (cm)",
            input_class=ttk.Spinbox,
            var=self._vars['Min Height'],
            input_args={"from_": 0, "to": 1000, "increment": .01}
        ).grid(row=1, column=0)
        LabelInput(
            p_info,
            "Max Height (cm)",
            input_class=ttk.Spinbox,
            var=self._vars['Max Height'],
            input_args={"from_": 0, "to": 1000, "increment": .01}
        ).grid(row=1, column=1)
        LabelInput(
            p_info,
            "Median Height (cm)",
            input_class=ttk.Spinbox,
            var=self._vars['Med Height'],
            input_args={"from_": 0, "to": 1000, "increment": .01}
        ).grid(row=1, column=2)

        LabelInput(
            self,
            "Notes",
            input_class=BoundText,
            var=self._vars['Notes'],
            input_args={"width": 75, "height": 10}
        ).grid(sticky=tk.W+tk.E, row=3, column=0)

        buttons = tk.Frame(self)
        buttons.grid(sticky=tk.W+tk.E, row=4)
        self.savebutton = ttk.Button(
            buttons,
            text="Save",
            command=self.master._on_save
        )
        self.savebutton.pack(side=tk.RIGHT)

        self.resetbutton = ttk.Button(
            buttons,
            text="Reset",
            command=self.reset
        )
        self.resetbutton.pack(side=tk.RIGHT)

    def reset(self):
        for var in self._vars.values():
            if isinstance(var, tk.BooleanVar):
                var.set(False)
            else:
                var.set('')

    def get(self):
        data = dict()
        fault = self._vars['Equipment Fault'].get()
        for key, variable in self._vars.items():
            if fault and key in ('Light', 'Humidity', 'Temperature'):
                data[key] = ''
            else:
                try:
                    data[key] = variable.get()
                except tk.TclError:
                    message = f'Error in field: {key}. Data was not saved!'
                    raise ValueError(message)

        return data



class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ABQ Data Entry Application")
        self.columnconfigure(0, weight=1)

        ttk.Label(
            self,
            text="ABQ Data Entry AP",
            font=("TKDefaultFont", 16)
        ).grid(row=0)

        self.recordform = DataRecordForm(self)
        self.recordform.grid(row=1, padx=10, sticky=tk.W+tk.E)

        self.status = tk.StringVar()
        ttk.Label().grid(sticky=tk.W+tk.E, row=2, padx=10)

        self._records_saved = 0

    def _on_save(self):
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "abq_data_record_{}.csv".format(datestring)
        newfile = not Path(filename).exists()

        try:
            data = self.recordform.get()

        except ValueError as e:
            self.status.set(str(e))
            return

        with open(filename, 'a', newline='') as fh:
            csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
            if newfile:
                csvwriter.writeheader()
            csvwriter.writerow(data)

        self._records_saved += 1
        self.status.set(
            "{} records saved this session".format(self._records_saved)
        )
        self.recordform.reset()


if __name__ == "__main__":

    app = Application()
    app.mainloop()
