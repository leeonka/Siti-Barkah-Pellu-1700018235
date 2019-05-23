from ai_pkg.planning import PlanningProblem, Action, goal_test
from ai_pkg.utils import expr

def double_tennis_problem():

	initial = 'At(A, LeftBaseline) & At(B, RightNet) &Approaching(Ball, RighBaseLine) & Team(A,B) & Team (B,A)'
	goal = 'Returned(Ball) & At(a, RightNet) & At(a, LeftNet)'
	action = [Action('Hit(player, Ball, loc)',
		 precound='Approaching(Ball, loc) & At(player, loc)',
		 effect= 'Returned(Ball)')
	Action('Go(player, to, loc)',
		precound='At(player, loc)',
		effect='At(player, to)')]
	return PlanningProblem(init=initial,
		goals=goal,
		actions=action)

if __name__ == '__main__':
	p=double_tennis_problem()
	print(goal_test(p.goals, p.init))
	solution = [expr('Go(A, RighBaseLine, LeftBaseline'),
	expr('Hit(A, Ball, RighBaseLine)',)]

	for action in solution:
		p.act(action)
		print(goal_test(p.goals,p.init))