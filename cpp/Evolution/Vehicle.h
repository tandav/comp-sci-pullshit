#pragma once
#include <iostream>
#include <vector>
#include <time.h>
//#include <cmath>
#include <gl/glut.h>

using namespace std;




class Vehicle
{
	vector<float> F_Best;
	float Mut_dens = 0.93, Mut_radius = 0.81;
	float smax = 0;
	unsigned int t = 0;
	float x, vx;
	int car_size;
	unsigned int dt;
	vector<float> F;
	vector<float> V;
	vector<float> X;

public:
	Vehicle();
	~Vehicle();
	void set_default();
	void moveVeh();
	bool isMove();
	void drawVeh();
	void mutation(float a, float b, float dens);
	void optimize();
};

