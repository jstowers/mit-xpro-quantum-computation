# Linear Algebra

Saturday, September 27, 2025

## Projector


## Transpose

A transpose of a vector _transforms_ the vector's orientation.

A row vector transforms into a column vector.  A column vector transforms into a row vector.

Example:

Vector ${v}$ is a column vector represented as _n_ rows and 1 column.

${v^T}$ becomes a row vector with 1 row and _n_ columns.

## Tensor Product

A tensor product is a mathematical operation that creates a new _vector space_ from two existing ones.

The properties of the two vector spaces are combined into a single, larger entity.

### Tensor Product in Quantum

In quantum, you must calculate the tensor product for a two-qubit system in order to create a _composite_ Hilbert space that can represent the _combined_ state of the two individiual qubits, their interactions and correlations, such as _entanglement_.



## Linearity

In quantum mechanics, __linearity__ means that quantum _operators_ obey the rules of linear algebra:

  1. they preserve linear combinations

  2. they preserve scalar multiplications of states

Operators can include:

  1. Unitary operators, $U$
  
  2. Hamiltonians
  
  3. Measurement projectors

Linearity is a _foundational property_ derived from the mathematical structure of quantum theory:

  1. States are __vectors__ in a complex Hilbert space; and

  2. Operators are __linear maps__ on that space.

### Example

A quantum superposition state, $\ket{\psi}$, is defined as:

$\ket{\psi} = \alpha \ket{\phi} + \beta \ket{\chi}$

where $\alpha$ and $\beta$ are complex scalars.  The vectors $\ket{\phi}$ and $\ket{\chi}$ represent two generic quantum states.

When quantum operator, $O$, (e.g. a unitary U), acts on $\ket{\psi}$, then:

${O \space \ket{\phi} = \alpha \space {O\ket{\phi}} + \beta \space {O\ket{\chi}}}$

This is the __superposition principle__:  operations on a superposition are equivalent to superposing the operations on each component.

## Unitarity

Quantum evolution is unitary.

${U}$ is a linear operator that:

  1. preserves the inner product; and

  2. acts on the full Hilbert space

Unitary operators _must_ map spaces of the _same_ dimension to themselves.  They cannot "create" extra dimensions out of nothing.

Unitarity is a property of __closed__ systems.  The total quantum state evolves deterministically without environmental interference.