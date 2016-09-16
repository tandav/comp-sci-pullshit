#include "PlanetarySystem.h"
#include <math.h>


float WinWid = 1366;//Ширина окна
float WinHei = 700;//Высота окна
float zoom = 0.5;  // больше число  - больше зум out

PlanetarySystem sol(WinWid, WinHei, zoom);


void Draw()
{
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(1.0, 0.0, 0.0);
	sol.drawPlanets();

	glutSwapBuffers();
}


void Timer(int = 0) // Один пробег через void Timer значит, что прошла одна единица времени
{
	sol.system_move();
	Draw();
	glutTimerFunc(1, Timer, 0);
}


void Initialize()
{
	glClearColor(0, 0, 0, 1.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-WinWid*zoom / 2, WinWid*zoom / 2, -WinHei*zoom / 2, WinHei*zoom / 2, -200.0, 200.0);
}


int main(int argc, char** argv)
{

	sol.initFromDatabase();

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(WinWid, WinHei);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Solar system");
	Initialize();
	glutDisplayFunc(Draw);
	Timer();
	glutMainLoop();
	return 0;
}