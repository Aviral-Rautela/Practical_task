# Consensus Mechanism Simulation

import random

# PoW: Select miner with highest power
miners = [{"name": "MinerA", "power": random.randint(1, 100)},
          {"name": "MinerB", "power": random.randint(1, 100)},
          {"name": "MinerC", "power": random.randint(1, 100)}]
pow_winner = max(miners, key=lambda x: x["power"])
print(f"PoW: {pow_winner['name']} wins with power {pow_winner['power']}")

# PoS: Select staker with highest stake
stakers = [{"name": "StakerA", "stake": random.randint(1, 100)},
           {"name": "StakerB", "stake": random.randint(1, 100)},
           {"name": "StakerC", "stake": random.randint(1, 100)}]
pos_winner = max(stakers, key=lambda x: x["stake"])
print(f"PoS: {pos_winner['name']} wins with stake {pos_winner['stake']}")

# DPoS: Voters elect a delegate
delegates = ["DelegateA", "DelegateB", "DelegateC"]
votes = [random.choice(delegates) for _ in range(3)]
dpos_winner = max(set(votes), key=votes.count)
print(f"DPoS: {dpos_winner} selected by votes: {votes}")


# Console Explanation:

# PoW: The miner with the highest computational power is selected.

# PoS: The staker with the most coins at stake is chosen.

# DPoS: Delegates are elected by votes; the one with the most votes becomes the validator.