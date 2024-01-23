using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace homework_4
{
    internal class VectorArray<T>
    {
        private T[] _array = Array.Empty<T>();

        public int Size { get; private set; } = 0;

        public int Copasity => _array.Length;

        public T this[int index] => _array[index];

        private int _increment = 10;

        public void add(T item, int index)
        {

            ResizeUp();
            
            for (int i = Size; i > index; i--)
            {
                _array[i] = _array[i-1];
            }

            _array[index] = item;
            
            Size++;
        }

        public void ResizeUp()
        {
            if (Size != Copasity)
            {
                return;
            }

            T[] tmpArr = new T[Size + _increment];


            for (int i = 0; i < Size; i++)
            {
                tmpArr[i] = _array[i];
            }

            _array = tmpArr;
        }


        public T remove(int index)
        {
            T[] tmpArr = new T[Copasity];
            T item = _array[index];

            int offset = 0;

            for (int i = 0; i < Size; i++)
            {
                if (i == index)
                {
                    offset = 1;
                    continue;
                }
                tmpArr[i-offset] = _array[i];
            }
            
            _array = tmpArr;
            Size--;

            return item;
        }
    }
}
