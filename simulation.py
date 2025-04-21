import random
import matplotlib.pyplot as plt

# --- Collatz Trust Core ---
def collatz_sequence(n):
	steps = 0
	peak = n
	while n != 1:
		n = n // 2 if n % 2 == 0 else 3 * n + 1
		peak = max(peak, n)
		steps += 1
	return steps, peak

def trust_score(steps, peak):
	return steps + peak // 100  # Chaotic signatures are strong

# --- Zero Trust Model (simplified) ---
def zero_trust_model(identity):
	verified = random.choice([True, False])
	mfa = random.choice([True, False])
	return verified and mfa

# --- Simulation: Collatz Rebels vs Zero Trust Agents ---
def simulate_battle(num_identities=1000, trust_threshold=30):
	rebels = []
	agents = []
	
	for entropy in range(1, num_identities + 1):
		steps, peak = collatz_sequence(entropy)
		c_score = trust_score(steps, peak)
		zero_trusted = zero_trust_model(entropy)
		
		if c_score >= trust_threshold and not zero_trusted:
			rebels.append((entropy, c_score))  # Trusted by Collatz, rejected by Zero Trust
		elif zero_trusted and c_score < trust_threshold:
			agents.append((entropy, c_score))  # Trusted by Zero Trust, weak Collatz chaos

	return rebels, agents

# --- Run the Fight ---
rebels, agents = simulate_battle()

print(f"🧬 Collatz Rebels: {len(rebels)} identities")
print(f"🛡️  Zero Trust Agents: {len(agents)} identities")
print("🔥 Resistance: Trust chaos. Down with blind verification.")

# --- Optional Plot ---
plt.figure(figsize=(10, 5))
plt.bar(['Collatz Rebels', 'Zero Trust Agents'], [len(rebels), len(agents)], color=['red', 'blue'])
plt.title("🔥 Battle for the Trust Stack: Collatz vs Zero Trust")
plt.ylabel("Identities")
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
