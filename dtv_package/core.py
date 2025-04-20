import pandas as pd
import matplotlib.pyplot as plt

class Info:     #doesn't create an instance, because not necessary
    @staticmethod       # says: next "method is separate from instance (=self)"
    def get_cr(dt):
        """Get database shape"""
        return [dt.shape[0], dt.shape[1]]     #(rows, columns)

    @staticmethod
    def get_na(dt):
        """Check and counts NaN"""
        if sum(dt.isna().sum()) == 0:
            return "No NaN found"
        else:
            return dt.isna()

    @staticmethod
    def get_dtypes(dt):
        """Check dtypes, retrieves them, check how many times they occur"""
        my_dictionary = dict()
        for i in dt:
            series = dt[i].apply(type)  # series with dtype-values for every element in column i
            unique_series = set(series)  # create a variable for that dtype from "series"; that's why set; because it's unqiue

            my_dictionary[i] = list(unique_series)  # adds key-value pair to dictionary; looks like this: "column": [<dtype>]

            """goal output: 'column': [<data_type>] <-- dictionary"""
        return pd.DataFrame(my_dictionary)

    @staticmethod
    def collect(dataF):
        """collects values from previous functions about our data; returns collection"""
        shape = Info.get_cr(dataF)
        na_n = Info.get_na(dataF)
        dtypes = Info.get_dtypes(dataF)

        header = dataF.head()

        return f"{header} \n \n ---> [rows, columns]: {shape} \n ---> NaN: {na_n} \n \n {dtypes}"      #\n to skip lines; more readable

class Draw:
    @staticmethod
    def plot_columns(dataF, cl_list):

        """for specific columns - draw diagram"""
        x = range(len(dataF))
        for column in cl_list:
            y = dataF[column]
            plt.scatter(x, y)
            plt.suptitle(column)

            plt.show()




if __name__ == "__main__":
    # Größere Beispiel-Daten erstellen
    data = {
        "A": [i for i in range(1, 21)],  # Zahlen von 1 bis 20
        "B": [i * 2 for i in range(1, 21)],  # Zahlen von 2 bis 40 (Verdopplung)
        "C": [i ** 2 for i in range(1, 21)],  # Quadratzahlen
        "D": [None if i % 5 == 0 else i for i in range(1, 21)]  # NaN für Vielfache von 5
    }
    df = pd.DataFrame(data)

    # Funktionen testen
    print("=== Informationen über den DataFrame ===")
    print(Info.collect(df))

    # Diagramme zeichnen
    print("\n=== Diagramme werden erstellt ===")
    Draw.plot_columns(df, ["A", "B", "C", "D"])


if __name__ == "__main__":
    print("Debug: Der Code wird ausgeführt!")