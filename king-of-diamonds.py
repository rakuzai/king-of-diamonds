import random

def generate_prediction_num():
    return [random.randint(0,100) for i in range(4)]

def calculate_the_number(prediction_num):
    total_pred_num = sum(prediction_num)
    number = int(total_pred_num * 0.8)
    closest_pred = min(prediction_num, key=lambda x:abs(x-number))
    print(number)
    return closest_pred

def decrease_score(data_player, index):
    for i, player in enumerate(data_player):
        if i != index:
            player[1] -= 1

def determine_winner(closest_pred, prediction_num, data_player):
    if closest_pred == prediction_num[0]:
        decrease_score(data_player, 0)
        print('King Diamond win!')
    elif closest_pred == prediction_num[1]:
        decrease_score(data_player, 1)
        print('Player 1 win!')
    elif closest_pred == prediction_num[2]:
        decrease_score(data_player, 2)
        print('Player 2 win!')
    elif closest_pred == prediction_num[3]:
        decrease_score(data_player, 3)
        print('Chishiya win!')
    else:
        print('erorr')
    print(data_player)

def kingOfDiamond(count, data_player):
    print('Babak ke-{}'.format(count))
    prediction_num = generate_prediction_num()
    closest_pred = calculate_the_number(prediction_num)
    print('King of Diamond Prediction: {} \nPlayer 1 Prediction: {} \nPlayer 2 Prediction: {} \nChishiya Prediction: {}'.format(prediction_num[0], prediction_num[1], prediction_num[2], prediction_num[3]))
    determine_winner(closest_pred, prediction_num, data_player)
    
    if count < 4:
        kingOfDiamond(count + 1, data_player)
    elif count == 4:
        biggest_poin = max(player[1] for player in data_player)
        for player in data_player[:]:
            if player[1] != biggest_poin:
                data_player.remove(player)
        print('{} Winning The Game!'.format(data_player[0][0]))

    return data_player

data = [
        ['King of Diamond', -1],
        ['Player 1', -1],
        ['Player 2', -1],
        ['Chishiya', -1]
    ]

print(kingOfDiamond(1, data))
