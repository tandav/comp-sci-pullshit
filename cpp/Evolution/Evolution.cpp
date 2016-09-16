#include "Vehicle.h"
//#include <math.h>

Vehicle vh;
float WinWid = 1366;//Ширина окна
float WinHei = 700;//Высота окна



bool mutation_good = false;


void Draw()
{
	glClear(GL_COLOR_BUFFER_BIT); // очистка экрана
	
	vh.drawVeh();

	glutSwapBuffers();
}


void Timer(int = 0) // Один пробег через void Timer значит, что прошла одна единица времени
{
	vh.moveVeh();
	Draw();
	vh.optimize();


	glutTimerFunc(0, Timer, 0);
}


void Initialize()
{
	glClearColor(0, 0, 0, 1.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-30, 10000, -100, 250, -200.0, 200.0);
}


int main(int argc, char** argv)
{
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