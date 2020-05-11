#include <iostream>
#include <fstream>

double* proizv(double** x, double* y, int m, int n) {
	double* new_arr = new double [m];

	for (size_t i = 0; i < m; i++)
		new_arr[i] = 0;

	for (size_t k = 0; k < m; k++)
		for (size_t j = 0; j < n; j++)
			for (size_t i = 0; i < m; i++)
				new_arr[k] += (x[k][i] * y[i]);

	return new_arr;
}

double** proizv(double** x, double** y, int m, int n, int p) {
	double** new_arr = new double* [m];
	for (size_t i = 0; i < m; i++)
		new_arr[i] = new double[n];

	for (size_t i = 0; i < m; i++)
		for (size_t j = 0; j < n; j++)
			new_arr[i][j] = 0;

	for (size_t k = 0; k < m; k++)
		for (size_t j = 0; j < n; j++)
			for (size_t i = 0; i < p; i++)
				new_arr[k][j] += (x[k][i] * y[i][j]);

	return new_arr;
}

double* proizv(double* x, double num, int n) {
	double* new_arr = new double [n];

	for (size_t i = 0; i < n; i++)
		new_arr[i] = x[i] * num;

	return new_arr;
}

double* sum(double* x, double* y, int n) {
	double* new_arr = new double [n];
	
	for (size_t i = 0; i < n; i++)
		new_arr[i] = x[i] + y[i];

	return new_arr;
}

double* func(double* y, double x, int num = 2) {
	double* f = new double[num];
	f[0] = y[1];
	f[1] = -y[1] + 4 * y[0] + x * exp(-x);
	return f;
}

double* func_x(double* y, double x, int num = 2) {
	double* f = new double[num];
	f[0] = -y[1] + 4 * y[0] + x * exp(-x);
	f[1] = 5 * y[1] - 4 * y[0] - (2 * x - 1) * exp(-x);
	return f;
}

double** func_y(double* y, double x, int num = 2) {
	double** f = new double* [num];
	for (size_t i = 0; i < num; i++)
		f[i] = new double[num];
	f[0][0] = -y[1] + 4 * y[0] + x * exp(-x);
	f[0][1] = -y[1] + 4 * y[0] + x * exp(-x);
	f[1][0] = 5 * y[1] - 4 * y[0] - x * exp(-x);
	f[1][1] = 5 * y[1] - 4 * y[0] - (3 * x - 1) * exp(-x);
	return f;
}

double* func_xx(double* y, double x, int num = 2) {
	double* f = new double[num];
	f[0] = 5 * y[1] - 4 * y[0] - (2 * x - 1) * exp(-x);
	f[1] = -9 * y[1] + 20 * y[0] + (7 * x - 3) * exp(-x);
	return f;
}

double** func_xy(double* y, double x, int num = 2) {
	double** f = new double* [num];
	for (size_t i = 0; i < num; i++)
		f[i] = new double[num];
	f[0][0] = 5 * y[1] - 4 * y[0] - (2 * x - 1) * exp(-x);
	f[0][1] = 5 * y[1] - 4 * y[0] - (2 * x - 1) * exp(-x);
	f[1][0] = -9 * y[1] + 20 * y[0] + (6 * x - 1) * exp(-x);
	f[1][1] = -9 * y[1] + 20 * y[0] + (8 * x - 4) * exp(-x);
	return f;
}

double* func_yy(double* y, double x, int num = 2) {
	double* f = new double [num];
	f[0] = 5 * y[1] - 4 * y[0] - x * exp(-x);
	f[1] = 5 * y[1] - 4 * y[0] - (2 * x - 1) * exp(-x);
	return f;
}

double norm(double* vec, int n) {
	double sum = 0;
	for (size_t i = 0; i < n; i++)
		sum += vec[i] * vec[i];
	return sum;
}

double* Taylor(double* y, double x, double h, int num = 2) {
	double* fi = new double[num];
	fi = sum(func(y, x), proizv(sum(func_x(y, x), proizv(func_y(y, x), func(y, x), num, num), num), h / 2, num), num);
	double* f_3 = new double[num];
	f_3 = sum(func_xx(y, x), proizv(func_y(y, x), func_x(y, x), num, num), 2);
	f_3 = sum(f_3, proizv(proizv(func_y(y, x), func_y(y, x), num, num, num), func(y, x), num, num), num);
	f_3 = sum(f_3, proizv(proizv(func_xy(y, x), func(y, x), num, num), 2, num), num);
	f_3 = sum(f_3, proizv(func_yy(y, x), norm(func(y, x), num), num), num);
	fi = sum(fi, proizv(f_3, h * h * h / 6, num), num);

	y = sum(y, proizv(fi, h, num), num);
	return y;
}

void result(double* y, double x, const double x_first, const double x_last, int steps, double eps, int num = 2) {
	double h = (x_last - x_first) / (double)steps;
	double* y1 = new double[num];
	double* y2 = new double[num];
	double* y0 = new double[num];
	y0 = y;
	int count = 0;

	std::ofstream ofs;
	ofs.open("result.txt");
	ofs << x << " " << y[0] << " " << y[1] << std::endl;
	for (size_t i = 0; i < steps || x <= x_last; i++) {
		y1 = Taylor(y0, x, h);
		y2 = Taylor(y0, x, h / 2);
		ofs << x + h << " " << y2[0] << " " << y2[1] << std::endl;
		if (fabs(sqrt(norm(sum(y1, proizv(y2, -1, num), num), num))) / 7. > eps)
			count++;
		y0 = y1;
		x += h;
	}
	ofs.close();
	x = x_first;

	if (count != 0) {
		steps *= 4;
		result(y, x, x_first, x_last, steps, eps);
	}
	else
		std::cout << "h = " << h << std::endl;
	delete[] y1, y2, y0;
}


int main(void) {
	double eps = 0.01, steps = 50;
	double* y = new double[2];
	y[0] = 0;
	y[1] = 0;
	double x_first = 0, x_last = 2;
	result(y, x_first, x_first, x_last, steps, eps);

	delete[] y;
	system("python3 graph.py");
	return 0;
}