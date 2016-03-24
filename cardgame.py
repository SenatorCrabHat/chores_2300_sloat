class Ace:
	high = 11
	low = 1

class Player:
	chips = 25
	chips_left = 25
	hands_won = 0
	hands_lost = 0

	def __init__(self, name):
		self.name = name

cardlist = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, Ace.high, Ace.high, Ace.high, Ace.high]

player1 = Player('Jason')

def stay(hit, player_hand, dealer_hand):
	import random
	if hit == 'Stay': #must turn this into a function
		while sum(dealer_hand) <= 16:
			print('The dealer has {}, totaling {}'.format(dealer_hand, sum(dealer_hand)))
			if sum(dealer_hand) > 21:
				ace_checkd(dealer_hand)
				print('The dealer busts! You win!')
				break
			if sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) > 16 and sum(dealer_hand) < 21:
				print('You lose.')
				break
			if sum(dealer_hand) <= 16:
				print('Dealer Hits!')
				deald3 = random.choice(cardlist)
				dealer_hand.append(deald3)
				ace_checkd(dealer_hand)
			if sum(dealer_hand) >= 17:
				ace_checkd(dealer_hand)
				if sum(dealer_hand) > 21:
					print('The dealer has {}, totaling {}. The dealer busts'.format(dealer_hand, sum(dealer_hand)))
					break
				elif sum(dealer_hand) == sum(player_hand):
					print('You have {}. The Dealer has {}. Push!'.format(sum(player_hand), sum(dealer_hand)))
					break
				else:
					print('The dealer has {}, totaling {}. The dealer stays'.format(dealer_hand, sum(dealer_hand)))

def ace_check(player_hand, dealer_hand):
	if Ace.high in player_hand:
		if sum(player_hand) >= 22:
			player_hand.remove(Ace.high)
			player_hand.append(Ace.low)
		if sum(dealer_hand) >= 22:
			player_hand.remove(Ace.high)
			player_hand.append(Ace.low)
		return player_hand
		return dealer_hand

def ace_checkp(player_hand):
	if Ace.high in player_hand:
		if sum(player_hand) >= 22:
			player_hand.remove(Ace.high)
			player_hand.append(Ace.low)

def ace_checkd(dealer_hand):
	if Ace.high in dealer_hand:
		if sum(dealer_hand) >= 22:
			dealer_hand.remove(Ace.high)
			dealer_hand.append(Ace.low)

def hit_func(player_hand, dealer_hand):
	import random
	while sum(player_hand) <= 21:
		deal3 = random.choice(cardlist)
		player_hand.append(deal3)
		ace_checkp(player_hand)
		if sum(player_hand) == 21:
			print('You have {}! Blackjack!'.format(player_hand))
			break
		if sum(player_hand) > 21:
			print('You Bust, {}, {}'.format(player_hand, sum(player_hand)))
			break
		if sum(player_hand) < 21:
			print('You have {}, totaling {}'.format(player_hand, sum(player_hand)))
			global hit
			hit = input('Would you like another card? (Hit/Stay)')
			if hit == 'Stay':
				return (hit)
				print(hit)
				break
	else:
		hit = 'Stay'
		return hit

