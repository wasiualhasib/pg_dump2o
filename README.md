# pg_dump2o
Enhanced PostgreSQL Backup Tool


```markdown
# pg_dump2o

`pg_dump2o` is an enhanced PostgreSQL backup tool developed by **Sheikh Wasiu Al Hasib**. It simplifies PostgreSQL backups by providing options for both **directory** and **SQL** formats, with support for optional tarball and gzip compression.

## Features

- Backup in **SQL** or **Directory** format.
- Supports parallel jobs and compression for directory backups.
- Create **tar** or **gzip-compressed tar** archives of backups.
- Specify individual tables or a list of tables for selective backups.
- Easy-to-use command-line interface.

## Installation

### Prerequisites

- PostgreSQL client tools (`pg_dump`).
- Bash shell.
- Required tools: `tar`, `gzip`.

### From RPM Package

You can install the tool directly from an RPM package if available:

```bash
sudo rpm -ivh pg_dump2o-1.0-1.noarch.rpm
```

### From Source

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/pg_dump2o.git
    cd pg_dump2o
    ```

2. Copy the script to your `PATH`:
    ```bash
    chmod +x pg_dump2o.sh
    mv pg_dump2o.sh /usr/local/bin/pg_dump2o
    ```

3. Verify the command:
    ```bash
    pg_dump2o --help
    ```

## Usage

`pg_dump2o` provides options for creating PostgreSQL backups in multiple formats with tarball and compression support.

### Basic Syntax

```bash
pg_dump2o -u <username> -d <database> -f <backup_path> [options]
```

### Options

| Option             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `-u <username>`    | PostgreSQL username                                                        |
| `-d <database>`    | Name of the database to back up                                            |
| `-f <backup_path>` | Path where the backup will be stored                                       |
| `-t <tables>`      | Comma-separated list of tables to back up                                  |
| `-T <tables_file>` | File containing a list of tables to back up                                |
| `-j <jobs>`        | Number of parallel jobs (for Directory format only)                        |
| `-c <level>`       | Compression level (0-9, for Directory format only)                        |
| `-S`               | Use SQL format instead of Directory format                                |
| `-R`               | Create a tar archive of the backup                                         |
| `-Z`               | Create a gzip-compressed tar archive of the backup                        |
| `--help`           | Display usage information                                                 |

### Examples

#### Full Backup in Directory Format
```bash
pg_dump2o -u postgres -d mydb -f /backups -j 8 -c 6
```

#### SQL Backup with Gzip Compression
```bash
pg_dump2o -u postgres -d mydb -f /backups -S -Z
```

#### Backup Specific Tables
```bash
pg_dump2o -u postgres -d mydb -f /backups -t table1,table2
```

#### Backup Tables from a File
```bash
pg_dump2o -u postgres -d mydb -f /backups -T /path/to/tables_list.txt
```

#### Full Backup with Tarball
```bash
pg_dump2o -u postgres -d mydb -f /backups -R
```

#### Help
```bash
pg_dump2o --help
```

## Building an RPM Package

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/pg_dump2o.git
    cd pg_dump2o
    ```

2. Create the RPM build environment:
    ```bash
    mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
    cp pg_dump2o /usr/local/bin/
    ```

3. Generate the spec file dynamically:
    ```bash
    ./generate_spec.sh
    ```

4. Build the RPM:
    ```bash
    rpmbuild -ba ~/rpmbuild/SPECS/pg_dump2o.spec
    ```

5. Install the RPM:
    ```bash
    sudo rpm -ivh ~/rpmbuild/RPMS/noarch/pg_dump2o-1.0-1.noarch.rpm
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Developed by **Sheikh Wasiu Al Hasib**  
Visit [wasiualhasib.com](https://wasiualhasib.com) for more details.
```

---

### **How to Use the README**
1. Save the content above as `README.md` in the root of your project directory.
2. If using GitHub, push the changes to your repository:
   ```bash
   git add README.md
   git commit -m "Add README file"
   git push origin main
   ```
