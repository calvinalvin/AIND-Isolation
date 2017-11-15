"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import timeit
import sample_players

from importlib import reload

TIME_LIMIT_MILLIS = 150

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        self.minimax_player = game_agent.MinimaxPlayer()

    # def test_minimax_player(self):
    #     time_millis = lambda: 1000 * timeit.default_timer()
    #     move_start = time_millis()
    #     time_left = lambda : TIME_LIMIT_MILLIS - (time_millis() - move_start)
    #
    #     print("minimax_player is ")
    #     print(self.minimax_player.get_move)
    #
    #     best_move = self.minimax_player.get_move(self.game, time_left)
    #     print('best move is ----')
    #     print(best_move)

    def test_minimax_func(self):
        minimax_player = game_agent.MinimaxPlayer(search_depth=1, score_fn=sample_players.improved_score)
        other_player = sample_players.GreedyPlayer()
        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 43]
        game = isolation.Board(minimax_player, other_player,  width=9, height=9)
        game._board_state = state

        legal_moves = game.get_legal_moves()
        move = minimax_player.get_move(game, lambda: 10)

        print(game.to_string())
        print('Available choices:')
        print(legal_moves)
        print(move)

        assert(move in legal_moves)


if __name__ == '__main__':
    unittest.main()
