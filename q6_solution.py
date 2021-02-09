INF = 10000

def on_segment(p, q, r):
	return (q[0] <= max(p[0], r[0]) and 
	q[0] >= min(p[0], r[0]) and 
	q[1] <= max(p[1], r[1]) and 
	q[1] >= min(p[1], r[1]))

def orientation(p, q, r):
	'''
	in: three point represented as tuples,
	return 0 if pqr are colinear
	return 1 if pqr are clockwise
	return -1 if pqr are counterclockwise
	'''
	o = ((q[1] - p[1]) * (r[0] - q[0]) -
		  (q[0] - p[0]) * (r[1] - q[1]))
	return 0 if o == 0 else (1 if o > 0 else -1)

def intersect(p1, q1, p2, q2):
	'''return True if (p1,q1) intersects (p2,q2),
	False otherwise
	'''
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)

	if (o1 != o2) and (o3 != o4):
		return True

	return 
	(
		(o1 == 0 and on_segment(p1, p2, q1)) or
		(o2 == 0 and on_segment(p1, q2, q1)) or
		(o3 == 0 and on_segment(p2, p1, q2)) or
		(o4 == 0 and on_segment(p2, q1, q2))
	)

def inside_polygon(points, P):
	'''we implement the Ray casting algorithm
	return True if P is inside the polygon, 
	False otherwise
	'''
	
	n = len(points)

	#return false immediatly if there are less than 3 points in the list
	if n < 3:
		return False

	#creat the inf_right point such that (P, inf_right) is a ray line
	inf_right = (INF, P[1])

	#whenever the ray line hits the polygon, we increment the counter by one
	num_intersection = 0

	for i in range(n):
		#retrive the current vertex and the next vertex
		current_vertex = points[i]
		next_vertex = points[(i + 1) % n]

		if intersect(current_vertex, next_vertex, P, inf_right):
			#handle special case: the ray pass by a vertex
			if orientation(current_vertex, P, next_vertex) == 0:
				return on_segment(current_vertex, P, next_vertex)

			#update counter
			num_intersection += 1

	return num_intersection % 2 == 1


def main(polygon_file, points_file, output_file_name):
	#prepair the files
	f_poly = open(polygon_file, 'r')
	f_points = open(points_file, 'r')
	f_out = open(output_file_name, 'w')

	#read file and construct polygon
	polygon = []
	for vertex in f_poly:
		coordinate = vertex.replace('\t', ' ').replace('\n', '').split(' ')
		x1, x2 = coordinate[0], coordinate[1]
		polygon.append((int(x1), int(x2)))


	#for each point, determin if it is in the polygon or not
	for point in f_points:
		coordinate = point.replace('\t', ' ').replace('\n', '').split(' ')
		if len(coordinate) == 2:
			x1, x2 = coordinate[0], coordinate[1]

			#check if the point is in the polygon or not
			is_inside_polygon = inside_polygon(polygon, (int(x1), int(x2)))
			f_out.write(x1 + '\t' + x2 + '\t' + ('inside\n' if is_inside_polygon else 'outside\n'))





if __name__ == '__main__':
	main('input_question_6_polygon', 'input_question_6_points', 'output_question_6')



