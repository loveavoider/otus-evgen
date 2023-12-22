using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace homework_4
{
    internal class SingleArray<T>
    {

        private T[] _array = Array.Empty<T>();

        public int Size => _array.Length;

        public T this[int index] => _array[index];

        public void add(T item, int index)
        {
            ResizeUp(index);
            _array[index] = item;
        }

        public void ResizeDown(int index)
        {

            T[] tmpArr = new T[Size - 1];

            int offset = 0;

            for (int i = 0; i < _array.Length; i++)
            {
                if (i == index)
                {
                    offset = 1;
                    continue;
                }
                tmpArr[i - offset] = _array[i];
            }

            _array = tmpArr;
        }

        public void ResizeUp(int index)
        {
            T[] tmpArr = new T[Size + 1];

            int offset = 0;

            for (int i = 0; i < Size+1; i++)
            {
                if (i == index)
                {
                    offset = 1;
                    continue;
                }
                tmpArr[i] = _array[i - offset];
            }

            _array = tmpArr;
        }


        public T remove(int index)
        {
            T item = _array[index];

            ResizeDown(index);

            return item;
        }
    }
}
