##  Approaches considered

1 CSV Module Approach

2 Machine Learning Algorithm approach

## document any assumptions made and why

 Assumed that the CSV file follows a specific format with columns "start_time", "end_time", "speaker", and "text" in that order.

## Selected Approach

The CSV Module Approach was chosen for its simplicity and built-in functionality. It allows for straightforward reading of CSV files, access to column values by name, and easy processing of each row. The CSV Module Approach suffices for the given task of reading and processing a relatively simple CSV file structure.

## what are the limitations of the current approach

 The csv module has limited support for different file encodings. I requires that the CSV file is encoded using the default system encoding. If a CSV file uses  different encoding, we may need to handle the encoding conversion separately.