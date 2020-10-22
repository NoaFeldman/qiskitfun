from qiskit import(
  QuantumCircuit,
  QuantumRegister,
  ClassicalRegister,
  execute,
  Aer)

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')


#### Quaestion 1a

# Create a Quantum Circuit with one quantum bit and one classical result bit
qa = QuantumRegister(1)
ca = ClassicalRegister(1)
circuit_a = QuantumCircuit(qa, ca)

# Add a H gate on qubit 0
circuit_a.h(qa[0])
circuit_a.measure(qa, ca)

# Execute the circuit on the qasm simulator
job1a = execute(circuit_a, simulator, shots=1000)

# Grab results from the job
result1a = job1a.result()

# Returns counts
counts1a = result1a.get_counts(circuit_a)
print("Total count for (1a):", counts1a)

# Draw the circuit
circuit_a.draw(output='mpl', filename='question1a.png')

#### Quaestion 1b

# Create a Quantum Circuit with two quantum bits and two classical result bits
qb = QuantumRegister(2)
cb = ClassicalRegister(2)
circuit_b = QuantumCircuit(qb, cb)

# Add a H gate on qubit 0
circuit_b.h(qb[0])
# Add a CNOT gate with 0 the control bit and 1 the target bit
circuit_b.cx(qb[0], qb[1])
circuit_b.measure(qb, cb)

# Execute the circuit on the qasm simulator
job1b = execute(circuit_b, simulator, shots=1000)

# Grab results from the job
result1b = job1b.result()

# Returns counts
counts1b = result1b.get_counts(circuit_b)
print("Total count for (1b):", counts1b)

# Draw the circuit
circuit_b.draw(output='mpl', filename='question1b.png')

#### Question 2

number_of_bits = 6
q2 = QuantumRegister(number_of_bits)
c2 = ClassicalRegister(number_of_bits)
circuit_2 = QuantumCircuit(q2, c2)

for i in range(number_of_bits):
    circuit_2.h(q2[i])

circuit_2.measure(q2, c2)
circuit_2.draw(output='mpl', filename='question2.png')

number_of_shots = 2**number_of_bits * 1000
job2 = execute(circuit_2, simulator, shots=number_of_shots)
result2 = job2.result()
counts2 = result2.get_counts(circuit_2)

sample_state = 31

# Get the binary string representation for our sample state
def toBinary(sample, n):
    return ''.join(str(1 & int(sample) >> i) for i in range(n)[::-1])

number_of_occurences = counts2[toBinary(sample_state, number_of_bits)]
print('Total count for i = ', sample_state, ':', number_of_occurences)
print('Estimated probability for i = ', sample_state, ': ', number_of_occurences/number_of_shots)

#### Question 3
number_of_bits = 5
q3 = QuantumRegister(number_of_bits)
c3 = ClassicalRegister(number_of_bits)
circuit_3 = QuantumCircuit(q3, c3)

circuit_3.h(q3[0])
for i in range(1, number_of_bits):
    circuit_3.cx(q3[i - 1], q3[i])

circuit_3.measure(q3, c3)

job3 = execute(circuit_3, simulator, shots=1000)
result3 = job3.result()
counts3 = result3.get_counts(circuit_3)
print("Total count for (3):", counts3)

# Draw the circuit
circuit_3.draw(output='mpl', filename='question3.png')

