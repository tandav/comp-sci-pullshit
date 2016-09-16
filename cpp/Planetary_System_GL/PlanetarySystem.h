#pragma once
#include <iostream>
#include <vector>
#include <fstream> 
#include <string>
#include <gl/glut.h>
using namespace std;

struct Planet
{
	float x;
	float y;
	float vx;
	float vy;
	float ro;
	float R;
	float m;
};

class PlanetarySystem
{
	int N; // Number of planets in the system 
	vector <Planet> P;
	vector<vector<bool> > cm; // collision matrix
	float G;
	float RX, RY; // Screen radius
	float u; // при ударе коэффициент трения, уходит на теплоту
	float mux, muy; // сопротивление воздуха
	float mu;
public:

	PlanetarySystem(float, float, float);
	~PlanetarySystem();
	void initFromDatabase();
	void system_move(); // function of all planet dx'es and dy'es per time unit
	void borders(int);
	void collision(int, int);
	void drawPlanets(); // Аргументы - P (там наверное указатель или ссылка, а может быть и нет)
};

void drawOnePlanet(float x, float y, float r, int amountSegments);
float max(float a, float b);
float min(float a, float b);