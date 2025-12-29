import cirq
import numpy as np

def quantum_optimize(costs, shots=1000):
    """
    costs: list of normalized costs (0–1)
    lower cost => higher probability
    """

    n = len(costs)
    qubits = cirq.LineQubit.range(n)
    circuit = cirq.Circuit()

    # Encode costs into amplitudes
    for i, cost in enumerate(costs):
        theta = np.pi * (1 - cost)
        circuit.append(cirq.ry(theta).on(qubits[i]))

    circuit.append(cirq.measure(*qubits, key="m"))

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=shots)

    measurements = result.measurements["m"]

    counts = {i: 0 for i in range(n)}

    for row in measurements:
        if 1 in row:
            idx = list(row).index(1)
            counts[idx] += 1

    best_index = max(counts, key=counts.get)

    return best_index, counts
