
using homework_4;

FactorArray<int> array = new FactorArray<int>();

void printArr(FactorArray<int> array)
{
    string arr = "[";

    for (int i = 0; i < array.Size; i++)
    {
        arr += array[i].ToString();
        if (i != array.Size - 1)
        {
            arr += ", ";
        }
    }

    arr += "]";
    Console.WriteLine(arr);
}

for (int i = 0; i < 10; i++)
{
    array.add(i, i);
}

array.add(15, 4);
//Console.WriteLine(array.remove(5));

printArr(array);


Console.ReadKey();