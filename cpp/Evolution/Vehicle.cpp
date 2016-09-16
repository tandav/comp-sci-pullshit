#include "Vehicle.h"


Vehicle::Vehicle()
{
	x = 0;
	vx = 0;
	dt = 0;
	car_size = 20;
	for (int i = 0; i < 20; i++)
	{
		F.push_back(5);
	}
}


void Vehicle::set_default()
{
	x = 0;
	vx = 0;
	dt = 0;
	car_size = 20;
	V.clear();
	X.clear();
}


Vehicle::~Vehicle()
{
}


void Vehicle::drawVeh()
{
	glBegin(GL_LINE_STRIP);
	for (int i = 0; i < X.size(); i++) // Drawing vx(t)
	{
		glColor3f(1.0, 0.0, 0.0);
		glVertex2d(X[i], V[i]);
	}
	glEnd();

	glBegin(GL_LINE_STRIP); //Drawing F(t)
	for (int i = 0; i < X.size() && i < F.size(); i++)
	{
		glColor3f(0.0, 1.0, 0.0);
		glVertex2d(X[i], F[i]);
	}
	glEnd();

	glColor3f(1.0, 1.0, 1.0); // Drawing car
	glBegin(GL_QUADS);
	glVertex2f(x - car_size, 0);
	glVertex2f(x + car_size, 0);
	glVertex2f(x + car_size, car_size / 2);
	glVertex2f(x - car_size, car_size / 2);
	glEnd();

	glColor4f(1.0, 1.0, 1.0, 0.1); // Drawing x-axis
	glBegin(GL_LINES);
	glVertex2f(0, 0);
	glVertex2f(200000, 0);
	glEnd();
}


void Vehicle::moveVeh()
{
	float ft = 0, fu = 0; //f tyagi, f trenya
	if (t < F.size()) 
		ft = F[t];
	else 
		dt++;
	if (vx > 0) fu = -1.5;
	if (vx < 0)
	{
		fu = 0;
		vx = 0;
	}
	
	//else if (vx < 0) fu = 0.028;
		
	vx += ft + fu; 
	V.push_back(vx);
	x += vx;
	X.push_back(x);
	//cout << vx << ' ' << "smax = " << smax << endl;
	t++;
}


bool Vehicle::isMove()
{
	if (vx) return true;
	else return false;
}


void rand_no_repeats(vector<int>& t, int sz, int a, int b)
{
	srand(time(0));
	while (t.size() < sz)
	{
		int temp = rand() % (b - a + 1) + a;
		bool exist = false;
		for (int i = 0; i < t.size(); i++)
		{
			if (t[i] == temp) exist = true;
		}
		if (!exist)
		{
			t.push_back(temp);
		}
	}
}


void dvalue(vector<float>& m, float a, float b) // , в классе не нужно никаких ссылок будет
{
	m[0] = (float)rand() * (b - a) / RAND_MAX + a;
	float sum_rand = 0;

	for (int i = 1; i < m.size(); i++)
	{
		m[i] = (float)rand() * (b - a) / RAND_MAX + a;
		sum_rand += m[i];
	}

	for (int i = 1; i < m.size(); i++)
	{
		m[i] = m[i] * -m[0] / sum_rand;
	}
}


void Vehicle::mutation(float a, float b, float dens)
{
	srand(time(0));
	int n_mut = F.size() * dens;

	vector<int> randIndexes;
	rand_no_repeats(randIndexes, n_mut, 0, F.size() - 1);
	vector<float> dv(n_mut);
	

	bool Fuel_bad = true;
	while (Fuel_bad)
	{
		dvalue(dv, a, b);
		for (int i = 0; i < n_mut; i++)
		{
			if (F[randIndexes[i]] + dv[i] < 0)
			{
				Fuel_bad = true;
				break;
			}
			else Fuel_bad = false;
		}


	}
	
	
	for (int i = 0; i < n_mut; i++)
	{
		//if (F[randIndexes[i]] + dv[i] >= 0) F[randIndexes[i]] += dv[i];
		//else
		F[randIndexes[i]] += dv[i];
	}
}


void Vehicle::optimize()
{
	if (!isMove())
	{
		if (x > smax)
		{
			smax = x;
			F_Best = F;
			mutation(-Mut_radius, Mut_radius, Mut_dens);
			set_default();
			t = 0;
		}
		else
		{
			F = F_Best;
			mutation(-Mut_radius, Mut_radius, Mut_dens);
			set_default();
			t = 0;
		}
		cout << "smax = " << smax << endl;
	}
}