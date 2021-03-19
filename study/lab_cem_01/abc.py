# Найти номер позиции нового руководителя
def josephus(list_position):
	skip = 14
	cur_id = skip
	while len(list_position) > 1:
		list_position.pop(cur_id)
		cur_id = (cur_id + 14) % len(list_position)
	return list_position[0]

# Вычислить расстояние от Mxgobgwq до нового руководителя
def count_dis(cur_pos, pos):
	if cur_pos > pos // 2:
		return pos + 1 - cur_pos
	return cur_pos - 1

# Определить номер безопасной позиции, которая ближайшей к Mxgobgwq
def print_ans(list_dd, n):
	for x in range(1, (n+1)//2):
		if list_dd[x] == 0:
			print(x)
			return
	print("Недостаточно данных")

while 1:
	n, m = map(int, input().split())
	if not n and not m:
		break
	dd = [0] * (m+3)
	for x in range(n, m+1):
		pos1 = josephus([i for i in range(1, x+1)])
		pos2 = josephus([1] + [i for i in range(x, 1, -1)])
		dd[count_dis(pos1, x)] = 1
		dd[count_dis(pos2, x)] = 1
	print_ans(dd, n)