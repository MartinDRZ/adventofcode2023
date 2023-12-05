using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Microsoft.VisualBasic;

String line;
var inputList = new List<string>();
String[] inputArray;
String[][] formattedArray;

try
{
    //Pass the file path and file name to the StreamReader constructor
    StreamReader sr = new StreamReader("input.txt");
    //Read the first line
    line = sr.ReadLine();
    //Continue to read lines until there are no more lines
    while (line != null)
    {
        //add the line to the list
        inputList.Add(line);
        //Read the next line
        line = sr.ReadLine();
    }
    //close the file
    sr.Close();
}
catch (Exception e)
{
    Console.WriteLine("Exception: " + e.Message);
}
finally
{
    Console.WriteLine("Input file read");
}

inputArray = inputList.ToArray();

Console.WriteLine("Array Created");

for (int i = 0; i < inputArray.Length; i++)
{

}