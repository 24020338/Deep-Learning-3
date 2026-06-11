import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <function_name>")
        return
    
    function_name = sys.argv[1]
    
    if function_name == "plot_absolute_width_horizontal":
        from plot_functions import plot_absolute_width_horizontal
        df = ...  # Load your DataFrame here
        images_dir = ...  # Set your directory path here
        plot_absolute_width_horizontal(df, images_dir)
    elif function_name == "plot_absolute_height_vertical":
        from plot_functions import plot_absolute_height_vertical
        df = ...  # Load your DataFrame here
        images_dir = ...  # Set your directory path here
        plot_absolute_height_vertical(df, images_dir)
    elif function_name == "plot_absolute_area_vertical":
        from plot_functions import plot_absolute_area_vertical
        df = ...  # Load your DataFrame here
        images_dir = ...  # Set your directory path here
        plot_absolute_area_vertical(df, images_dir)
    else:
        print(f"Invalid function name: {function_name}")

if __name__ == "__main__":
    main()