def bet():
	import random
	player1 = Player
	will_play = input('How about a round of blackjack? (Y/N)')
	if will_play != 'Y' and will_play != 'N':
		while will_play != 'Y' and will_play != 'N':
			will_play = input('Please enter Y or N:')
			if will_play == 'Y':
				break
			if will_play == 'N':
				break
	while will_play == 'Y':
		if will_play == 'Y':
			print('You have {} chips'.format(player1.chips))
			try:
				player_bet = int(input('How much do you want to bet?(5 to {})'.format(player1.chips)))
			except (TypeError, ValueError):
				player_bet = int(input('Please use a numerical value between 5 and {}'.format(player1.chips)))
			if player_bet < 5:
				while player_bet < 5:
					player_bet = int(input('The minimum bet is 5. How much wil you bet?'))
					if player_bet >= 5:
						break
			if player_bet > player1.chips:
				while player_bet > player1.chips:
					player_bet = int(input('You cannot bet more than you have in the bank! Please place your bet:'))
					print(player_bet)
					if player_bet >= 5 and player_bet <= player1.chips:
						break
			print('Your bet is set at {}'.format(player_bet))
			if player_bet >= 5:
				print('Dealing!')
				hit1 = 'Stay'
				player_hand = []
				dealer_hand = []
				deal1 = random.choice(cardlist)
				deal1d = random.choice(cardlist)
				deal2 = random.choice(cardlist)
				deald2d = random.choice(cardlist)
				player_hand.append(deal1)
				player_hand.append(deal2)
				dealer_hand.append(deal1d)
				dealer_hand.append(deald2d)
				ace_check(player_hand, dealer_hand)
				print('You have {} and {}, totaling {}. The dealer is showing {}.'.format(player_hand[0], player_hand[1], sum(player_hand), dealer_hand[1]))
				hit1 = input('Would you like another card? (Hit/ Stay/ or DD(Doubledown))')
				if hit1 == 'DD':
					if player1.chips > player_bet * 2:
						player_bet = player_bet * 2
						dd_deal = random.choice(cardlist)
						player_hand.append(dd_deal)
						print('You Doubledown, your bet is now {}, and you hold {} totaling {}'.format(player_bet, player_hand, sum(player_hand)))
						hit1 = 'Stay'
					else:
						print("Sorry you don't have enough money!")
						hit1 = input('Would you still like another card?(Hit/Stay))')
				if hit1 != 'Hit' and hit1 != 'Stay':
					while hit1 != 'Hit' and hit1 != 'Stay':
						hit1 = input('Please type Hit or Stay exactly as they are shown!')
						if hit1 == 'Hit':
							break
						if hit1 == 'Stay':
							break
				if hit1 == 'Hit':
					hit_func(player_hand, dealer_hand)
					try:
						if hit == 'Stay':
							stay(hit, player_hand, dealer_hand)
					except:
						pass
				if hit1 == 'Stay':
					stay(hit1, player_hand, dealer_hand)
				try:
					if hit == 'Stay':
						stay(hit, player_hand, dealer_hand)
				except:
					pass
				if sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) < 21:
					player1.chips = player1.chips - player_bet
					print('Dealer has {} totaling {}. Dealer Wins....:('.format(dealer_hand, sum(dealer_hand)))
					player1.hands_lost = player1.hands_lost + 1
				if sum(dealer_hand) < sum(player_hand) and sum(player_hand) < 21:
					player1.chips = player1.chips + player_bet
					print('You Win! Dealer has {} totaling {}!'.format(dealer_hand, sum(dealer_hand)))
					player1.hands_won = player1.hands_won + 1
				if sum(dealer_hand) > 21 and sum(player_hand) < 21:
					player1.chips = player1.chips + player_bet
					print('You Win! You have {}, the dealer has {}!'.format(sum(player_hand), sum(dealer_hand)))
					player1.hands_won = player1.hands_won + 1
				if sum(player_hand) > 21:
					player1.chips = player1.chips - player_bet
					print('You bust, Dealer Wins....:(')
					player1.hands_lost = player1.hands_lost + 1
				if sum(player_hand) == 21:
					player1.chips = player1.chips + player_bet * 1.5
					winnings = player_bet * 1.5
					print('Blackjack pays out 1.5 times!')
					player1.hands_won = player1.hands_won + 1
		print('You have {} chips'.format(player1.chips))
		if player1.chips <= 0:
			print('Sorry, but you are out of money!')
			break
		will_play = input('Play another round?(Y/N)')
	else:
		if will_play == 'N':
			print('You won {} number of hands, and lost {} number of hands'.format(player1.hands_won, player1.hands_lost))
			print('Have a nice day')

bet()
			