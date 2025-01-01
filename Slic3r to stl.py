import xml.etree.ElementTree as ET

# Load the file
tree = ET.parse('3dmodel.model')
root = tree.getroot()

# Define the namespace
ns = {'ns': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}

# Debugging: Check the structure of the XML tree
print("Inspecting XML structure...")
for child in root:
    print(child.tag, child.attrib)

# List to store vertex positions
vertices = []

# Adjust XPath for vertices with namespace
for vertex in root.findall('.//ns:resources/ns:object/ns:mesh/ns:vertices/ns:vertex', ns):
    x = float(vertex.attrib['x'])
    y = float(vertex.attrib['y'])
    z = float(vertex.attrib['z'])
    vertices.append((x, y, z))

print(f"Found {len(vertices)} vertices.")

# Open STL file for writing
with open('output_model.stl', 'w') as stl_file:
    stl_file.write('solid model\n')

    # Adjust XPath for triangles with namespace
    for triangle in root.findall('.//ns:resources/ns:object/ns:mesh/ns:triangles/ns:triangle', ns):
        v1 = int(triangle.attrib['v1'])
        v2 = int(triangle.attrib['v2'])
        v3 = int(triangle.attrib['v3'])

        # Get the coordinates of each vertex
        coord1 = vertices[v1]
        coord2 = vertices[v2]
        coord3 = vertices[v3]

        # Write the triangle facet
        stl_file.write('facet normal 0 0 0\n')  # Replace with actual normals if needed
        stl_file.write('  outer loop\n')
        stl_file.write(f'    vertex {coord1[0]} {coord1[1]} {coord1[2]}\n')
        stl_file.write(f'    vertex {coord2[0]} {coord2[1]} {coord2[2]}\n')
        stl_file.write(f'    vertex {coord3[0]} {coord3[1]} {coord3[2]}\n')
        stl_file.write('  endloop\n')
        stl_file.write('endfacet\n')

    stl_file.write('endsolid model\n')

print("STL file successfully written.")
