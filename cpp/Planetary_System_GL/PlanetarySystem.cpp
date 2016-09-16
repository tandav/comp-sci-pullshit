#include "PlanetarySystem.h"


PlanetarySystem::PlanetarySystem(float WinWid, float WinHei, float k)
{
	N = 0;
	G = 0.0007;
	RX = WinWid*k / 2;
	RY = WinHei*k / 2;
	u = 1; // при ударе коэффициент трения, уходит на теплоту 
	mux = 1, muy = 1;
	mu = 1;
}


PlanetarySystem::~PlanetarySystem()
{
}


void  PlanetarySystem::initFromDatabase()
{
	ifstream fin;
	string line;
	fin.open("Planets_database.txt", ios::in);
	while (!fin.eof())
	{
		getline(fin, line);
		N++;
	}
	fin.seekg(0, ios::beg);

	for (int i = 0; i < N; i++)
	{
		Planet tmp_pl;
		fin >> tmp_pl.x >> tmp_pl.y >> tmp_pl.vx >> tmp_pl.vy >> tmp_pl.m >> tmp_pl.R;
		//tmp_pl.m = tmp_pl.ro * 4 / 3 * 3.14159 * tmp_pl.R * tmp_pl.R * tmp_pl.R;
		P.push_back(tmp_pl);
		cm.push_back(vector<bool>(N, 0));
	}
}
	

void PlanetarySystem::system_move()
{
	for (int i = 0; i < N; ++i) //Пробег по частицам (чтобы для каждой скорректировать координату)
	{
		Planet &p0 = P[i]; // Более короткое обозначение, ссылка: p0 = P[i]
		borders(i); // Добавить борты (закоментировать, если не нужно)
		for (int j = 0; j < N; ++j) // Пробег по частицам, которые будут действовать на данную
		{
			
			if (j == i) // Сама на себя не действует
				continue;
			collision(i, j);
			const Planet &p = P[j]; // Действущая частица[j]
			float d = sqrt((p0.x - p.x) * (p0.x - p.x) + (p0.y - p.y) * (p0.y - p.y)); // Расстояние до действующ частицы
			if (p0.vx !=0 && p0.vy != 0)
			{
				mux = 0.1292 * 3.1416 * p0.R * p0.R * p0.vx * p0.vx;
				muy = 0.1292 * 3.1416 * p0.R * p0.R * p0.vy * p0.vy;
			}

			if (d > p0.R + p.R) // Если so close, то не влияет
			{
				p0.vx += G * p.m / d / d * (p.x - p0.x) / d / mu; // последнее - косинус альфа ну можно сказать d спроецировали расстояние меньше 
				p0.vy += G * p.m / d / d * (p.y - p0.y) / d / mu; // mu - коэффициент сопротивления воздуха, при необходимости закоментить
			}
		}
		p0.x += p0.vx; // За одну единицу времени координата изменяется на значение скорости
		p0.y += p0.vy;
	}
}


void PlanetarySystem::borders(int index)
{

	if (abs(P[index].x) >= RX && P[index].x*P[index].vx > 0) P[index].vx = -u*P[index].vx;
	if (abs(P[index].y) >= RY && P[index].y*P[index].vy > 0) P[index].vy = -u*P[index].vy;

}


void PlanetarySystem::collision(int ind1, int ind2)
{
	float d = sqrt((P[ind1].x - P[ind2].x) * (P[ind1].x - P[ind2].x) + (P[ind1].y - P[ind2].y) * (P[ind1].y - P[ind2].y));
	if (d < P[ind1].R + P[ind2].R)
	{
		float
			v1x = P[ind1].vx,
			v1y = P[ind1].vy,
			v2x = P[ind2].vx,
			v2y = P[ind2].vy,
			m1 = P[ind1].m,
			m2 = P[ind2].m;

		int ind_x_min, ind_x_max, ind_y_min, ind_y_max;

		if (P[ind1].x < P[ind2].x) ind_x_min = ind1;
		else ind_x_min = ind2;

		if (P[ind1].x > P[ind2].x) ind_x_max = ind1;
		else ind_x_max = ind2;

		if (P[ind1].y < P[ind2].y) ind_y_min = ind1;
		else ind_y_min = ind2;

		if (P[ind1].y > P[ind2].y) ind_y_max = ind1;
		else ind_y_max = ind2;

		if (!cm[ind1][ind2] && (P[ind_x_min].vx > 0 || P[ind_x_max].vx < 0 || P[ind_y_min].vy > 0 || P[ind_y_max].vy < 0))
		{
			P[ind1].vx = (-v1x + 2 * (m1*v1x + m2*v2x) / (m1 + m2))*u;
			P[ind1].vy = (-v1y + 2 * (m1*v1y + m2*v2y) / (m1 + m2))*u;

			P[ind2].vx = (-v2x + 2 * (m1*v1x + m2*v2x) / (m1 + m2))*u;
			P[ind2].vy = (-v2y + 2 * (m1*v1y + m2*v2y) / (m1 + m2))*u;
			cm[ind1][ind2] = 1;
			cm[ind2][ind1] = 1;
		}
	}
	else 
	{
		cm[ind1][ind2] = 0;
		cm[ind2][ind1] = 0;
	}
}


void PlanetarySystem::drawPlanets()
{
	for (int i = 0; i < N; ++i)
	{
		drawOnePlanet(P[i].x, P[i].y, P[i].R, 20);
	}
}


void drawOnePlanet(float x, float y, float r, int amountSegments)
{
	glBegin(GL_LINE_LOOP);

	for (int i = 0; i < amountSegments; i++)
	{
		float angle = 2.0 * 3.1415926 * float(i) / float(amountSegments);

		float dx = r * cosf(angle);
		float dy = r * sinf(angle);
		glVertex2f(x + dx, y + dy);
	}

	glEnd();
}


float max(float a, float b)
{
	if (a > b) return a; 
	else return b;
}


float min(float a, float b)
{
	if (a < b) return a;
	else return b;
}