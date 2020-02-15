using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int L = int.Parse(Console.ReadLine());
        int H = int.Parse(Console.ReadLine());
        string T = Console.ReadLine();

        int[] I = Aorder(T);
        List<char> list = new List<char>();

        for (int i = 0; i < H; i++)
        {
            string ROW = Console.ReadLine();
            char[] C = ROW.ToCharArray();

            for (int j = 0 ; j < C.Length ; j++){
                list.Add(C[j]);
            }
        }
        for(int k = 0; k < H ;k++){
            for (int i = 0; i < I.Length; i++){
                for (int j = 0; j < L; j++){
                    Console.Write(list[(L * I[i]) + j + (k* (L*27) )  ]);
                }
            }Console.WriteLine();
        }
    }
    public static int[] Aorder(string T)
    {
        char[] C = T.ToCharArray();
        int[] I = new int[C.Length];

        for(int i = 0; i < C.Length ; i++)
        {
            if (Convert.ToInt32(C[i]) >= 65 && Convert.ToInt32(C[i]) <= 90)
                I[i] = Convert.ToInt32(C[i]) - 65;

            else if (Convert.ToInt32(C[i]) >= 97 && Convert.ToInt32(C[i]) <= 122)
                I[i] = Convert.ToInt32(C[i]) - 97;

            else I[i] = 26;
        }
        return I;
    }
}