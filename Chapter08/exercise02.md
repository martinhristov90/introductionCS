### Repeat the previous exercise using negative indices.

- The first item of kingdoms
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[:-5]
    'Bacteria'
    >>> 
    ```
- The last item of kingdoms
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[-1]
    'Animalia'
    >>> 
    ```
- The list ['Bacteria', 'Protozoa', 'Chromista']
    ```python
     >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
     >>> kingdom[-6:-3]
    ['Bacteria', 'Protozoa', 'Chromista']
    >>> 
    ```
- The list ['Chromista', 'Plantae', 'Fungi']
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[-4:-1]
    ['Chromista', 'Plantae', 'Fungi']
    >>> 
    ```
- The list ['Fungi', 'Animalia']
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[-2:]
    ['Fungi', 'Animalia']
    >>> 
    ```
- The empty list    
    ```python
    >>> kingdom = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
    >>> kingdom[:0]
    []
    >>> 
    ```