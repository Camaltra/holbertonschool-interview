#include "sandpiles.h"
#include <stdio.h>

/**
 * sandpiles_sum - computes the sum of two sandpiles
 *
 * @grid1: stable sandpile to sum
 * @grid2: stable sandpile to sum
 *
 * Return: No return
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	/*summation grid1 and grid2*/
	for (i = 0; i < N_ROW; i++)
	{
		for (j = 0; j < N_COL; j++)
			grid1[i][j] += grid2[i][j];
	}

	/*dispatche with neighbours if not stable*/
	while (is_stable(grid1) == 0)
	{
		printf("=\n");
		print_grid(grid1);
		dispatch(grid1);
	}
}

/**
 * is_stable - check if the sandpile is stable
 *
 * @grid: sandpile to check
 *
 * Return: 1 if stable, 0 otherwise
 */
int is_stable(int grid[3][3])
{
	int i, j;

	for (i = 0; i < N_ROW; i++)
	{
		for (j = 0; j < N_COL; j++)
		{
			if (grid[i][j] > 3)
				return (0);
		}
	}
	return (1);
}

/**
 * topple -- Topple the sandpile
 *
 * @grid: The grid to topple
 * @i: The i row
 * @j: The j row
 *
 * Return: Nothing
 */
void topple(int grid[3][3], int i, int j)
{
	grid[i][j] -= 4;

	if (i - 1 >= 0)
		grid[i - 1][j] += 1;
	if (j + 1 < N_COL)
		grid[i][j + 1] += 1;
	if (i + 1 < N_ROW)
		grid[i + 1][j] += 1;
	if (j - 1 >= 0)
		grid[i][j - 1] += 1;
}

/**
 * dispatch - dispatch the grains to the neighbours in a sandpile
 *
 * @grid: sandpile to arrange in order to be stable
 *
 * Return: No return
 */
void dispatch(int grid[3][3])
{
	int i, j;
	int saved_grid[3][3];

	for (i = 0; i < N_ROW; i++)
	{
		for (j = 0; j < N_COL; j++)
			saved_grid[i][j] = grid[i][j];
	}

	for (i = 0; i < N_ROW; i++)
	{
		for (j = 0; j < N_COL; j++)
		{
			if (saved_grid[i][j] > 3)
				topple(grid, i, j);
		}
	}
}

/**
 * print_grid - Print 3x3 grid
 *
 * @grid: 3x3 grid
 *
 * Return: Nothing
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < N_ROW; i++)
	{
		for (j = 0; j < N_COL; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}
