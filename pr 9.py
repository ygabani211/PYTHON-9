import pandas as pd
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        self.current_figure = None

    def create_plot(self, df, plot_type, x_col=None, y_col=None):
        """Generates different types of plots based on user choice."""
        plt.figure() 
        try:
            if plot_type == '1': 
                self.current_figure = df.plot(kind='bar', x=x_col, y=y_col).get_figure()
            elif plot_type == '2': 
                self.current_figure = df.plot(kind='line', x=x_col, y=y_col).get_figure()
            elif plot_type == '3': 
                self.current_figure = df.plot(kind='scatter', x=x_col, y=y_col).get_figure()
            elif plot_type == '4': 
                self.current_figure = df.plot(kind='pie', y=y_col).get_figure()
            elif plot_type == '5': 
                self.current_figure = df.plot(kind='hist', y=y_col).get_figure()
            elif plot_type == '6': 
                self.current_figure = df.plot(kind='area', stacked=True).get_figure()
                
            plt.show()
            return True
        except Exception as e:
            print(f"Error generating plot: {e}. Please check your column names.")
            return False

    def save_plot(self, filename):
        """Saves the most recently generated plot."""
        if self.current_figure is None:
            print("No visualization to save. Please generate a plot first.")
            return
        
        try:
            self.current_figure.savefig(filename)
            print(f"Visualization saved as {filename} successfully!")
        except Exception as e:
            print(f"Error saving file: {e}")

class SalesDataAnalyzer:
    def __init__(self):
        self.df = None
        self.viz = Visualizer()

    def load_dataset(self):
        print("\n== Load Dataset ==")
        file_path = input("Enter the path of the dataset (CSV file): ")
        try:
            self.df = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("Error: File not found. Please check the path.")
        except Exception as e:
            print(f"Error: {e}")

    def explore_data(self):
        if self.df is None:
            print("Please load a dataset first (Option 1).")
            return

        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(self.df.head())
        elif choice == '2':
            print(self.df.tail())
        elif choice == '3':
            print(self.df.columns.tolist())
        elif choice == '4':
            print(self.df.dtypes)
        elif choice == '5':
            self.df.info()
        else:
            print("Invalid choice.")

    def perform_dataframe_operations(self):
        if self.df is None:
            print("Please load a dataset first.")
            return
        print("\n== Perform DataFrame Operations ==")
        # Example operation: Sorting by Sales
        try:
            print("Sorted by Sales descending:")
            print(self.df.sort_values(by='Sales', ascending=False).head())
        except KeyError:
            print("Sales column not found for sorting.")

    def handle_missing_data(self):
        if self.df is None:
            print("Please load a dataset first.")
            return

        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            missing_rows = self.df[self.df.isnull().any(axis=1)]
            if missing_rows.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing_rows)
        elif choice == '2':
            numeric_cols = self.df.select_dtypes(include=['number']).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
            print("Missing values filled with mean successfully!")
        elif choice == '3':
            self.df.dropna(inplace=True)
            print("Rows with missing values dropped successfully!")
        elif choice == '4':
            val = input("Enter the value to replace missing data with: ")
            self.df.fillna(val, inplace=True)
            print("Missing values replaced successfully!")

    def generate_statistics(self):
        if self.df is None:
            print("Please load a dataset first.")
            return
        print("\n== Generate Descriptive Statistics ==")
        print(self.df.describe(include='all'))

    def data_visualization(self):
        if self.df is None:
            print("Please load a dataset first.")
            return

        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        
        choice = input("Enter your choice: ")
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice.")
            return

        if choice in ['1', '2', '3']:
            print(f"\n== {['Bar', 'Line', 'Scatter'][int(choice)-1]} Plot ==")
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ")
            print("Generating plot...")
            success = self.viz.create_plot(self.df, choice, x_col, y_col)
            if success:
                print(f"{['Bar', 'Line', 'Scatter'][int(choice)-1]} plot displayed successfully!")
        elif choice == '4':
            print("\n== Pie Chart ==")
            y_col = input("Enter column name for pie chart slices: ")
            print("Generating pie chart...")
            if self.viz.create_plot(self.df, choice, y_col=y_col):
                print("Pie chart displayed successfully!")
        elif choice == '5':
            print("\n== Histogram ==")
            y_col = input("Enter column name for histogram: ")
            print("Generating histogram...")
            if self.viz.create_plot(self.df, choice, y_col=y_col):
                print("Histogram displayed successfully!")
        elif choice == '6':
            print("\n== Stack Plot ==")
            print("Generating stack plot...")
            if self.viz.create_plot(self.df, choice):
                print("Stack plot displayed successfully!")

    def save_visualization(self):
        print("\n== Save Visualization ==")
        filename = input("Enter file name to save the plot (e.g., scatter_plot.png): ")
        self.viz.save_plot(filename)

def main():
    analyzer = SalesDataAnalyzer()
    
    while True:
        print("\n" + "="*50)
        print("Data Analysis & Visualization Program")
        print("="*50)
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            analyzer.load_dataset()
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '3':
            analyzer.perform_dataframe_operations()
        elif choice == '4':
            analyzer.handle_missing_data()
        elif choice == '5':
            analyzer.generate_statistics()
        elif choice == '6':
            analyzer.data_visualization()
        elif choice == '7':
            analyzer.save_visualization()
        elif choice == '8':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()