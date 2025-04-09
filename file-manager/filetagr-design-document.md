# FileTagr: Python Library Design Document

## 1. Project Overview

FileTagr is a Python library that implements a tagging system for file organization, allowing users to categorize files with multiple tags and search for files based on these tags and other attributes, all without physically duplicating files.

### 1.1 Core Objectives

- Create a Python library that can be installed via pip
- Provide a command-line interface (CLI) for interacting with the library
- Implement a flexible tagging system for files
- Enable powerful search capabilities based on tags and other file attributes
- Create virtual collections of files without duplication

## 2. System Architecture

The FileTagr library will be organized into several components:

### 2.1 High-Level Components

1. **Core Engine**: Implements the fundamental tagging and indexing functionality
2. **File Scanner**: Discovers and tracks files in specified directories
3. **Database Manager**: Handles storage and retrieval of file metadata and tags
4. **Query Engine**: Processes search queries and returns matching files
5. **Virtual Folder Manager**: Creates symbolic links to files in virtual folders
6. **CLI Interface**: Provides command-line access to library functions

### 2.2 Component Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   CLI Interface │────▶│   Core Engine   │────▶│  File Scanner   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                               │  ▲                      │
                               │  │                      │
                               ▼  │                      ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Virtual Folder  │◀────│ Database Manager│◀────│  Query Engine   │
│    Manager      │     └─────────────────┘     └─────────────────┘
└─────────────────┘
```

## 3. Detailed Component Design

### 3.1 Core Engine

The Core Engine will be the central module that coordinates between all other components.

#### Key Classes:

- `FileTagrEngine`: Main entry point for the library
- `ConfigManager`: Handles application configuration
- `EventManager`: Manages event subscriptions for file changes

#### Key Functions:

- `initialize()`: Set up the library
- `add_directory(path)`: Add a directory for scanning
- `remove_directory(path)`: Remove a directory from scanning
- `get_files()`: Retrieve indexed files
- `reload()`: Rescan all directories

### 3.2 File Scanner

The File Scanner will be responsible for discovering and tracking files in specified directories.

#### Key Classes:

- `FileScanner`: Performs directory scanning
- `FileWatcher`: Monitors directories for changes
- `FileMetadata`: Represents file attributes

#### Key Functions:

- `scan_directory(path)`: Recursively scan a directory
- `extract_metadata(file)`: Extract metadata from a file
- `watch_directories()`: Monitor directories for changes
- `handle_file_change(event)`: Process file change events

### 3.3 Database Manager

The Database Manager will handle the storage and retrieval of file metadata and tags.

#### Key Classes:

- `DatabaseManager`: Interface to the database
- `FileRecord`: Represents a file in the database
- `TagRecord`: Represents a tag in the database
- `FileTagMapping`: Maps files to tags

#### Key Functions:

- `initialize_database()`: Create the database schema
- `add_file(metadata)`: Add a file to the database
- `update_file(file_id, metadata)`: Update file metadata
- `remove_file(file_id)`: Remove a file from the database
- `add_tag(name, description)`: Create a new tag
- `tag_file(file_id, tag_id)`: Associate a tag with a file
- `untag_file(file_id, tag_id)`: Remove a tag from a file

### 3.4 Query Engine

The Query Engine will process search queries and return matching files.

#### Key Classes:

- `QueryEngine`: Processes file queries
- `QueryBuilder`: Builds query expressions
- `QueryResult`: Contains query results

#### Key Functions:

- `query_by_tags(tags, match_all=True)`: Find files with specified tags
- `query_by_name(pattern)`: Find files matching a name pattern
- `query_by_extension(extension)`: Find files with a specific extension
- `query_by_size(min_size, max_size)`: Find files within a size range
- `query_by_date(start_date, end_date)`: Find files modified in a date range
- `complex_query(criteria)`: Find files matching multiple criteria

### 3.5 Virtual Folder Manager

The Virtual Folder Manager will create symbolic links to files in virtual folders.

#### Key Classes:

- `VirtualFolderManager`: Manages virtual folders
- `VirtualFolder`: Represents a virtual folder

#### Key Functions:

- `create_virtual_folder(name, query)`: Create a new virtual folder
- `update_virtual_folder(folder_id, query)`: Update a virtual folder's contents
- `delete_virtual_folder(folder_id)`: Delete a virtual folder
- `refresh_virtual_folder(folder_id)`: Refresh a virtual folder's contents

### 3.6 CLI Interface

The CLI Interface will provide command-line access to the library functions.

#### Key Classes:

- `FileTagrCLI`: Command-line interface
- `CommandParser`: Parses command-line arguments

#### Key Functions:

- `initialize()`: Set up the CLI
- `parse_arguments()`: Parse command-line arguments
- `execute_command(command)`: Execute a CLI command
- `display_results(results)`: Display command results

## 4. Database Schema

The database will use SQLite for storage, with the following schema:

### 4.1 Tables

1. **files**
   - id (INTEGER PRIMARY KEY)
   - path (TEXT)
   - name (TEXT)
   - extension (TEXT)
   - size (INTEGER)
   - created_at (TIMESTAMP)
   - modified_at (TIMESTAMP)
   - last_indexed (TIMESTAMP)

2. **tags**
   - id (INTEGER PRIMARY KEY)
   - name (TEXT)
   - description (TEXT)
   - created_at (TIMESTAMP)

3. **file_tags**
   - id (INTEGER PRIMARY KEY)
   - file_id (INTEGER)
   - tag_id (INTEGER)
   - tagged_at (TIMESTAMP)
   - FOREIGN KEY (file_id) REFERENCES files(id)
   - FOREIGN KEY (tag_id) REFERENCES tags(id)

4. **virtual_folders**
   - id (INTEGER PRIMARY KEY)
   - name (TEXT)
   - path (TEXT)
   - query (TEXT)
   - created_at (TIMESTAMP)
   - updated_at (TIMESTAMP)

## 5. CLI Command Structure

The CLI will support the following commands:

### 5.1 Directory Management

- `filetagr scan <directory>`: Scan and index a directory
- `filetagr dirs`: List monitored directories
- `filetagr remove-dir <directory>`: Stop monitoring a directory

### 5.2 Tag Management

- `filetagr tags`: List all tags
- `filetagr add-tag <name> [description]`: Create a new tag
- `filetagr remove-tag <tag>`: Delete a tag

### 5.3 File Operations

- `filetagr files [--tagged <tag>] [--untagged] [--extension <ext>]`: List files
- `filetagr tag <file> <tag>`: Add a tag to a file
- `filetagr untag <file> <tag>`: Remove a tag from a file
- `filetagr file-tags <file>`: Show tags for a file
- `filetagr file-info <file>`: Show file metadata

### 5.4 Bulk Operations

- `filetagr batch-tag <pattern> <tag>`: Tag files matching a pattern
- `filetagr batch-untag <pattern> <tag>`: Untag files matching a pattern

### 5.5 Search

- `filetagr find --tags <tags> [--all] [--extension <ext>] [--name <pattern>] [--newer-than <date>] [--older-than <date>] [--min-size <size>] [--max-size <size>]`: Search for files

### 5.6 Virtual Folders

- `filetagr vfolders`: List virtual folders
- `filetagr create-vfolder <name> <query>`: Create a virtual folder
- `filetagr update-vfolder <name> <query>`: Update a virtual folder
- `filetagr delete-vfolder <name>`: Delete a virtual folder
- `filetagr refresh-vfolder <name>`: Refresh a virtual folder

### 5.7 Import/Export

- `filetagr export <file>`: Export database to a file
- `filetagr import <file>`: Import database from a file

## 6. Implementation Plan

### 6.1 Project Structure

```
filetagr/
├── __init__.py
├── cli/
│   ├── __init__.py
│   ├── commands.py
│   └── parser.py
├── core/
│   ├── __init__.py
│   ├── engine.py
│   └── config.py
├── database/
│   ├── __init__.py
│   ├── manager.py
│   ├── models.py
│   └── schema.py
├── query/
│   ├── __init__.py
│   ├── engine.py
│   └── builder.py
├── scanner/
│   ├── __init__.py
│   ├── scanner.py
│   └── watcher.py
└── vfolder/
    ├── __init__.py
    └── manager.py
