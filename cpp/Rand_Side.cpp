#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

void interpolate(vector<float> &A)
{
	int n = A.size();
	for (int i = 1; i < 2 * n - 1; i += 2)
		A.insert(A.begin() + i, (A[i] + A[i - 1]) / 2.0);
}


void interpolate2(vector<float> &A, int dt) // dt - íà ñêîëüêî çíà÷åíèé óïëîòíÿòü ìàññèâ
{
	vector<float> A_COPY = A;
	A.clear();
	//int n = A.size();
	float u = (float) (A.size() - 1) / (dt + 1);
	vector<float> T(dt);
	vector<float> FT(dt);
	for (int i = 0; i < dt; i++)
	{
		T[i] = u * (i + 1);
		if (floor(T[i]) != ceil(T[i]))
		{
			float x1 = floor(T[i]),
				  x2 = ceil(T[i]),
				  y1 = A[(int)x1],
				  y2 = A[(int)x2];
			FT[i] = y1 + (y2 - y1) / (x2 - x1) * (T[i] - x1);
		}
		else
		{
			float
				x1 = T[i] - 1,
				x2 = T[i],
				x3 = T[i] + 1,
				y1 = A[(int)x1],
				y2 = A[(int)x2],
				y3 = A[(int)x3];
			
		}
	}

	for (int i = 0; i < dt; i++)
	{
		T[i] += i;
		A.insert(A.begin() + (int)ceil(T[i]), FT[i]);
	}
	cout << endl;
	//for (int i = 1; i < 2 * n - 1; i += 2)
	//	A.insert(A.begin() + i, (A[i] + A[i - 1]) / 2.0);
}

int main()
{
	int n = 10;
	vector<float> A(n);

	for (int i = 0; i < A.size(); i++)
	{
		A[i] = 1.0 /(i+1);
		cout << A[i] << ' ';
	}
	cout << endl << endl;

	interpolate2(A, 3);
	for (int i = 0; i < A.size(); i++)
	{
		cout << A[i] << ' ';
	}
	//cout << floor(5.52) << ceil(5.52);
	system("pause");
	return 0;
}
