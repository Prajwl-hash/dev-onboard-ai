def create_chunk(
    file_data,
    content,
    chunk_index,
    start_line=None,
    end_line=None
):
    metadata = {
        "file_path": file_data["file_path"],
        "extension": file_data["extension"],
        "chunk_index": chunk_index
    }

    if start_line is not None:
        metadata["start_line"] = start_line

    if end_line is not None:
        metadata["end_line"] = end_line

    return {
        "content": content,
        "metadata": metadata
    }


def chunk_markdown(file_data):
    lines = file_data["content"].splitlines()

    sections = []
    current_section = []

    for line in lines:

        # A new Markdown heading starts a new section
        if line.startswith("#") and current_section:
            sections.append("\n".join(current_section))
            current_section = []

        current_section.append(line)

    # Add the final section
    if current_section:
        sections.append("\n".join(current_section))

    chunks = []

    for section in sections:

        if section.strip():
            chunk = create_chunk(
                file_data=file_data,
                content=section,
                chunk_index=len(chunks)
            )

            chunks.append(chunk)

    return chunks


def chunk_by_lines(
    file_data,
    chunk_size=50,
    overlap=10
):
    lines = file_data["content"].splitlines()

    chunks = []

    start = 0

    while start < len(lines):

        end = min(
            start + chunk_size,
            len(lines)
        )

        chunk_lines = lines[start:end]

        chunk_content = "\n".join(chunk_lines)

        if chunk_content.strip():

            chunk = create_chunk(
                file_data=file_data,
                content=chunk_content,
                chunk_index=len(chunks),
                start_line=start + 1,
                end_line=end
            )

            chunks.append(chunk)

        # We reached the end of the file
        if end == len(lines):
            break

        # Move forward while keeping overlap
        start += chunk_size - overlap

    return chunks


def chunk_file(file_data):

    extension = file_data["extension"]
    lines = file_data["content"].splitlines()

    # Markdown has natural heading boundaries
    if extension == ".md":
        return chunk_markdown(file_data)

    # Keep small files intact
    if len(lines) <= 50:

        return [
            create_chunk(
                file_data=file_data,
                content=file_data["content"],
                chunk_index=0,
                start_line=1,
                end_line=len(lines)
            )
        ]

    # Any large file uses overlapping line chunks
    return chunk_by_lines(file_data)