```

### 6.2 Dependencies

- **SQLAlchemy**: Database ORM
- **Click**: CLI framework
- **Watchdog**: File system monitoring
- **Pathlib**: Path manipulation
- **Rich**: Terminal formatting

### 6.3 Development Phases

1. **Phase 1**: Core architecture and database setup
   - Implement database schema
   - Implement Core Engine
   - Implement basic File Scanner

2. **Phase 2**: Tagging and querying
   - Implement Database Manager
   - Implement Query Engine
   - Implement basic CLI commands

3. **Phase 3**: Virtual folders and file watching
   - Implement Virtual Folder Manager
   - Implement file watching
   - Complete CLI commands

4. **Phase 4**: Import/export and optimizations
   - Implement import/export functionality
   - Optimize performance
   - Add advanced search features

## 7. Testing Strategy

### 7.1 Unit Tests

- Test each component in isolation
- Use pytest for test framework
- Achieve >80% code coverage

### 7.2 Integration Tests

- Test component interactions
- Test database operations
- Test file system operations

### 7.3 End-to-End Tests

- Test CLI commands
- Test virtual folder creation
- Test file watching and updates

## 8. Package Distribution

### 8.1 Package Configuration

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="filetagr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "click",
        "watchdog",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "filetagr=filetagr.cli.commands:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A file tagging and organization library",
    keywords="file, organization, tags, search",
    url="https://github.com/yourusername/filetagr",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
```

### 8.2 Installation

```
pip install filetagr
```

## 9. Performance Considerations

- Implement caching for frequent queries
- Use indexes on database tables
- Optimize file scanning for large directories
- Implement batch operations for tag management
- Use lazy loading for file metadata

## 10. Security Considerations

- Validate all file paths to prevent path traversal
- Sanitize user input for database queries
- Handle file permissions appropriately
- Implement error handling for file operations
